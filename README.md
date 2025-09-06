
# Nexus3Client

[![PyPI version](https://badge.fury.io/py/nexus3client.svg)](https://pypi.org/project/nexus3client/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python Versions](https://img.shields.io/pypi/pyversions/nexus3client.svg)](https://pypi.org/project/nexus3client/)
[![Build Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()

A lightweight **Python client** for interacting with **Sonatype Nexus3** repositories via REST API.  
This package helps you **search**, **list**, and **delete components** from Nexus3 repositories with minimal code.

---

## 📦 Features

- 🔍 Search for components in Nexus3 repositories
- 🗑️ Delete components easily
- 🧩 Supports authentication for secure Nexus3 servers
- ⚡ Built for automation and CI/CD integration
- ✅ Fully tested with **pytest**

---

## 📥 Installation

Install the package from **PyPI**:

```bash
pip install nexus3client
```

Or install from source:

```bash
git clone https://github.com/<your-username>/nexus3client.git
cd nexus3client
pip install -e .
```

---

## 🚀 Usage

### **1. Import and Initialize**

```python
from nexus3client import Nexus3Client

# Initialize the client
client = Nexus3Client()
```

### **2. Search for Components**

```python
results = client.search_components(
    base_url="http://localhost:8084",
    repository="test-repo",
    username="admin",
    password="admin123",
    verify_ssl=False,
    timeout=10,
    *fields=["id", "repository"]
)

print(results)
```

**Example Output:**
```json
[
    {
        "id": "d2a3f2b6f3f2",
        "repository": "test-repo",
        "name": "my-artifact",
        "version": "1.0.0"
    }
]
```

### **3. Delete Components**

```python
results = client.search_components(
    "http://localhost:8084", 
    "test-repo", 
    "admin", 
    "admin123", 
    False, 
    10, 
    "id"
)

for result in results:
    component_id = result.get("id")
    client.delete_components(
        "http://localhost:8084",
        component_id,
        "admin",
        "admin123",
        False,
        10
    )
```

---

## 🧪 Running Tests

We use **pytest** for testing. To run tests locally:

```bash
pytest tests/
```

**Example Test (`tests/test_nexus3client.py`):**

```python
import pytest
from nexus3client import Nexus3Client

client = Nexus3Client()

def test_nexus3_search():
    results = client.search_components(
        "http://localhost:8084", 
        "test-repo", 
        "admin", 
        "admin123", 
        False, 
        10, 
        "id", 
        "repository"
    )
    assert isinstance(results, list)
    assert len(results) >= 0

def test_nexus3_delete():
    results = client.search_components(
        "http://localhost:8084", 
        "test-repo", 
        "admin", 
        "admin123", 
        False, 
        10, 
        "id"
    )
    assert isinstance(results, list)
    assert len(results) > 0
    for result in results:
        component_id = result.get("id")
        assert component_id is not None
        client.delete_components(
            "http://localhost:8084",
            component_id,
            "admin",
            "admin123",
            False,
            10
        )
```

---

## 📂 Project Structure

```
nexus3client/
├── nexus3client/
│   ├── __init__.py
│   ├── client.py
├── tests/
│   ├── test_nexus3client.py
├── README.md
├── setup.py
├── pyproject.toml
└── LICENSE
```

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an [issue](https://github.com/<your-username>/nexus3client/issues) or submit a pull request.

---

## 📧 Contact

**Author:** Prabhu Thangaraj  
**Email:** thangaraj.prabhu@gmail.com  
**GitHub:** [https://github.com/thangap-cloud](https://github.com/thangap-cloud)

---

## 🔗 References

- [Sonatype Nexus3 REST API Docs](https://help.sonatype.com/repomanager3/rest-and-integration-api)

---

