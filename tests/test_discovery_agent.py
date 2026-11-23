
import pytest

from src.discovery_agent import DiscoveryAgent


@pytest.fixture
def agent():
    return DiscoveryAgent()


def test_complete_enquiry(agent):

    enquiry = (
        "I own a dental clinic in Pune. "
        "I need a website with online appointment booking. "
        "My budget is ₹40,000 and I need it within 1 month."
    )

    result = agent.process_enquiry(enquiry)

    assert result["lead_details"]["industry"] == "Healthcare"
    assert result["lead_details"]["location"] == "Pune"
    assert result["lead_score"]["score"] == 100
    assert result["lead_score"]["priority"] == "High"
    assert result["follow_up_questions"] == []


def test_incomplete_enquiry(agent):

    enquiry = "I need a website for my business."

    result = agent.process_enquiry(enquiry)

    assert result["lead_score"]["score"] == 25
    assert result["lead_score"]["priority"] == "Low"
    assert len(result["follow_up_questions"]) > 0


def test_knowledge_retrieval(agent):

    result = agent.process_enquiry(
        "Does Cynbit provide AI automation?"
    )

    assert len(result["company_knowledge"]) > 0


def test_empty_enquiry(agent):

    with pytest.raises(ValueError):
        agent.process_enquiry("")


def test_output_contains_all_modules(agent):

    result = agent.process_enquiry(
        "I need a website for my gym in Pune."
    )

    assert "company_knowledge" in result
    assert "lead_details" in result
    assert "lead_score" in result
    assert "follow_up_questions" in result
    