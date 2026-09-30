import re


def parse_education(lines):

    education = []

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        if not line:
            i += 1
            continue

        # =========================================
        # HSC / SSC
        # =========================================

        school_match = re.match(
            r"^(H\.?S\.?C\.?|S\.?S\.?C\.?)\s*[–\-:]\s*(.+)$",
            line,
            re.IGNORECASE
        )

        if school_match:

            education.append({
                "degree": school_match.group(1).upper(),
                "institution": school_match.group(2).strip(),
                "location": None,
                "cgpa": None
            })

            i += 1
            continue

        # =========================================
        # College degree
        # =========================================

        degree_match = re.search(
            r"\b(B\.?E\.?|B\.?Tech|M\.?E\.?|M\.?Tech|"
            r"B\.?Sc|M\.?Sc|BCA|MCA|MBA)\b",
            line,
            re.IGNORECASE
        )

        if degree_match:

            current = {
                "degree": line,
                "institution": None,
                "location": None,
                "cgpa": None
            }

            # -------------------------------------
            # Look at next lines
            # -------------------------------------

            j = i + 1

            while j < len(lines):

                next_line = lines[j].strip()

                if not next_line:
                    j += 1
                    continue

                # Stop if another degree starts
                next_degree = re.search(
                    r"\b(B\.?E\.?|B\.?Tech|M\.?E\.?|M\.?Tech|"
                    r"B\.?Sc|M\.?Sc|BCA|MCA|MBA|"
                    r"H\.?S\.?C\.?|S\.?S\.?C\.?)\b",
                    next_line,
                    re.IGNORECASE
                )

                if next_degree:
                    break

                # CGPA
                cgpa_match = re.search(
                    r"(?:CGPA|GPA)\s*[:\-]?\s*(\d+(?:\.\d+)?)",
                    next_line,
                    re.IGNORECASE
                )

                if cgpa_match:

                    current["cgpa"] = cgpa_match.group(1)

                    j += 1
                    continue

                # Institution
                if current["institution"] is None:

                    current["institution"] = next_line

                    location_match = re.search(
                        r",\s*([A-Za-z ]+)$",
                        next_line
                    )

                    if location_match:

                        current["location"] = (
                            location_match.group(1).strip()
                        )

                    j += 1
                    continue

                break

            education.append(current)

            i = j
            continue

        i += 1

    return education