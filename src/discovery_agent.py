
from src.knowledge_base import load_knowledge_base
from src.retriever import KnowledgeRetriever
from src.lead_extractor import LeadExtractor
from src.lead_scorer import LeadScorer


class DiscoveryAgent:
    """Coordinate retrieval, lead extraction and lead scoring."""

    def __init__(self):

        knowledge = load_knowledge_base()

        self.retriever = KnowledgeRetriever(knowledge)
        self.extractor = LeadExtractor()
        self.scorer = LeadScorer()

    def process_enquiry(self, enquiry: str) -> dict:
        """Process a customer enquiry through all three modules."""

        if not enquiry or not enquiry.strip():
            raise ValueError("Customer enquiry cannot be empty.")

        # 1. Extract customer requirements
        lead = self.extractor.extract(enquiry)

        # 2. Retrieve relevant company information
        retrieval_query = " ".join(
            part
            for part in [lead.service or ""] + lead.requirements
            if part
        ).strip()

        knowledge_results = (
            self.retriever.search(
                retrieval_query,
                top_k=3,
                min_score=0.05
            )
            if retrieval_query
            else []
        )

        # 3. Calculate information completeness score
        scoring_result = self.scorer.score(lead)

        # 4. Generate questions for missing information
        question_map = {
            "service": "Which service are you interested in?",
            "budget": "What is your approximate project budget?",
            "timeline": "When would you like the project completed?",
            "requirements": "Could you share the key features you need?",
            "business profile": "What type of business do you operate?",
            "location": "Where is your business located?"
        }

        follow_up_questions = [
            question_map[field]
            for field in scoring_result["missing_fields"]
            if field in question_map
        ]

        # 5. Return complete discovery report
        return {
            "enquiry": enquiry,
            "company_knowledge": knowledge_results,
            "lead_details": lead.model_dump(),
            "lead_score": scoring_result,
            "follow_up_questions": follow_up_questions
        }
