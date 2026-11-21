from pathlib import Path
import os


POEM = """I stop the kettle before it screams,
then hold the match my friend would strike,
keep the door I meant to open shut.

Not retreat. A hand can also mean no:
I stay beside the ticking stove,
choosing the hour I refuse to enter."""

target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(POEM, encoding="utf-8")
