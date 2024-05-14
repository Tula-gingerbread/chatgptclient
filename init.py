if __name__ == '__main__':
    import sys

    print('Its need to initialize main code. Not to bare use')
    sys.exit(1)

import json
import os
from openai import OpenAI
import collections

with open('settings.json', 'r', encoding='utf-8') as f:
    settings = json.load(f)

user = settings['username'] or os.getenv('USER')
modelname = settings['friendlyname'] or settings['model']
model = settings['model']
sysprompt = settings['sysprompt'].\
    replace('%USERNAME%', user).\
    replace('%GPTNAME%', settings['friendlyname'] or 'ChatGPT')

client = OpenAI(api_key=settings['token'] or None, base_url=settings['api_url'] or None)

# Not needed
del settings

context = collections.deque(list(), 10)
