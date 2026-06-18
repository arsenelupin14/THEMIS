from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_examples_exist():
    examples = [
        "software-app.md",
        "oss-security-tool.md",
        "community-product.md",
        "weird-role-request.md",
    ]
    for name in examples:
        assert (ROOT / "examples" / name).exists()

def test_examples_include_themes():
    combined = "\n".join(p.read_text() for p in (ROOT / "examples").glob("*.md"))
    assert "THEMIS_STATE_V1" in combined
    assert "CHALLENGE" in combined.upper() or "NO_BLOCKING_CONFLICT" in combined
