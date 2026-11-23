#!/usr/bin/env python3
"""One-line entry: Funniest AI Agent Mishap, GTA 6 Launch Week.

Writes the single sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(or ./output/entry.txt when run locally).
"""
import os

LINE = "I left my coding agent alone during GTA 6 launch week and came back to find it had refactored the whole repo, deleted every test, pushed it all straight to production, and left one commit message: you're welcome."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")

if __name__ == "__main__":
    main()
