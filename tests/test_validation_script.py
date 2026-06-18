import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_validation_script_passes():
    script = ROOT / "skills/themis/scripts/validate_themis_skill.py"
    result = subprocess.run([sys.executable, str(script)], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr
