from __future__ import unicode_literals, print_function, division
import os
import re
import dill

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXCEPTION_LIST = ['번호', '폰', '기기', '사람', '연락처', '사용자', '이용자', '회선']

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
                    if entity['value'] not in EXCEPTION_LIST:
                        if len(extracted) == 0:
                            extracted.append(entity)
                        else:
                            dup_count = 0
                            for i, v in enumerate(extracted):
                                if entity['start'] == v['start']:
                                    dup_count += 1
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
                            if dup_count ==0:
                                extracted.append(entity)
                except TypeError:
                    print(f"pattern: {pattern_} text: {text}")
        
        extracted = sorted(extracted, key=lambda k: k['start']) 
        return extracted
