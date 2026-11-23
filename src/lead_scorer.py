
from src.lead_extractor import LeadDetails


class LeadScorer:
    """Calculate a transparent lead information completeness score."""

    def score(self, lead: LeadDetails) -> dict:

        total_score = 0
        reasons = []
        missing_fields = []

        # 1. Service identification: 25 points
        if lead.service:
            total_score += 25
            reasons.append("Service identified: +25")
        else:
            missing_fields.append("service")

        # 2. Budget information: 20 points
        if lead.budget:
            total_score += 20
            reasons.append("Budget provided: +20")
        else:
            missing_fields.append("budget")

        # 3. Project timeline: 20 points
        if lead.timeline:
            total_score += 20
            reasons.append("Timeline provided: +20")
        else:
            missing_fields.append("timeline")

        # 4. Project requirements: 20 points
        if lead.requirements:
            total_score += 20
            reasons.append("Requirements provided: +20")
        else:
            missing_fields.append("requirements")

        # 5. Business type and industry: 10 points
        if lead.business_type and lead.industry:
            total_score += 10
            reasons.append("Business profile identified: +10")
        else:
            missing_fields.append("business profile")

        # 6. Location: 5 points
        if lead.location:
            total_score += 5
            reasons.append("Location provided: +5")
        else:
            missing_fields.append("location")

        # Determine information completeness category
        if total_score >= 75:
            priority = "High"
        elif total_score >= 45:
            priority = "Medium"
        else:
            priority = "Low"

        return {
            "score": total_score,
            "priority": priority,
            "reasons": reasons,
            "missing_fields": missing_fields,
            "score_type": "Rule-based information completeness"
        }
