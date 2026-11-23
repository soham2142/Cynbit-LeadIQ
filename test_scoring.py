from src.lead_extractor import LeadExtractor
from src.lead_scorer import LeadScorer

enquiry = """
I own a dental clinic in Pune.
I need a professional website with online
appointment booking and payment gateway.
My budget is ₹40,000 and I need it within 1 month.
"""

extractor = LeadExtractor()
scorer = LeadScorer()

lead = extractor.extract(enquiry)
result = scorer.score(lead)

print("\nEXTRACTED LEAD")
print(lead.model_dump_json(indent=4))

print("\nLEAD SCORE")
print(result)
