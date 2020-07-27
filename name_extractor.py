from __future__ import unicode_literals, print_function, division
import os
import re
import dill

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class NameExtractor():
    def __init__(self):
        with open(os.path.join(BASE_DIR, 'name_pattern.pkl'), 'rb') as f:
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
                        "entity": 'CONTACT_NAME',
                    }
                    # extracted.append(entity)
                    for i, v in enumerat(extracted):
                        if entity['start'] == v['start']:
                            ## 중복 제거
                            if entity['end'] == v['end']:
                                pass
                            else:
                                ##minimum 기준
                                if entity['end'] < v['end']:
                                    del extracted[i]
                                    extracted.append(entity)
                                else:
                                    pass
                except TypeError:
                    print(f"pattern: {pattern_} text: {text}")
        
        # extracted_filter = list({frozenset(item.items()) : item for item in extracted}.values())
        return extracted
