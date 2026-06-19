import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/themis/scripts/validate_claim_ledger.py"

def test_valid_claim_ledger_passes():
    fixture = ROOT / "tests/fixtures/valid-claim-ledger.md"
    result = subprocess.run([sys.executable, str(SCRIPT), str(fixture)], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr

def test_invalid_claim_ledger_fails():
    fixture = ROOT / "tests/fixtures/invalid-claim-ledger.md"
    result = subprocess.run([sys.executable, str(SCRIPT), str(fixture)], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode != 0
