# Cynbit LeadIQ – Technical Approach Report

## 1. Project Overview

**Project Name:** Cynbit LeadIQ  
**Project Type:** AI-Powered Lead Intelligence and Discovery Agent  
**Technology:** Python, Streamlit, Scikit-learn, Pydantic

Cynbit LeadIQ is a prototype designed to process customer enquiries, extract structured business requirements, retrieve relevant company information, and assess lead information completeness.

The system helps organize incoming enquiries and provides suggested follow-up questions so that a human team member can better understand customer requirements.

## 2. Problem Statement

Customer enquiries often arrive as unstructured natural-language messages. Important details such as business type, industry, location, required services, budget, timeline, and project requirements may be scattered throughout the message.

Manually reviewing these enquiries can require additional time and may result in incomplete information.

Cynbit LeadIQ addresses this problem by converting unstructured enquiries into structured lead information and identifying missing details.

## 3. Proposed Solution

The proposed solution consists of five major stages:

1. Customer submits a natural-language enquiry.
2. Lead extraction identifies important business and project details.
3. Knowledge retrieval searches the company knowledge base for relevant information.
4. Rule-based scoring calculates the completeness of the extracted lead.
5. Follow-up question generation identifies missing information.

The results are displayed through an interactive Streamlit dashboard.

## 4. System Architecture

### Architecture Components

**1. User Interface – Streamlit**

- Accepts customer enquiries.
- Displays extracted lead details.
- Shows completeness score and priority.
- Displays relevant company knowledge.
- Presents suggested follow-up questions.

**2. Knowledge Base – JSON**

- Stores structured company information.
- Contains company overview, services, products, contact information, and project delivery information.

**3. Knowledge Retrieval – TF-IDF**

- Converts knowledge documents into numerical vectors using TF-IDF.
- Uses cosine similarity to rank relevant documents.
- Returns the most relevant company information based on the enquiry.

**4. Lead Extraction – Python and Pydantic**

- Identifies business type and industry.
- Extracts service requirements.
- Identifies location, budget, and timeline.
- Collects relevant project requirements.
- Uses a Pydantic model to structure the extracted information.

**5. Lead Scoring – Rule-Based Approach**

- Calculates a lead information completeness score.
- Assigns High, Medium, or Low priority.
- Identifies missing information.

**6. Discovery Agent**

- Coordinates the extraction, retrieval, scoring, and follow-up question generation modules.
- Combines the outputs into a structured response.

## 5. Technology Stack

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python       | Core programming language    |
| Streamlit    | Interactive web dashboard    |
| Scikit-learn | TF-IDF and cosine similarity |
| Pydantic     | Structured data validation   |
| JSON         | Company knowledge storage    |
| Pytest       | Automated testing            |

## 6. Lead Scoring Methodology

The prototype uses a transparent rule-based completeness scoring mechanism.

| Parameter                  |  Weight |
| -------------------------- | ------: |
| Service                    |      25 |
| Budget                     |      20 |
| Timeline                   |      20 |
| Requirements               |      20 |
| Business Type and Industry |      10 |
| Location                   |       5 |
| **Total**                  | **100** |

### Priority Classification

- High: Score of 75 or above.
- Medium: Score from 45 to 74.
- Low: Score below 45.

The score represents the completeness of the available lead information. It does not represent the probability of customer conversion or purchase.

## 7. Workflow

1. Customer enters an enquiry through the Streamlit interface.
2. Discovery Agent validates the input.
3. Lead Extractor identifies relevant information.
4. Knowledge Retriever searches the company knowledge base.
5. Lead Scorer calculates the completeness score.
6. Missing information is identified.
7. Follow-up questions are generated.
8. Results are displayed on the dashboard.

## 8. Evaluation and Testing

The project includes automated tests for the core components.

The implemented test coverage includes:

- Lead extraction.
- Lead scoring.
- Knowledge retrieval.
- Discovery Agent workflow.
- Input validation and error handling.

**Current automated test status:** 15 tests passed.

An additional evaluation script (`evaluation.py`) has been created to test field-level extraction performance using synthetic customer enquiries.

The evaluation script compares expected and extracted values for industry, service, location, budget, and timeline.

The measured field extraction accuracy should be reported after executing and reviewing the evaluation results.

## 9. Limitations

- The current extraction system uses keyword-based and rule-based logic.
- TF-IDF retrieval may not understand complex semantic relationships.
- Lead scoring is based on information completeness rather than predictive machine learning.
- The knowledge base is limited to the information currently stored in the JSON file.
- Follow-up questions are generated using predefined rules.
- The prototype does not automatically contact customers or update an external CRM.

## 10. Future Enhancements

- Integrate an LLM for more flexible requirement extraction.
- Implement semantic search using embeddings.
- Add grounded question-answering with source references.
- Integrate CRM systems.
- Add human approval and lead assignment workflows.
- Expand the evaluation dataset and measure extraction and retrieval performance.
- Introduce multilingual enquiry processing.

## 11. Conclusion

Cynbit LeadIQ demonstrates a modular approach to transforming unstructured customer enquiries into structured lead intelligence.

By combining structured extraction, TF-IDF-based knowledge retrieval, transparent rule-based scoring, and automated follow-up question generation, the prototype provides a foundation for improving the customer enquiry discovery process.

The modular architecture also allows future integration of LLMs, semantic retrieval, and CRM automation.
