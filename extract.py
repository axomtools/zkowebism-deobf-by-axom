import re


def getparts(code):
    if not code or not isinstance(code, str):
        return None
    pat = re.compile(
        r'local\s+(\w+)\s*=\s*\{([\d\s,\-]+)\}\s*;?[\s\S]{0,400}?string\.char\s*\(\s*\(\s*\1\s*\[\s*\w+\s*\]\s*-\s*(\d+)\s*\)\s*/\s*(\d+)\s*\)',
        re.DOTALL
    )
    found = list(pat.finditer(code))
    if not found:
        pat = re.compile(
            r'local\s+(\w+)\s*=\s*\{([\d\s,\-]+)\}\s*;?[\s\S]{0,400}?string\.char\s*\(\s*\(\s*\1\s*\[\s*\w+\s*\]\s*-\s*(\d+)\s*\)\s*/\s*(\d+)\s*\)',
            re.DOTALL | re.IGNORECASE
        )
        found = list(pat.finditer(code))
    if not found:
        return None
    out = []
    for item in found:
        raw = item.group(2)
        off = int(item.group(3))
        div = int(item.group(4))
        if div == 0:
            continue
        nums = [int(x) for x in re.findall(r'\d+', raw)]
        out.append((nums, off, div))
    if not out:
        return None
    return out
