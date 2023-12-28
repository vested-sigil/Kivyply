# OID.py
import os
import inspect
from pathlib import Path
from typing import Dict, Any, Optional, List

class OperationInvestigationDiscovery:
    def __init__(self, dir: Optional[Path] = Path('.')):
        self.dir = dir
        self.chart = None

    def __call__(self):
        self.chart = self.discovery()
        self.submit_plan(self.chart)

    def investigate(self, name: str) -> Dict[str, Dict[str, List[str]]]:
        try:
            mod = __import__(name)
            info = {}
            for name, obj in inspect.getmembers(mod):
                if inspect.isclass(obj) or inspect.isfunction(obj) or inspect.ismethod(obj):
                    members = [m[0] for m in inspect.getmembers(obj)] if inspect.isclass(obj) else []
                    info[name] = {
                        "doc": obj.__doc__ or "No doc",
                        "members": members
                    }
            return info
        except Exception as e:
            print(f"Error investigating {name}: {e}")
            return {}

    def discovery(self) -> Dict[str, Dict[str, Dict[str, List[str]]]]:
        chart = {}
        for f in self.dir.glob('*.py'):
            name = f.stem
            chart[name] = self.investigate(name)
        return chart

    def submit_plan(self, chart: Dict[str, Dict[str, Dict[str, List[str]]]]):
        # Logic to review the chart and submit a plan
        # Example: print("Submitting plan based on chart analysis")
        pass

# Usage example
if __name__ == "__main__":
    oid = OperationInvestigationDiscovery(Path('path_to_modules'))
    oid()  # Execute the OID
