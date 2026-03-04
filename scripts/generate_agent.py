import json
import os

OUTPUT_FOLDER = "outputs/accounts"

def generate_agent(account):

    memo_path = f"{OUTPUT_FOLDER}/{account}/v1/memo.json"

    with open(memo_path) as f:
        memo = json.load(f)

    agent = {
        "agent_name": memo["account_id"] + "_agent",
        "version": "v1",
        "voice_style": "professional",
        "system_prompt": "You are Clara, an AI call assistant.",
        "services": memo["services_supported"]
    }

    with open(f"{OUTPUT_FOLDER}/{account}/v1/agent_spec.json","w") as f:
        json.dump(agent,f,indent=2)

for account in os.listdir(OUTPUT_FOLDER):

    generate_agent(account)