# Mobile QA Multi-Agent System

This project is a prototype mobile QA system built for the QualGent Research Intern Coding Challenge.
It takes a natural-language QA test case, breaks it into executable steps, runs those steps on a real Android emulator using adb, and then determines whether the test should pass or fail.
The focus of this project is correct QA evaluation and reasoning, rather than forcing UI automation where it is not feasible.
---

## Architecture

The system is composed of three agents with clearly separated responsibilities.

### Planner

- Parses a natural-language QA test case
- Breaks the test case into a sequence of high-level steps
- Does not interact with the Android device

### Executor

- Executes each planned step on a real Android emulator
- Uses adb commands (launch app, tap, input text, key events)
- Returns structured execution results for each step
- Does not determine test success or failure

### Supervisor

- Evaluates the execution results produced by the Executor
- Determines whether the test passes or fails
- Explicitly identifies cases where a test cannot be automated due to application or platform limitations
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
- adb available in PATH
- Python 3.9+

### Steps

1. Start an Android emulator
2. Install the Obsidian Android APK on the emulator
3. Run the system:

```bash
python main.py
```
The system will generate a plan, execute each step on the emulator using adb, and evaluate the final result.
The system interacts with a real Android emulator. No UI behavior is mocked or simulated.

4. Example Test Case
Open Obsidian, create a new Vault named "InternVault", and enter the vault.

5. Example Result
In this case, the test correctly fails because the vault creation flow in Obsidian is not accessible through adb-based automation.
```bash
{
  "status": "FAIL",
  "failure_type": "ui_not_automatable",
  "reason": "Vault creation flow is internal to MainActivity and not accessible via adb tap, uiautomator, or intent"
}
```
This result indicates that the test could not be completed due to application-level limitations rather than an execution failure.

## Notes
The system interacts with a real Android emulator; no UI behavior is mocked.
If a test step cannot be automated due to application constraints, the system reports this explicitly instead of forcing unreliable actions.
The objective is accurate QA evaluation and reasoning, not UI hacking or brittle automation.

Author: Yishan Liu

QualGent Research Intern Coding Challenge
