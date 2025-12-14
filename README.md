# Mobile QA Multi-Agent System

This repository contains a mobile QA automation system built for the **QualGent Research Intern Coding Challenge**.

The system executes natural-language QA test cases on a real Android emulator using a multi-agent architecture and adb-based actions.

---

## Architecture

The system is composed of three agents with clearly separated responsibilities:

### Planner
- Parses a natural-language QA test case
- Breaks it down into a sequence of high-level steps
- Does not interact with the Android device

### Executor
- Executes each step on an Android emulator
- Uses adb commands (launch app, tap, input text, key events)
- Returns structured results for each step
- Does not determine test success or failure

### Supervisor
- Evaluates the execution results produced by the Executor
- Determines whether the test passes or fails
- Distinguishes between execution failures and non-automatable UI flows

---

## Project Structure

mobile-qa-multi-agent/
├── agents/
│ ├── planner.py
│ ├── executor.py
│ ├── supervisor.py
│ └── prompts.py
├── tools/
│ ├── adb_tools.py
│ └── vision_tools.py
├── tests/
│ └── test_cases.yaml
├── main.py
├── report.md
├── requirements.txt
└── README.md

---

## Running the System

### Requirements
- macOS
- Android Studio
- Android Emulator (Pixel device, API ≥ 34)
- adb in PATH
- Python 3.9+

### Steps

1. Start an Android emulator
2. Install the Obsidian Android APK
3. Run:

```bash
python main.py
The system will generate a plan, execute each step on the emulator, and output a final test verdict.

Example Test Case
Open Obsidian, create a new Vault named "InternVault", and enter the vault.
Example Result
{
  "status": "FAIL",
  "failure_type": "ui_not_automatable",
  "reason": "Vault creation flow is internal to MainActivity and not accessible via adb or intent"
}
This result indicates that the test could not be completed due to application-level automation constraints.

Notes
The system interacts with a real Android emulator; no UI behavior is mocked.
If a test step cannot be automated due to application limitations, the system reports a failure with an explicit reason.
The goal is accurate QA evaluation rather than forcing UI automation.

Author: Yishan Liu
QualGent Research Intern Coding Challenge

