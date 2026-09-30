import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SKILLS_FILE = BASE_DIR / "data" / "skills.json"


with open(SKILLS_FILE, "r", encoding="utf-8") as file:
    SKILL_DATA = json.load(file)


def get_all_skills():

    skills = {}

    for category in SKILL_DATA.values():

        for canonical_name, aliases in category.items():

            skills[canonical_name] = aliases

    return skills


def normalize_text(text: str):

    text = text.lower()

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_skills(text: str):

    normalized_text = normalize_text(text)

    skill_dictionary = get_all_skills()

    found_skills = set()

    for canonical_name, aliases in skill_dictionary.items():

        for alias in aliases:

            alias = alias.lower()

            pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

            if re.search(pattern, normalized_text):

                found_skills.add(canonical_name)

                break

    return sorted(found_skills)