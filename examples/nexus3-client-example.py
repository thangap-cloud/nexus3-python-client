from nexus3client import Nexus3Client

# Create a client instance
client = Nexus3Client()

# --------------------------------------------
# 1️⃣ Search for all components in a repository
# --------------------------------------------
results = client.search_components(
    base_url="http://localhost:8084",    # Nexus3 URL
    repository="test-repo",             # Repository name
    username="admin",                   # Nexus username
    password="admin123",                # Nexus password
    verify_ssl=False,                   # Disable SSL verification if using HTTP or self-signed certs
    timeout=10,                         # Request timeout (in seconds)
    *fields=["id", "name", "version"]   # Fields you want to extract from the API response
)

print("=== All Components ===")
for component in results:
    print(component)

# Example Output:
# {'id': 'abc123', 'name': 'my-artifact', 'version': '1.0.0'}
# {'id': 'xyz456', 'name': 'another-artifact', 'version': '2.1.0'}


# -------------------------------------------------------
# 2️⃣ Search for components and fetch nested JSON fields
# -------------------------------------------------------
# If your components have nested metadata like "assets.downloadUrl",
# you can fetch it using dot notation in the *fields argument.

results = client.search_components(
    "http://localhost:8084",
    "test-repo",
    "admin",
    "admin123",
    False,
    10,
    "id",
    "repository",
    "assets.downloadUrl"  # Example of nested field extraction
)

print("\n=== Components with Download URLs ===")
for component in results:
    print(component)

# Example Output:
# {'id': 'abc123', 'repository': 'test-repo', 'assets.downloadUrl': ['http://localhost:8084/repository/.../file.jar']}


# -----------------------------------------------------
# 3️⃣ Delete a specific component using its component ID
# -----------------------------------------------------
component_id = "abc123"  # Example component ID to delete

client.delete_components(
    base_url="http://localhost:8084",
    componentId=component_id,
    username="admin",
    password="admin123",
    verify_ssl=False,
    timeout=10
)
print(f"Deleted component: {component_id}")


# ----------------------------------------------------------------
# 4️⃣ Delete ALL components in a repository (use with caution ⚠️)
# ----------------------------------------------------------------
results = client.search_components(
    "http://localhost:8084",
    "test-repo",
    "admin",
    "admin123",
    False,
    10,
    "id"
)

if results:
    for component in results:
        component_id = component.get("id")
        if component_id:
            client.delete_components(
                "http://localhost:8084",
                component_id,
                "admin",
                "admin123",
                False,
                10
            )
    print("✅ Deleted all components in test-repo")
else:
    print("ℹ️ No components found to delete.")


# -----------------------------------------------------------------
# 5️⃣ Handling SSL verification and request timeouts (best practice)
# -----------------------------------------------------------------
# Example when connecting to a Nexus3 server with a valid SSL cert:
results = client.search_components(
    base_url="https://nexus3.company.com",
    repository="secure-repo",
    username="admin",
    password="securePass",
    verify_ssl=True,      # Enable SSL verification for secure environments
    timeout=30,           # Increase timeout for slower networks
    *fields=["id", "name", "version"]
)

print("\n=== Secure Repository Results ===")
print(results)

