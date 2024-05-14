#!/usr/bin/env python3
import sys
from init import client, sysprompt, model, modelname, context

try:
    print(f'# --- Chat with {modelname} (Model: {model}) --- #')
    while True:
        message = input(f'>>> ').strip()

        messages = [
            {
                'role': 'system',
                'content': sysprompt
            }
        ]
        messages.extend(list(context))
        messages.append({'role': 'user', 'content': message})

        completion = client.chat.completions.create(model=model, messages=messages)

        print(f'Answer: \n{completion.choices[0].message.content}')
        context.append({'role': 'user', 'content': message})
        context.append({'role': 'assistant', 'content': completion.choices[0].message.content})

        # print(f'\n---Debuginfo---:', completion, context, sep='\n')
except KeyboardInterrupt:
    print('Exit')
except Exception as ex:
    print(f'Exception: {ex}\nExit!')
    print(f'Context:\n{context}')
    sys.exit(1)
