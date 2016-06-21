"""
Some functions for pygame rects.
"""

def multiply(rect):
    "Equivalent of pygame.transform.scale for surfaces."
    # convert the position coords
    rect.left *= 2
    rect.top *= 2
    # convert the size
    rect.width *= 2
    rect.height *= 2
