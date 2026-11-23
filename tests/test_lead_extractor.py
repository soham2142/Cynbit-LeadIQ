
import pytest

from src.lead_extractor import LeadExtractor, LeadDetails


@pytest.fixture
def extractor():
    return LeadExtractor()


def test_extract_complete_enquiry(extractor):
    enquiry = (
        "I own a dental clinic in Pune. "
        "I need a professional website with online "
        "appointment booking. My budget is ₹40,000 "
        "and I want it completed within one month."
    )

    result = extractor.extract(enquiry)

    assert isinstance(result, LeadDetails)
    assert result.business_type == "Dental Clinic"
    assert result.industry == "Healthcare"
    assert result.location == "Pune"
    assert result.service == "Website Development"
    assert "online appointment booking" in result.requirements
    assert result.budget == "40,000"
    assert result.timeline == "1 month"


def test_extract_gym_enquiry(extractor):
    enquiry = (
        "I run a gym in Mumbai and need a website "
        "with a booking system."
    )

    result = extractor.extract(enquiry)

    assert result.business_type == "Gym"
    assert result.industry == "Fitness"
    assert result.location == "Mumbai"
    assert result.service == "Website Development"
    assert "booking system" in result.requirements


def test_extract_missing_information(extractor):
    result = extractor.extract("I need a website for my business.")

    assert result.service == "Website Development"
    assert result.budget is None
    assert result.timeline is None


def test_empty_enquiry(extractor):
    with pytest.raises(ValueError):
        extractor.extract("")


def test_budget_with_lakh(extractor):
    result = extractor.extract(
        "My budget is 2 lakhs for a website."
    )

    assert result.budget == "2 lakhs"
