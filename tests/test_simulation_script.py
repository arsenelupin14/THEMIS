import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_simulation_script_valid_output():
    fixture = ROOT / "tests/fixtures/valid-output.md"
    script = ROOT / "skills/themis/scripts/simulate_themis_output.py"
    result = subprocess.run([sys.executable, str(script), str(fixture)], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr
