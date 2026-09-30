import re
import spacy


nlp = spacy.load("en_core_web_sm")


def extract_email(text: str):

    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_phone(text: str):

    pattern = r"(?<!\d)(?:\+91[\s-]?)?[6-9]\d{9}(?!\d)"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_linkedin(text: str):

    pattern = (
        r"(?:https?://)?"
        r"(?:www\.)?"
        r"linkedin\.com/in/"
        r"[A-Za-z0-9_-]+"
    )

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

    if match:
        return match.group()

    return None


def extract_github(text: str):

    pattern = (
        r"(?:https?://)?"
        r"(?:www\.)?"
        r"github\.com/"
        r"[A-Za-z0-9_-]+"
    )

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

    if match:
        return match.group()

    return None


def extract_name(text: str):

    # ------------------------------------------------
    # Method 1: Look at the first few lines of resume
    # ------------------------------------------------

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    # Common words that should NOT be considered names
    excluded_words = {
        "resume",
        "curriculum vitae",
        "cv",
        "javascript",
        "python",
        "java",
        "developer",
        "engineer",
        "student",
        "software",
        "skills",
        "education",
        "experience",
        "projects",
        "certifications",
        "contact"
    }

    for line in lines[:10]:

        # Ignore very long lines
        if len(line) > 50:
            continue

        # Ignore lines containing email/URLs
        if "@" in line:
            continue

        if "http" in line.lower():
            continue

        # Remove unnecessary characters
        cleaned = re.sub(
            r"[^A-Za-z\s.'-]",
            "",
            line
        ).strip()

        if not cleaned:
            continue

        words = cleaned.split()

        # A normal person's name usually has 2-4 words
        if not 2 <= len(words) <= 4:
            continue

        # Reject known non-name words
        if any(
            word.lower() in excluded_words
            for word in words
        ):
            continue

        # Make sure every word looks like a name
        if all(
            re.match(
                r"^[A-Za-z][A-Za-z.'-]*$",
                word
            )
            for word in words
        ):

            return cleaned

    # ------------------------------------------------
    # Method 2: spaCy fallback
    # ------------------------------------------------

    doc = nlp(text[:5000])

    for entity in doc.ents:

        if entity.label_ == "PERSON":

            candidate = entity.text.strip()

            if candidate.lower() not in excluded_words:

                return candidate

    return None


def extract_personal_info(text: str):

    return {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "linkedin": extract_linkedin(text),

        "github": extract_github(text)
    }