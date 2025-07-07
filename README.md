
# 🧾 Claims Processing Automation and Prioritization

This project automates the processing of simple claims and intelligently prioritizes complex ones for human review using rule-based logic and optional AI/ML capabilities.

---

## 🚀 Features

- 📥 Accepts claim files in `.pdf`, `.jpg`, `.png`, and `.txt` formats
- 🧠 Analyzes text using OCR (Tesseract) and PDF parsing
- 🔍 Extracts key information: Claim Amount, Date, etc.
- ⚖️ Assesses complexity based on rules or AI model
- 📊 Outputs clear routing decision: Auto-Processed or Sent for Review

---

## 🧱 Project Structure

claims-automation-advanced/
├── main.py # Entry point
├── requirements.txt # Python dependencies
├── app/
│ ├── ingestion.py # Loads claim files
│ ├── preprocessing.py # OCR / PDF / Text extraction
│ ├── extraction.py # Field extraction (amount, date)
│ ├── complexity.py # Complexity assessment (rules or ML)
│ ├── routing.py # Final decision: route or auto-process


---

## ⚙️ Installation

1. **Clone this repo or extract the ZIP**
2. Install dependencies:

```bash
pip install -r requirements.txt

🧪 Running the App
Place a sample claim file (e.g., sample_claim.pdf) in the project root

Update file_path in main.py if needed

Run the system:

bash
Copy
Edit
python main.py

✨ Sample Output
markdown
Copy
Edit
========================================
📄  CLAIM PROCESSING RESULT
========================================
💰 Extracted Amount: $12000
📅 Date Found: 06/05/2024
🧠 Complexity: COMPLEX
🎯 Priority Score: 90
🚦 Routing Decision: ⚠️ Sent for Human Review (Priority: 90)
========================================
