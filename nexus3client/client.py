import requests
import logging
from requests.auth import HTTPBasicAuth
from .config import DEFAULT_TIMEOUT, DEFAULT_VERIFY_SSL

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Nexus3Client:
    def __init__(self):
        self.nexus3 = None

    def search_components(self, base_url, repository, username, password, verify_ssl=DEFAULT_VERIFY_SSL, timeout=DEFAULT_TIMEOUT, *fields):
        results = []
        if not base_url.startswith('http'):
            logger.warning("Invalid base URL must start with http or https '%s'" % base_url)
            return {}
        url = f"{base_url.rstrip('/')}/service/rest/v1/components?repository={repository}"
        try:
            response = requests.get(url, auth=HTTPBasicAuth(username, password), verify=verify_ssl, timeout=timeout)
            response.raise_for_status()
            logger.info(f"Successfully searched components in repository {repository}")
            data = response.json()
            items = data.get("items", [])
            for item in items:
                result = {}
                for field in fields:
                    keys = field.split(".")
                    current = item
                    for key in keys:
                        if isinstance(current, list):
                            # If current is a list, collect all matching values
                            values = []
                            for sub_item in current:
                                if isinstance(sub_item, dict) and key in sub_item:
                                    values.append(sub_item[key])
                            current = values
                            break
                        elif isinstance(current, dict):
                            current = current.get(key)
                        else:
                            current = None
                            break
                    result[field] = current
                results.append(result)
            return results
        except requests.HTTPError as e:
            logger.warning(f"Error searching components in repository {repository}")
            logger.warning(f"HTTPError: {e.response.status_code} - {e.response.text}")
        except requests.RequestException as e:
            logger.warning(f"Error searching components in repository {repository} : {e}")
        return {}

    def delete_components(self,base_url, componentId, username, password, verify_ssl=DEFAULT_VERIFY_SSL, timeout=DEFAULT_TIMEOUT):
        if not base_url.startswith('http'):
            logger.warning("Invalid base URL must start with http or https '%s'" % base_url)
            return {}
        print(f"componentId: {componentId}")
        try:
            url = f"{base_url.rstrip('/')}/service/rest/v1/components/{componentId}"
            response = requests.delete(url, auth=HTTPBasicAuth(username, password), verify=verify_ssl, timeout=timeout)
            response.raise_for_status()
            logger.info(f"Successfully found component {componentId} and deleted ")
        except requests.HTTPError as e:
                logger.warning(f"Error finding component {componentId}")
                logger.warning(f"HTTPError: {e.response.status_code} - {e.response.text}")
        except requests.RequestException as e:
                logger.warning(f"Error finding component {componentId} : {e}")
        return {}