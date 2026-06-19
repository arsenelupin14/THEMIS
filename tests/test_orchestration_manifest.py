import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/themis/scripts/validate_orchestration_manifest.py"

def test_valid_manifest_passes():
    fixture = ROOT / "tests/fixtures/valid-orchestration-manifest.yml"
    result = subprocess.run([sys.executable, str(SCRIPT), str(fixture)], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr

def test_invalid_manifest_fails():
    fixture = ROOT / "tests/fixtures/invalid-orchestration-manifest.yml"
    result = subprocess.run([sys.executable, str(SCRIPT), str(fixture)], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode != 0
