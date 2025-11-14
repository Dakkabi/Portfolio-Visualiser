from backend.src.services.security.secrets import generate_symmetric_key

print(f"CHACHA Valid Key: {generate_symmetric_key()}")