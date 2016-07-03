"""
Some functions for pygame rects.
"""

def resize(rect, before, now):
    "Equivalent of pygame.transform.scale for surfaces."
    # convert the position coords
    rect.left = int(rect.left / before * now)
    rect.top = int(rect.top / before * now)
    # convert the size
    rect.width = int(rect.width / before * now)
    rect.height = int(rect.height / before * now)
