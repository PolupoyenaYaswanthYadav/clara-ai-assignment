# Clara AI Assignment

## Overview
This project implements a simple pipeline that converts demo and onboarding call transcripts into structured AI agent configurations.

The pipeline first processes demo call transcripts to extract customer requirements and generate an initial agent configuration (v1).  
Then onboarding call transcripts are used to update the configuration (v2) and produce a changelog of the changes.

## Project Structure

dataset/  
- demo_calls/  
- onboarding_calls/

scripts/  
- extract_demo.py  
- generate_agent.py  
- update_onboarding.py  
- generate_changelog.py  
- run_pipeline.py  

outputs/  
- accounts/ (generated results)

workflows/  
- clara_pipeline.json (n8n workflow)

## Running the Pipeline

Run the pipeline from the project root:

python scripts/run_pipeline.py

This processes the transcripts in the dataset folder and generates outputs in:

outputs/accounts/

## Outputs

Each account contains:

- v1 → initial configuration generated from the demo call  
- v2 → updated configuration after onboarding  
- changes.md → summary of configuration updates
