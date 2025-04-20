from typing import Literal

def sort(width: float, height: float, length: float, mass: float) -> Literal["STANDARD", "SPECIAL", "REJECTED"]:
    """
    Sorts a package into a stack based on its dimensions and mass.

    Note:
        bulky: A package is considered bulky if its volume is greater than or equal to 1,000,000 cm³ or any of its dimensions (width, height, length) is greater than or equal to 150 cm.
        heavy: A package is considered heavy if its mass is greater than or equal to 20 kg.

    Args:
        width (float): The width of the package in cm.
        height (float): The height of the package in cm.
        length (float): The length of the package in cm.
        mass (float): The mass of the package in kg.

    Returns:
        str: The name of the stack for this package ("STANDARD", "SPECIAL", or "REJECTED").
    """
    # Defensive programming: validate input types
    if not all(isinstance(arg, (int, float)) for arg in (width, height, length, mass)):
        raise TypeError("All arguments must be of type int or float.")

    # Handle invalid input values
    if any(dim <= 0 for dim in (width, height, length)) or mass <= 0:
        raise ValueError("All dimensions and mass must be positive values.")

    volume = width * height * length
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in (width, height, length))
    is_heavy = mass >= 20

    return "REJECTED" if is_bulky and is_heavy else "SPECIAL" if is_bulky or is_heavy else "STANDARD"
