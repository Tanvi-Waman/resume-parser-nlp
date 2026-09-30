import re

from app.services.skill_extractor import extract_skills


MONTHS = (
    "january|february|march|april|may|june|"
    "july|august|september|october|november|december|"
    "jan|feb|mar|apr|jun|jul|aug|sep|sept|oct|nov|dec"
)


DATE_PATTERN = re.compile(
    rf"\b("
    rf"(?:{MONTHS})"
    rf"\s+\d{{4}}"
    rf"|"
    rf"\d{{4}}"
    rf")"
    rf"\s*[-–—]\s*"
    rf"(?:"
    rf"(?:{MONTHS})\s+\d{{4}}"
    rf"|"
    rf"present"
    rf"|"
    rf"current"
    rf"|\d{{4}}"
    rf")\b",
    re.IGNORECASE
)


def find_duration(lines):

    for line in lines:

        match = DATE_PATTERN.search(line)

        if match:
            return match.group(0)

    return None


def looks_like_role(line):

    role_keywords = [
        "developer",
        "engineer",
        "intern",
        "analyst",
        "manager",
        "designer",
        "consultant",
        "specialist",
        "administrator",
        "architect",
        "scientist",
        "lead",
        "associate"
    ]

    lower_line = line.lower()

    return any(
        keyword in lower_line
        for keyword in role_keywords
    )


def find_role(lines):

    for line in lines:

        if looks_like_role(line):
            return line

    return None


def looks_like_company(line):

    company_keywords = [
        "technologies",
        "technology",
        "solutions",
        "systems",
        "software",
        "services",
        "ltd",
        "limited",
        "pvt",
        "private",
        "inc",
        "corp",
        "corporation"
    ]

    lower_line = line.lower()

    return any(
        keyword in lower_line
        for keyword in company_keywords
    )


def find_company(lines, role):

    for line in lines:

        if line == role:
            continue

        if looks_like_company(line):
            return line

    return None


def remove_metadata_lines(lines, role, company, duration):

    description = []

    for line in lines:

        if line == role:
            continue

        if company and line == company:
            continue

        if duration and line == duration:
            continue

        description.append(line)

    return description


def parse_experience(lines):

    if not lines:
        return {
            "role": None,
            "company": None,
            "duration": None,
            "technologies": [],
            "description": []
        }

    role = find_role(lines)

    duration = find_duration(lines)

    company = find_company(lines, role)

    description = remove_metadata_lines(
        lines,
        role,
        company,
        duration
    )

    # Extract technologies from the entire experience section
    experience_text = " ".join(lines)

    technologies = extract_skills(experience_text)

    return {
        "role": role,
        "company": company,
        "duration": duration,
        "technologies": technologies,
        "description": description
    }
