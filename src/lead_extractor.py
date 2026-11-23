
import re
from typing import Optional

from pydantic import BaseModel, Field


class LeadDetails(BaseModel):
    business_type: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None
    service: Optional[str] = None
    requirements: list[str] = Field(default_factory=list)
    budget: Optional[str] = None
    timeline: Optional[str] = None


class LeadExtractor:

    INDUSTRY_KEYWORDS = {
        "Healthcare": ["dental clinic", "hospital", "clinic", "doctor"],
        "Fitness": ["gym", "fitness centre", "fitness center"],
        "Education": ["school", "college", "institute", "coaching"],
        "Retail": ["shop", "store", "retail"],
        "Real Estate": ["real estate", "property", "builder"]
    }

    SERVICE_KEYWORDS = {
        "Website Development": [
            "website", "web development", "web application"
        ],
        "AI Automation": [
            "ai automation", "automation", "ai agent"
        ],
        "Mobile App Development": [
            "mobile app", "android app", "ios app"
        ],
        "Digital Marketing": [
            "digital marketing", "seo", "social media marketing"
        ],
        "CRM Development": [
            "crm", "customer relationship management"
        ]
    }

    REQUIREMENT_KEYWORDS = [
        "online appointment booking",
        "appointment booking",
        "payment gateway",
        "admin dashboard",
        "user dashboard",
        "e-commerce",
        "ecommerce",
        "chatbot",
        "login system",
        "booking system"
    ]

    def extract(self, text: str) -> LeadDetails:

        if not text or not text.strip():
            raise ValueError("Enquiry text cannot be empty.")

        normalized = text.lower()

        industry = self._find_category(
            normalized, self.INDUSTRY_KEYWORDS
        )

        service = self._find_category(
            normalized, self.SERVICE_KEYWORDS
        )

        business_type = self._find_business_type(normalized)
        location = self._extract_location(text)
        budget = self._extract_budget(text)
        timeline = self._extract_timeline(normalized)

        requirements = [
            item for item in self.REQUIREMENT_KEYWORDS
            if item in normalized
        ]

        return LeadDetails(
            business_type=business_type,
            industry=industry,
            location=location,
            service=service,
            requirements=requirements,
            budget=budget,
            timeline=timeline
        )

    @staticmethod
    def _find_category(text, categories):

        for category, keywords in categories.items():
            if any(keyword in text for keyword in keywords):
                return category

        return None

    @staticmethod
    def _find_business_type(text):

        business_types = [
            "dental clinic", "hospital", "clinic", "gym",
            "fitness centre", "fitness center", "school",
            "college", "shop", "store"
        ]

        for business in business_types:
            if business in text:
                return business.title()

        return None

    @staticmethod
    def _extract_location(text):

        match = re.search(
            r"\b(?:in|at|based in|located in)\s+"
            r"([A-Z][A-Za-z]+(?:[\s-][A-Z][A-Za-z]+)*)",
            text
        )

        return match.group(1) if match else None

    @staticmethod
    def _extract_budget(text):

        patterns = [
            r"(?:₹|rs\.?\s*)(\d[\d,]*(?:\.\d+)?)\s*"
            r"(lakhs?|lacs?|k)?",
            r"(\d[\d,]*(?:\.\d+)?)\s*"
            r"(lakhs?|lacs?|k)\s*(?:rupees|rs)?"
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)

            if match:
                amount = match.group(1)
                unit = match.group(2) or ""
                return f"{amount} {unit}".strip()

        return None

    @staticmethod
    def _extract_timeline(text):

        word_numbers = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6"
        }

        pattern = (
            r"\b(\d+|one|two|three|four|five|six)\s*"
            r"(days?|weeks?|months?|years?)\b"
        )

        match = re.search(pattern, text)

        if match:
            number = match.group(1)
            unit = match.group(2)
            number = word_numbers.get(number, number)

            return f"{number} {unit}"

        if "as soon as possible" in text:
            return "As soon as possible"

        return None
