# 28 December 2023
# Wildcard string matching

import re

class Solution:
    def match(self, wildcard, text_to_match):
        # Convert the wildcard pattern to a regular expression pattern
        regex_pattern = '^' + wildcard.replace('?', '.').replace('*', '.*') + '$'

        # Use re.fullmatch to check if the entire text matches the regular expression pattern
        return True if re.fullmatch(regex_pattern, text_to_match) else False
