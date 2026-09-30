def parse_certifications(lines):

    certifications = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        certifications.append({
            "name": line
        })

    return certifications