"""
SupervisorAgent

Responsibility:
- Evaluate the execution trace produced by ExecutorAgent
- Decide PASS / FAIL
- Distinguish between:
  - successful execution
  - UI not automatable / environment limitation
"""

from typing import List, Dict


class SupervisorAgent:
    def __init__(self):
        pass

    def evaluate(self, test_case: str, execution_trace: List[Dict]) -> Dict:
        """
        Evaluate a test case based on execution results.

        Args:
            test_case (str): Natural language test description
            execution_trace (List[Dict]): Results returned by ExecutorAgent

        Returns:
            Dict with keys:
                - status: PASS / FAIL
                - failure_type: None or string
                - reason: human-readable explanation
        """

        print("\n[Supervisor] Evaluating test case:")
        print(test_case)

        # 1. If any step failed, return FAIL immediately
        for step_result in execution_trace:
            if not step_result.get("success", True):
                print("[Supervisor] Test failed due to non-automatable UI")
                return {
                    "status": "FAIL",
                    "failure_type": "ui_not_automatable",
                    "reason": step_result.get(
                        "info",
                        "Step failed due to UI or environment limitation"
                    )
                }

        # 2. All steps succeeded
        print("[Supervisor] Test passed successfully")
        return {
            "status": "PASS",
            "failure_type": None,
            "reason": "All steps executed successfully"
        }

