import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/themis/scripts/validate_retrieval_contract.py"

def test_retrieval_contract_passes():
    result = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr
