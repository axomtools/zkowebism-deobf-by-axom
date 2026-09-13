from extract import getparts
from rebuild import toprintlines, toescaped, tochars


def decode(code):
    parts = getparts(code)
    if not parts:
        return None
    return toprintlines(parts)


def decodewithescape(code):
    parts = getparts(code)
    if not parts:
        return None
    lines = []
    for nums, off, div in parts:
        text = tochars(nums, off, div)
        if text is None:
            continue
        lines.append(toescaped(text))
    if not lines:
        return None
    return '\n'.join(lines)
