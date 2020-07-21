from __future__ import unicode_literals, print_function, division
import os
import re
import dill

class NameExtractor():
    def __init__(self):
        with open('./name_pattern.pkl', 'rb') as f:
            self.NAME_PATTERN = dill.load(f)
        
    def process(self, text):
        extracted = []
        for pattern in self.NAME_PATTERN:
            matches = re.findall(pattern=pattern, string=text)
            for pattern_ in matches:
                try:
                    match = re.search(pattern=pattern_, string=text)
                    s, e = match.span()
                    entity = {
                        "start": s,
                        "end": e,
                        "value": match.group(),
                        "confidence": 1.0,
                        "entity": 'UserName',
                    }
                    extracted.append(entity)
                except TypeError:
                    print(f"pattern: {pattern_} text: {text}")
        return extracted
