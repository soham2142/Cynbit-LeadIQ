
import json
from src.lead_extractor import LeadExtractor
from src.lead_scorer import LeadScorer


# Synthetic evaluation dataset
TEST_DATA = [
    {
        "enquiry": (
            "I own a dental clinic in Pune. "
            "I need a website with online appointment booking. "
            "My budget is Rs 40000 and I need it within 1 month."
        ),
        "expected": {
            "industry": "Healthcare",
            "service": "Website Development",
            "location": "Pune",
            "budget": "40000",
            "timeline": "1 month"
        }
    },
    {
        "enquiry": (
            "I run a gym in Mumbai. "
            "I need AI automation for my business. "
            "My budget is Rs 50000 and I need it within 2 months."
        ),
        "expected": {
            "industry": "Fitness",
            "service": "AI Automation",
            "location": "Mumbai",
            "budget": "50000",
            "timeline": "2 months"
        }
    },
    {
        "enquiry": (
            "I operate an education institute in Pune. "
            "I need a mobile app development solution. "
            "My budget is Rs 100000 and I need it within 3 months."
        ),
        "expected": {
            "industry": "Education",
            "service": "Mobile App Development",
            "location": "Pune",
            "budget": "100000",
            "timeline": "3 months"
        }
    }
]


def normalize(value):
    """Normalize values for comparison."""
    if value is None:
        return ""

    return str(value).lower().replace(",", "").replace("₹", "").replace("rs", "").strip()


def evaluate():
    extractor = LeadExtractor()
    scorer = LeadScorer()

    total_fields = 0
    correct_fields = 0
    results = []

    for index, test_case in enumerate(TEST_DATA, start=1):

        enquiry = test_case["enquiry"]
        expected = test_case["expected"]

        lead = extractor.extract(enquiry)
        extracted = lead.model_dump()

        score_result = scorer.score(lead)

        case_correct = 0

        for field, expected_value in expected.items():

            total_fields += 1

            actual_value = extracted.get(field)

            is_correct = (
                normalize(actual_value) == normalize(expected_value)
            )

            if is_correct:
                correct_fields += 1
                case_correct += 1

            results.append({
                "test_case": index,
                "field": field,
                "expected": expected_value,
                "actual": actual_value,
                "correct": is_correct
            })

        print(f"\nTest Case {index}")
        print("-" * 40)
        print("Extracted Lead:", extracted)
        print("Completeness Score:", score_result["score"])
        print("Priority:", score_result["priority"])
        print("Correct Fields:", f"{case_correct}/{len(expected)}")

    accuracy = (
        correct_fields / total_fields * 100
        if total_fields else 0
    )

    print("\n" + "=" * 45)
    print("       EVALUATION SUMMARY")
    print("=" * 45)

    print("Total Test Cases:", len(TEST_DATA))
    print("Total Fields Tested:", total_fields)
    print("Correct Fields:", correct_fields)
    print("Incorrect Fields:", total_fields - correct_fields)
    print(f"Field Extraction Accuracy: {accuracy:.2f}%")

    # Save detailed evaluation results
    report = {
        "total_test_cases": len(TEST_DATA),
        "total_fields": total_fields,
        "correct_fields": correct_fields,
        "incorrect_fields": total_fields - correct_fields,
        "field_extraction_accuracy": round(accuracy, 2),
        "results": results
    }

    with open("evaluation_results.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print("\nDetailed results saved to evaluation_results.json")


if __name__ == "__main__":
    evaluate()
