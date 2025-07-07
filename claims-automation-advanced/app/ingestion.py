import os

def load_claim(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Claim file not found: {file_path}")
    with open(file_path, "rb") as f:
        return f.read()