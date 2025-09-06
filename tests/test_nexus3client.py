import pytest
from nexus3client import Nexus3Client

client = Nexus3Client()

def test_nexus3_search():
    results = client.search_components("http://localhost:8084","test-repo", "admin", "admin123",False,10, "id","repository")
    assert isinstance(results, list)
    assert len(results) >= 0  # Adjust based on expected result

def test_nexus3_delete():
    results = client.search_components("http://localhost:8084","test-repo", "admin", "admin123",False,10, "id")
    assert isinstance(results, list), "search_components() should return a list"
    assert len(results) > 0, f"No components found in repo"
    for result in results:
        component_id = result.get("id")
        assert component_id is not None, "Component ID should not be None"
        client.delete_components("http://localhost:8084",component_id, "admin", "admin123",False,10)
    updated_results = client.search_components("http://localhost:8084","test-repo", "admin", "admin123",False,10, "id")
    for updated_result in updated_results:
        updated_component_id=updated_result.get("id")
        remaining_ids = [r.get("id") for r in results]
        assert updated_component_id not in remaining_ids, f"Component {updated_component_id} was not deleted successfully!"

if __name__ == "__main__":
    pytest.main()

