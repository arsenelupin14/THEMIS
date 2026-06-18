from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_skill_md_exists():
    assert (ROOT / "skills/themis/SKILL.md").exists()

def test_skill_frontmatter():
    text = (ROOT / "skills/themis/SKILL.md").read_text()
    assert text.startswith("---")
    assert "name: themis" in text
    assert "description:" in text

def test_required_references_exist():
    refs = [
        "protocol.md",
        "role-generation.md",
        "challenge-loop.md",
        "memory-compression.md",
        "anti-sycophancy.md",
        "simulation.md",
        "install-notes.md",
    ]
    for ref in refs:
        assert (ROOT / "skills/themis/references" / ref).exists()
