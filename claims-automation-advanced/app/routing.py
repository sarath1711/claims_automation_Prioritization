def route_claim(complexity, priority_score):
    if complexity == "SIMPLE":
        return "✅ Auto-Processed"
    else:
        return f"⚠️ Sent for Human Review (Priority: {priority_score})"