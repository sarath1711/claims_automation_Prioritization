from app.ingestion import load_claim
from app.preprocessing import extract_text_from_any_file
from app.extraction import extract_fields
from app.complexity import assess_complexity
from app.routing import route_claim

def main():
    file_path = "sample_claim.pdf"  # Supports .jpg, .png, .pdf, .txt

    # Pipeline
    text = extract_text_from_any_file(file_path)
    fields = extract_fields(text)
    complexity, score = assess_complexity(fields)
    result = route_claim(complexity, score)

    # 💡 Output
    print("\n" + "=" * 40)
    print("📄  CLAIM PROCESSING RESULT")
    print("=" * 40)
    print(f"💰 Extracted Amount: ${fields['amount']}")
    print(f"📅 Date Found: {fields['date']}")
    print(f"🧠 Complexity: {complexity}")
    print(f"🎯 Priority Score: {score}")
    print(f"🚦 Routing Decision: {result}")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    main()
