def calculate_percentage(part, total):
    """
    Safely calculate percentage.
    """
    if total == 0:
        return 0

    return round((part / total) * 100, 2)


def get_missing_severity(percentage):
    """
    Classify missing value severity.
    """
    if percentage < 5:
        return "Low"

    elif percentage < 20:
        return "Medium"

    return "High"


def get_outlier_severity(percentage):
    """
    Classify outlier severity.
    """
    if percentage == 0:
        return "Low"

    elif percentage < 5:
        return "Moderate"

    return "High"


def get_correlation_strength(correlation):
    """
    Classify correlation strength.
    """
    value = abs(correlation)

    if value < 0.30:
        return "Weak"

    elif value < 0.70:
        return "Moderate"

    return "Strong"