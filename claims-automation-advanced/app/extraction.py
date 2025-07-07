import re

def extract_fields(text):
    amount = re.search(r'\$\s?(\d+)', text)
    date = re.search(r'\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b', text)

    return {
        "amount": int(amount.group(1)) if amount else 0,
        "date": date.group(1) if date else "unknown"
    }