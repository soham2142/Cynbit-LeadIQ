
import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KNOWLEDGE_PATH = PROJECT_ROOT / "data" / "company_knowledge.json"


def load_knowledge_base(
    file_path: str | Path = DEFAULT_KNOWLEDGE_PATH
) -> list[dict[str, Any]]:
    """Load and validate Cynbit's knowledge entries from a JSON file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Knowledge file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        knowledge = json.load(file)

    if not isinstance(knowledge, list):
        raise ValueError("Knowledge base must contain a JSON list.")

    required_fields = {"id", "category", "title", "content", "source"}

    for index, item in enumerate(knowledge):
        if not isinstance(item, dict):
            raise ValueError(f"Entry {index} must be a JSON object.")

        missing_fields = required_fields - item.keys()

        if missing_fields:
            raise ValueError(
                f"Entry {index} is missing fields: {missing_fields}"
            )

        if not isinstance(item["content"], str) or not item["content"].strip():
            raise ValueError(f"Entry {index} has empty content.")

    return knowledge
