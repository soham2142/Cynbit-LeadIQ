
from src.discovery_agent import DiscoveryAgent

agent = DiscoveryAgent()

enquiry = """
I own a dental clinic in Pune.
I need a professional website with online
appointment booking and payment gateway.
My budget is ₹40,000 and I need it within 1 month.
"""

result = agent.process_enquiry(enquiry)

print("\n===== COMPANY KNOWLEDGE =====")
for item in result["company_knowledge"]:
    print(item["title"], "|", item["score"])

print("\n===== LEAD DETAILS =====")
print(result["lead_details"])

print("\n===== LEAD SCORE =====")
print(result["lead_score"])

print("\n===== FOLLOW-UP QUESTIONS =====")
print(result["follow_up_questions"])
