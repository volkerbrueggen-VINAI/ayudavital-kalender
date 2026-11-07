"""Baut index.html aus template.html und data.json. Aufruf: python3 build.py"""
import json
d=json.load(open('data.json'))
open('index.html','w').write(open('template.html').read().replace('/*DATA*/',json.dumps(d,ensure_ascii=False)))
