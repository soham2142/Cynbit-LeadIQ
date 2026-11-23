# Cynbit LeadIQ – Evaluation Report

## 1. Evaluation Overview

The purpose of this evaluation is to measure the field-level extraction performance of Cynbit LeadIQ using synthetic customer enquiries.

The evaluation checks whether the system correctly identifies important customer and project information.

## 2. Evaluation Dataset

- Total test cases: 3
- Total fields evaluated: 15
- Fields evaluated:
  - Industry
  - Service
  - Location
  - Budget
  - Timeline

## 3. Evaluation Results

| Metric                    | Result |
| ------------------------- | -----: |
| Total Test Cases          |      3 |
| Total Fields Tested       |     15 |
| Correct Fields            |     15 |
| Incorrect Fields          |      0 |
| Field Extraction Accuracy |   100% |

## 4. Accuracy Calculation

Field extraction accuracy is calculated using:

Accuracy = (Correct Fields / Total Fields Tested) × 100

Accuracy = (15 / 15) × 100

**Final Field Extraction Accuracy: 100%**

## 5. Observations

- All 15 evaluated fields were correctly extracted.
- The system successfully identified industry and service categories.
- Location, budget, and timeline extraction worked correctly for the tested examples.
- The evaluation dataset contained synthetic customer enquiries.

## 6. Limitations

- The evaluation dataset is small and contains only three test cases.
- Results may differ for more complex or ambiguous customer enquiries.
- Exact-match evaluation does not measure semantic correctness.
- The reported accuracy applies only to the evaluated fields and test cases.

## 7. Conclusion

Cynbit LeadIQ achieved 100% field extraction accuracy across 15 evaluated fields from three synthetic customer enquiries.

This result demonstrates that the current extraction logic performed correctly on the selected test dataset. Further testing with a larger and more diverse dataset is required before making broader performance claims.
