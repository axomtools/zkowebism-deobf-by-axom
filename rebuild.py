def tochars(nums, off, div):
    if div == 0:
        return None
    try:
        return ''.join(chr(int((n - off) / div)) for n in nums)
    except Exception:
        return None


def toescaped(text):
    if text is None:
        return None
    out = text.replace('\\', '\\\\')
    out = out.replace('"', '\\"')
    out = out.replace('\n', '\\n')
    out = out.replace('\r', '\\r')
    out = out.replace('\t', '\\t')
    return out


def toprintlines(parts):
    if not parts:
        return None
    lines = []
    for nums, off, div in parts:
        text = tochars(nums, off, div)
        if text is None:
            continue
        esc = toescaped(text)
        lines.append('print("' + esc + '")')
    if not lines:
        return None
    return '\n'.join(lines)


def torawtext(parts):
    if not parts:
        return None
    chunks = []
    for nums, off, div in parts:
        text = tochars(nums, off, div)
        if text is None:
            continue
        chunks.append(text)
    if not chunks:
        return None
    return ''.join(chunks)
