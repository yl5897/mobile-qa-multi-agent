"""
PlannerAgent

Responsibility:
- Take a natural language mobile QA test case
- Decompose it into a sequence of high-level actions
- Do NOT execute actions
- Do NOT judge pass/fail

The planner focuses on reasoning, not interaction.
"""
class PlannerAgent:
    def __init__(self):
        pass
    def generate_plan(self, test_case: str):
        """
        Convert a natural language QA test case into
        an ordered list of high-level actions.
        """
        print("\n[Planner] Received test case:")
        print(test_case)
        test_case_lower = test_case.lower()
        if "create" in test_case_lower and "vault" in test_case_lower:
            intent = "create_vault"
        elif "create" in test_case_lower and "note" in test_case_lower:
            intent = "create_note"
        elif "verify" in test_case_lower or "verify that" in test_case_lower:
            intent = "verify_ui_property"
        else:
            intent = "unknown"
        plan = []
        if intent == "create_vault":
            plan = [
                "Launch Obsidian app",
                "Navigate to vault creation screen",
                "Input vault name",
                "Confirm vault creation",
                "Enter newly created vault"
            ]

        elif intent == "create_note":
            plan = [
                "Open note creation menu",
                "Input note title",
                "Type note content",
                "Save note"
            ]

        elif intent == "verify_ui_property":
            plan = [
                "Navigate to settings screen",
                "Locate target UI element",
                "Check UI property against expectation"
            ]

        else:
            plan = [
                "Attempt to interpret test case",
                "Report inability to generate reliable plan"
            ]
        print("[Planner] Generated plan:")
        for idx, step in enumerate(plan, start=1):
            print(f"  {idx}. {step}")

        return plan

