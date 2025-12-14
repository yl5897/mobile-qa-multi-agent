"""
Entry point for the Mobile QA Multi-Agent System.

This file defines:
- the system-level control loop
- how agents interact with each other
"""

from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.supervisor import SupervisorAgent


def run_single_test(test_case: str):
    """
    Run a single natural language QA test case
    through Planner -> Executor -> Supervisor.
    """
    print("\n==============================")
    print("New Test Case")
    print(f"Test description: {test_case}")

    # Initialize agents
    planner = PlannerAgent()
    executor = ExecutorAgent()
    supervisor = SupervisorAgent()

    # 1. Planning phase
    plan = planner.generate_plan(test_case)

    # 2. Execution phase
    execution_trace = []
    for step in plan:
        result = executor.execute(step)
        execution_trace.append(result)

    # 3. Supervision phase
    verdict = supervisor.evaluate(test_case, execution_trace)

    print("\nFinal Verdict:")
    print(verdict)


if __name__ == "__main__":
    # Temporary placeholder test
    sample_test = (
        "Open Obsidian, create a new Vault named 'InternVault', "
        "and enter the vault."
    )

    run_single_test(sample_test)


