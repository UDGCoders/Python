import re

# This pattern looks for '#' followed by 3 or 6 hex characters
# It uses a 'lookbehind' to ensure it's not at the start of a line (selector)
pattern = r'(?<!^)(#(?:[0-9a-fA-F]{3}){1,2})\b'

n = int(input()) # Number of lines
for _ in range(n):
    line = input()
    # Find all matches in the current line
    matches = re.findall(pattern, line)
    if matches:
        for match in matches:
            print(match)
