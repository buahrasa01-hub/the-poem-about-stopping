from pathlib import Path
import os


POEM = """I stop the kettle before it screams,
slide the match back beneath its darkness,
close the door my friend had begun to open.

A hand can also mean no. I stay
beside the ticking stove, guarding
the hour I have chosen not to enter."""

target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(POEM, encoding="utf-8")
