# Weird-job-title entry courier. One line in, one line out, no surprises.

import json
import os
import pathlib

BOUND = 60  # titles longer than this never reach the blind judge

repo_dir = pathlib.Path(__file__).resolve().parent
line = (repo_dir / "entry.txt").read_text(encoding="utf-8").strip()

out_root = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
out_dir = pathlib.Path(out_root)
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(line, encoding="utf-8")

verdict = {
    "valid": 1 <= len(line) <= BOUND,
    "chars": len(line),
    "artifact": "entry.txt",
}
print(json.dumps(verdict))
