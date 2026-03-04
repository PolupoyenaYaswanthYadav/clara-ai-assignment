import json
import os

ONBOARDING_FOLDER = "dataset/onboarding_calls"
OUTPUT_FOLDER = "outputs/accounts"

def extract_updates(text):

    updates = {}

    if "24/7" in text.lower():
        updates["business_hours"] = {
            "days": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
            "start": "00:00",
            "end": "23:59",
            "timezone": "unknown"
        }

    if "dispatch" in text.lower():
        updates["emergency_routing_rules"] = "transfer to dispatch"

    if "service trade" in text.lower():
        updates["integration_constraints"] = "never create sprinkler jobs in ServiceTrade"

    return updates


def apply_update(account_id, updates):

    v1_path = f"{OUTPUT_FOLDER}/{account_id}/v1/memo.json"

    if not os.path.exists(v1_path):
        print(f"Account {account_id} not found")
        return

    with open(v1_path) as f:
        memo = json.load(f)

    for key,value in updates.items():
        memo[key] = value

    v2_folder = f"{OUTPUT_FOLDER}/{account_id}/v2"
    os.makedirs(v2_folder, exist_ok=True)

    with open(f"{v2_folder}/memo.json","w") as f:
        json.dump(memo,f,indent=2)

    print(f"Updated account {account_id} to v2")


def run_pipeline():

    for file in os.listdir(ONBOARDING_FOLDER):

        if file.endswith(".txt"):

            account_id = file.split(".")[0]

            with open(os.path.join(ONBOARDING_FOLDER,file)) as f:
                text = f.read()

            updates = extract_updates(text)

            apply_update(account_id, updates)


if __name__ == "__main__":
    run_pipeline()