import re

def extract_title(markdown):
    matches = re.findall(r'^#\s(.+)', markdown, flags=re.MULTILINE)
    
    if matches:
        return matches[0].strip()
    else:
        raise Exception("No H1 header found in the markdown")