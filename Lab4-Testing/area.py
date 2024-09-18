"""
Function for computing areas of various shapes
"""

def triangle_area(height, base):
    if height < 0 or base < 0:
        raise ValueError('Base and height must be 0 or positive')   # use "raise" instead of "return" to raise an error
    else:
        return height * base * 0.5

