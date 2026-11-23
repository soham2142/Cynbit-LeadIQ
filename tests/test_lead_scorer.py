
import pytest

from src.lead_extractor import LeadDetails
from src.lead_scorer import LeadScorer


@pytest.fixture
def scorer():
    return LeadScorer()


def test_complete_lead_gets_100(scorer):

    lead = LeadDetails(
        business_type="Dental Clinic",
        industry="Healthcare",
        location="Pune",
        service="Website Development",
        requirements=["appointment booking"],
        budget="40000",
        timeline="1 month"
    )

    result = scorer.score(lead)

    assert result["score"] == 100
    assert result["priority"] == "High"


def test_incomplete_lead_gets_low_score(scorer):

    lead = LeadDetails()

    result = scorer.score(lead)

    assert result["score"] == 0
    assert result["priority"] == "Low"


def test_medium_priority(scorer):

    lead = LeadDetails(
        service="Website Development",
        budget="30000"
    )

    result = scorer.score(lead)

    assert result["score"] == 45
    assert result["priority"] == "Medium"


def test_missing_fields_are_reported(scorer):

    lead = LeadDetails(
        service="Website Development"
    )

    result = scorer.score(lead)

    assert "budget" in result["missing_fields"]
    assert "timeline" in result["missing_fields"]
    assert "requirements" in result["missing_fields"]


def test_score_never_exceeds_100(scorer):

    lead = LeadDetails(
        business_type="Gym",
        industry="Fitness",
        location="Pune",
        service="Website Development",
        requirements=["booking system", "payment gateway"],
        budget="50000",
        timeline="2 months"
    )

    result = scorer.score(lead)

    assert 0 <= result["score"] <= 100
