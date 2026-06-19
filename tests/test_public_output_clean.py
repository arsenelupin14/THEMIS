import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/themis/scripts/validate_public_output.py"

def test_valid_clean_final_passes():
    fixture = ROOT / "tests/fixtures/valid-clean-final.md"
    result = subprocess.run([sys.executable, str(SCRIPT), str(fixture)], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr

def test_invalid_internal_tags_fail():
    fixture = ROOT / "tests/fixtures/invalid-final-with-internal-tags.md"
    result = subprocess.run([sys.executable, str(SCRIPT), str(fixture)], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode != 0
