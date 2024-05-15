#!/usr/bin/env python3
import sys
from init import client, sysprompt, model, context, markdown_print

try:
    while True:
        # read.remove_whitespace.replace_\\n_to_new_line
        prompt = input(f'>>> ').strip().replace(r'\\n', '\n')
        lprompt = prompt.lower()    # Lowercased Prompt

        if prompt == '': continue     # Ignore empty prompt

        # Remove all context
        if lprompt in ['cc //sys', 'clear context //system']:
            context.clear()
            print('Context cleared')
            continue
        # Multiline prompt
        if lprompt in ['ml //sys', 'multiline //system']:
            inputs = []
            while True:
                prompt_part = input('...>')
                if prompt_part.lower() in ['end //sys', 'end //system']:
                    break

                inputs.append(prompt_part)

            prompt = '\n'.join(inputs)

        # Generate context
        messages = [{'role': 'system', 'content': sysprompt}]
        messages.extend(list(context))
        messages.append({'role': 'user', 'content': prompt})

        # Generate response
        completion = client.chat.completions.create(model=model, messages=messages)
        markdown_print(completion.choices[0].message.content)
        print()    # Just add new line

        # Append new messages to context
        context.append({'role': 'user', 'content': prompt})
        context.append({'role': 'assistant', 'content': completion.choices[0].message.content})

        # print(f'\n---Debuginfo---:', completion, context, sep='\n')    # Print debug info
except KeyboardInterrupt:  # CTRL + C
    print('\nExit')
except EOFError:           # CTRL + D
    print('\nExit')
except Exception as ex:    # Other
    print(f'\nException: {ex}\nExit!')
    sys.exit(1)
