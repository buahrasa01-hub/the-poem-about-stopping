from pathlib import Path
import os

poem = (
    "The train takes the hill in its teeth.\n"
    "You lift my bag from gravel.\n"
    "I could climb in. Instead, I stay,\n"
    "holding your sleeve against wind\n"
    "while you find the torn ticket.\n"
    "Then you press it into my palm.\n"
    "The train is gone. Your hand is empty.\n"
    "Now you choose which way to walk."
)
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(poem, encoding="utf-8")
