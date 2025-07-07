def assess_complexity(fields):
    if fields["amount"] > 10000 or fields["date"] == "unknown":
        return "COMPLEX", 90
    else:
        return "SIMPLE", 10