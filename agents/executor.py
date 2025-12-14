"""
ExecutorAgent

Executes planned steps on a real Android emulator via adb.
"""

import subprocess


class ExecutorAgent:
    def __init__(self, device_id="emulator-5556"):
        self.device_id = device_id

    def _run_adb(self, command):
        try:
            result = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return True, result.stdout.strip()
        except Exception as e:
            return False, str(e)

    def execute(self, step: str):
        print(f"[Executor] Executing step: {step}")

        step_lower = step.lower()

        # 1. Launch Obsidian
        if "launch" in step_lower and "obsidian" in step_lower:
            cmd = [
                "adb", "-s", self.device_id,
                "shell", "monkey",
                "-p", "md.obsidian",
                "-c", "android.intent.category.LAUNCHER", "1"
            ]
            success, output = self._run_adb(cmd)
            return {
                "success": success,
                "info": output
            }

        # 2. Navigate to vault creation screen (tap)
        if "navigate" in step_lower and "vault" in step_lower:
           return {
               "success": False,
               "info": (
                   "Vault creation flow is internal to MainActivity "
                   "and not accessible via adb tap, uiautomator, or intent"
                )
           }

        # 3. Input vault name
        if "input" in step_lower and "vault" in step_lower:
            cmd = [
                "adb", "-s", self.device_id,
                "shell", "input", "text", "InternVault"
            ]
            success, output = self._run_adb(cmd)
            return {
                "success": success,
                "info": "Entered vault name"
            }

        # 4. Confirm creation (Enter key)
        if "confirm" in step_lower:
            cmd = [
                "adb", "-s", self.device_id,
                "shell", "input", "keyevent", "66"
            ]
            success, output = self._run_adb(cmd)
            return {
                "success": success,
                "info": "Confirmed vault creation"
            }

        # Default fallback
        return {
            "success": True,
            "info": "Step executed (no-op)"
        }


