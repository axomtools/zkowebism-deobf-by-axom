import re


def iszkowebism(code):
    if not code or not isinstance(code, str):
        return False
    if re.search(r'local\s+\w+\s*=\s*\{[\d\s,]+\}\s*;?[\s\S]{0,400}?string\.char\s*\(\s*\(\s*\w+\s*\[\s*\w+\s*\]\s*-\s*\d+\s*\)\s*/\s*\d+\s*\)', code, re.DOTALL):
        return True
    return False
