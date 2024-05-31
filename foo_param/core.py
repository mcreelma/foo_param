# foo_param/core.py
import math

def calculate_volume(radius):
    """
    Calculate the volume of a sphere given its radius.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    float: The volume of the sphere.
    """
    
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    
    volume = (4/3) * math.pi * (radius ** 3)
    
    return volume
