"""
AI Response Parser

Converts AI markdown responses into structured sections.
"""

import re


class AIResponseParser:

    # Expected headings from the prompt
    SECTIONS = [
        "Dataset Overview",
        "Data Quality Assessment",
        "Key Observations",
        "Business Insights",
        "Potential Risks",
        "Recommendations",
    ]

    @staticmethod
    def parse(response: str) -> dict:
        """
        Parse markdown response into dictionary.

        Parameters
        ----------
        response : str
            Raw LLM response.

        Returns
        -------
        dict
            {
                "Dataset Overview": "...",
                ...
            }
        """

        parsed = {}

        current_section = None
        buffer = []

        lines = response.splitlines()

        for line in lines:

            line = line.strip()

            if not line:
                continue

            # Remove markdown ##
            clean_line = re.sub(r"^#+\s*", "", line)

            if clean_line in AIResponseParser.SECTIONS:

                if current_section:

                    parsed[current_section] = "\n".join(buffer).strip()

                current_section = clean_line

                buffer = []

            else:

                if current_section:

                    buffer.append(line)

        # Save last section
        if current_section:

            parsed[current_section] = "\n".join(buffer).strip()

        # Ensure every section exists
        for section in AIResponseParser.SECTIONS:

            parsed.setdefault(section, "No information available.")

        return parsed