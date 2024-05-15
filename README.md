# OpenAI-compatible client
init.py is all non-cycle actions (load config, make client object) -- you will not run it directly

main.py is program which use init.py and then asking you input, then requesting and printing ChatGPT answer

settings.json is settings  (wow! Oh my god!). Rename `settings.json.example` to `settings.json` and setup values
- `api_url`: base_url to API (if `null` - standard API URL)
- `token`: your API token
- `username`: how chatgpt will address you (if `null` - PC username)
- `friendlyname`: friendly ChatGPT's name (if `null` - ChatGPT's model)
- `model`: ChatGPT's model <br>
- `sysprompt`: ChatGPT's system prompt. `%GPTNAME%` - GPT's friendly name; `%USERNAME%` - User's name
