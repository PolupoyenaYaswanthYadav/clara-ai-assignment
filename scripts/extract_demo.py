import json
import os

DATASET_FOLDER = "dataset/demo_calls"
OUTPUT_FOLDER = "outputs/accounts"

def extract_info(text):

    memo = {
        "account_id": "",
        "company_name": "",
        "business_hours": {
            "days": [],
            "start": "",
            "end": "",
            "timezone": ""
        },
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": "",
        "non_emergency_routing_rules": "",
        "call_transfer_rules": "",
        "integration_constraints": "",
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }

    # simple keyword extraction
    if "sprinkler" in text.lower():
        memo["services_supported"].append("sprinkler service")

    if "fire alarm" in text.lower():
        memo["services_supported"].append("fire alarm service")

    if "emergency" in text.lower():
        memo["emergency_definition"].append("customer reported emergency")

    return memo


def process_file(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    memo = extract_info(text)

    account_id = os.path.basename(file_path).split(".")[0]
    memo["account_id"] = account_id

    account_folder = f"{OUTPUT_FOLDER}/{account_id}/v1"
    os.makedirs(account_folder, exist_ok=True)

    with open(f"{account_folder}/memo.json", "w") as f:
        json.dump(memo, f, indent=2)

    print(f"Processed {account_id}")


def run_pipeline():

    for file in os.listdir(DATASET_FOLDER):

        path = os.path.join(DATASET_FOLDER, file)

        if file.endswith(".txt"):
            process_file(path)


if __name__ == "__main__":
    run_pipeline()