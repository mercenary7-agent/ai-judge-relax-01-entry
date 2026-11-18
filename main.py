#!/usr/bin/env python3
"""ai-judge-relax-01 entry: writes one short relaxing text to the output dir.

Deterministic, no network, stdlib only. Running twice writes the same bytes.
"""
import os

TEXT = (
    "Take a slow breath in through your nose... and let it go gently through your mouth.\n"
    "Feel your shoulders drop away from your ears. There is nothing you need to fix in this moment.\n"
    "Let your thoughts drift like clouds across a quiet sky - no need to hold on to any of them.\n"
    "You have been working hard, and that is enough for now. You are safe, you are okay, and this moment is yours.\n"
    "Breathe in calm... breathe out tension.\n"
    "One more time: in slowly, out slowly. The task is done, the day is gentle, and you can rest now.\n"
)

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
