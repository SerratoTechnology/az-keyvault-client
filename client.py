from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# URL of your Key Vault
key_vault_url = "https://KEYVAULT_NAME.vault.azure.net"

# Name of the secret you want to read
secret_name = "SECRET_NAME"  # Example: "MyFirstSecret"

# Automatic authentication with your local credentials
credential = DefaultAzureCredential()

# Create Key Vault client
client = SecretClient(vault_url=key_vault_url, credential=credential)

# Retrieve the secret
retrieved_secret = client.get_secret(secret_name)

# Display the secret value
print(f"The secret value is: {retrieved_secret.value}")