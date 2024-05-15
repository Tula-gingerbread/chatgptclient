if __name__ == '__main__':
    import sys

    print('Its need to initialize main code. Not to bare use')
    sys.exit(1)

import json
import os
from openai import OpenAI
import collections
from rich.console import Console
from rich.markdown import Markdown

with open('settings.json', 'r', encoding='utf-8') as f:
    settings = json.load(f)

user = settings['username'] or os.getenv('USER') or os.getenv('USERNAME')
modelname = settings['friendlyname'] or settings['model']
model = settings['model']
sysprompt = settings['sysprompt'].\
    replace('%USERNAME%', user).\
    replace('%GPTNAME%', settings['friendlyname'] or 'ChatGPT')

client = OpenAI(api_key=settings['token'] or None, base_url=settings['api_url'] or None)

# Not needed
del settings
context = collections.deque(list(), 10)

console = Console()

def markdown_print(text: str) -> None:
    console.print(Markdown(text, hyperlinks=False))   # Hyperlinks doesn't work in *K*onsole (KDE terminal), enable it if you want

# Here we go
print(f'# --- Chat with {modelname} (Model: {model}) --- #')
