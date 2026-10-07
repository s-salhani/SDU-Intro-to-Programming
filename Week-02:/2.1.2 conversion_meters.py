def convert_to_meters(length: float, unit: str) -> float:
"""converts length given in unit to meters"""

    if unit == "inch" or unit == "in":
        return (length * 0.0254)

    elif unit == "hand" or unit == "h":
        return (length * 0.1016)

    elif unit == "foot" or unit == "ft":
        return (length * 0.3048)

    elif unit == "yard" or unit == "yd":
        return (length * 0.9144)
    
