
import streamlit as st
from src.discovery_agent import DiscoveryAgent

# Page configuration
st.set_page_config(
    page_title="Cynbit LeadIQ",
    page_icon="🎯",
    layout="wide"
)

# Initialize agent
@st.cache_resource
def load_agent():
    return DiscoveryAgent()


agent = load_agent()

# Header
st.title("🎯 Cynbit LeadIQ")
st.subheader("AI-Powered Lead Intelligence & Discovery Agent")

st.markdown(
    "Convert customer enquiries into structured lead insights "
    "with knowledge retrieval and requirement analysis."
)

st.divider()

# Customer enquiry input
st.header("📝 Customer Enquiry")

enquiry = st.text_area(
    "Enter the customer's enquiry:",
    placeholder=(
        "Example: I own a dental clinic in Pune. "
        "I need a website with online appointment booking. "
        "My budget is ₹40,000 and I need it within 1 month."
    ),
    height=150
)

# Process enquiry
if st.button("🚀 Analyse Enquiry", type="primary"):
    if not enquiry.strip():
        st.warning("Please enter a customer enquiry.")
    else:
        try:
            with st.spinner("Analysing customer enquiry..."):
                result = agent.process_enquiry(enquiry)

            st.success("Enquiry analysed successfully!")

            # Lead score
            st.header("📊 Lead Intelligence")

            score = result["lead_score"]

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Completeness Score",
                f'{score["score"]}/100'
            )

            col2.metric(
                "Lead Priority",
                score["priority"]
            )

            col3.metric(
                "Scoring Type",
                "Rule-based"
            )

            st.caption(
                "This score measures information completeness, "
                "not the probability of conversion."
            )

            st.divider()

            # Extracted details
            st.header("👤 Extracted Lead Details")

            lead = result["lead_details"]

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Business Type:**", lead.get("business_type") or "Not identified")
                st.write("**Industry:**", lead.get("industry") or "Not identified")
                st.write("**Location:**", lead.get("location") or "Not identified")

            with col2:
                st.write("**Service:**", lead.get("service") or "Not identified")
                st.write("**Budget:**", lead.get("budget") or "Not identified")
                st.write("**Timeline:**", lead.get("timeline") or "Not identified")

            st.write("**Requirements:**")
            if lead.get("requirements"):
                for requirement in lead["requirements"]:
                    st.write(f"- {requirement}")
            else:
                st.write("No specific requirements identified.")

            st.divider()

            # Score explanation
            st.header("📈 Score Explanation")

            for reason in score["reasons"]:
                st.write(f"✅ {reason}")

            if score["missing_fields"]:
                st.warning("Missing information:")
                for field in score["missing_fields"]:
                    st.write(f"- {field}")
            else:
                st.success("All tracked information fields are complete.")

            st.divider()

            # Follow-up questions
            st.header("❓ Suggested Follow-up Questions")

            questions = result["follow_up_questions"]

            if questions:
                for index, question in enumerate(questions, start=1):
                    st.write(f"{index}. {question}")
            else:
                st.success("No follow-up questions required.")

            st.divider()

            # Knowledge retrieval
            st.header("📚 Relevant Cynbit Knowledge")

            knowledge = result["company_knowledge"]

            if knowledge:
                for item in knowledge:
                    with st.expander(item["title"]):
                        st.write(item["content"])
                        st.caption(
                            f'Category: {item["category"]} | '
                            f'Relevance Score: {item["score"]}'
                        )
            else:
                st.info(
                    "No sufficiently relevant company knowledge "
                    "was found for this enquiry."
                )

        except Exception as error:
            st.error(f"An error occurred: {error}")

# Footer
st.divider()
st.caption("Cynbit LeadIQ | AI/ML Engineering Assessment Prototype")
