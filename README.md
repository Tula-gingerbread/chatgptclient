# OpenAI-compatible client

`init.py` - Executes all actions not related to cycles (loading configuration, creating a client object). You don't need to run it directly.

`main.py` - this is the program that uses `init.py`, then requests data input, sends a request, and displays the GPT response.

To input new line type `\n` (if you not need new line type `\\n`).
Also, you can type `ml //sys` (`multiline //system`), 
then your message with multiple lines and `end //sys` (`end //system`) to end input. 
Also, whitespace in the message will not be removed.

Enter `cc //sys` (`clear context //system`) to clear context.


`settings.json` - settings (well, yes, surprising!). Rename `settings.json.example` to `settings.json` and configure the values:
- `api_url`: the base API URL (if `null` - the standard API URL is used).
- `token`: your API token.
- `username`: how GPT will address you (if `null` - the PC username is used).
- `friendlyname`: GPT's friendly name (if `null` - the GPT model).
- `model`: the GPT model.
- `sysprompt`: the GPT system prompt. `%GPTNAME%` - GPT's friendly name; `%USERNAME%` - the username.

The code has been tested only on Linux/GNU, but probably will work on all systems.
