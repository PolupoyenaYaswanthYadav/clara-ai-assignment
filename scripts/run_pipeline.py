import subprocess

scripts = [
    "scripts/extract_demo.py",
    "scripts/generate_agent.py",
    "scripts/update_onboarding.py",
    "scripts/generate_changelog.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script], check=True)

print("Pipeline completed successfully.")