import json
import os

OUTPUT_FOLDER = "outputs/accounts"

def generate_changelog(account):

    v1_path = f"{OUTPUT_FOLDER}/{account}/v1/memo.json"
    v2_path = f"{OUTPUT_FOLDER}/{account}/v2/memo.json"

    if not os.path.exists(v2_path):
        return

    with open(v1_path) as f:
        v1 = json.load(f)

    with open(v2_path) as f:
        v2 = json.load(f)

    changes = []

    for key in v2:
        if v1.get(key) != v2.get(key):
            changes.append(f"{key} updated")

    with open(f"{OUTPUT_FOLDER}/{account}/changes.md","w") as f:
        for change in changes:
            f.write(change + "\n")


for account in os.listdir(OUTPUT_FOLDER):

    generate_changelog(account)