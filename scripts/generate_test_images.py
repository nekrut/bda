#!/usr/bin/env python3
"""Generate PNG images for test questions to prevent copy-paste."""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "images" / "test1"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Questions data
questions = [
    # Python Questions
    {
        "num": 1,
        "section": "Python",
        "text": "What is the output of the following code?",
        "code": 'x = "ATCG"\nprint(x[1:3])',
        "options": ["A) AT", "B) TC", "C) TCG", "D) ATC"]
    },
    {
        "num": 2,
        "section": "Python",
        "text": "Which of the following correctly creates a dictionary in Python?",
        "code": None,
        "options": [
            'A) my_dict = ["name": "Alice", "age": 25]',
            'B) my_dict = {"name": "Alice", "age": 25}',
            'C) my_dict = ("name": "Alice", "age": 25)',
            'D) my_dict = <"name": "Alice", "age": 25>'
        ]
    },
    {
        "num": 3,
        "section": "Python",
        "text": "What does the following code print?",
        "code": "nums = [1, 2, 3, 4, 5]\nresult = [x * 2 for x in nums if x > 2]\nprint(result)",
        "options": ["A) [2, 4, 6, 8, 10]", "B) [6, 8, 10]", "C) [3, 4, 5]", "D) [1, 2]"]
    },
    {
        "num": 4,
        "section": "Python",
        "text": 'What is the result of len("Hello\\nWorld")?',
        "code": None,
        "options": ["A) 10", "B) 11", "C) 12", "D) 5"]
    },
    # Bash Questions
    {
        "num": 5,
        "section": "Bash",
        "text": "Which command displays your current working directory?",
        "code": None,
        "options": ["A) cd", "B) ls", "C) pwd", "D) dir"]
    },
    {
        "num": 6,
        "section": "Bash",
        "text": "What does ls -la do?",
        "code": None,
        "options": [
            "A) List only hidden files",
            "B) List all files including hidden ones in long format",
            "C) List files sorted by size",
            "D) List only directories"
        ]
    },
    {
        "num": 7,
        "section": "Bash",
        "text": "Which command would copy all .txt files from the current directory to a folder called backup?",
        "code": None,
        "options": [
            "A) mv *.txt backup/",
            "B) cp *.txt backup/",
            "C) copy *.txt backup/",
            "D) cat *.txt > backup/"
        ]
    },
    {
        "num": 8,
        "section": "Bash",
        "text": 'What does the command cat file1.txt | grep "error" | wc -l do?',
        "code": None,
        "options": [
            'A) Displays all lines containing "error" from file1.txt',
            'B) Counts the number of lines containing "error" in file1.txt',
            'C) Replaces "error" with line numbers in file1.txt',
            'D) Deletes lines containing "error" from file1.txt'
        ]
    },
    # Git Questions
    {
        "num": 9,
        "section": "Git",
        "text": "Which command stages all changed files for the next commit?",
        "code": None,
        "options": ["A) git commit -a", "B) git add .", "C) git push --all", "D) git stage *"]
    },
    {
        "num": 10,
        "section": "Git",
        "text": "What is the correct order of commands to save and upload your changes to GitHub?",
        "code": None,
        "options": [
            "A) git push → git commit → git add",
            "B) git commit → git add → git push",
            "C) git add → git commit → git push",
            "D) git add → git push → git commit"
        ]
    },
    {
        "num": 11,
        "section": "Git",
        "text": "Which command creates a new branch called feature and switches to it?",
        "code": None,
        "options": [
            "A) git branch feature",
            "B) git checkout feature",
            "C) git checkout -b feature",
            "D) git switch --new feature"
        ]
    },
    {
        "num": 12,
        "section": "Git",
        "text": "What does git status show?",
        "code": None,
        "options": [
            "A) The commit history",
            "B) The list of remote repositories",
            "C) Modified, staged, and untracked files",
            "D) The difference between two commits"
        ]
    },
    # Agentic CLI Questions
    {
        "num": 13,
        "section": "Agentic CLI",
        "text": 'What is an "agentic" CLI tool like Claude Code?',
        "code": None,
        "options": [
            "A) A tool that only executes pre-written scripts",
            "B) An AI assistant that can read files, run commands, and make code changes autonomously",
            "C) A graphical user interface for coding",
            "D) A compiler for multiple programming languages"
        ]
    },
    {
        "num": 14,
        "section": "Agentic CLI",
        "text": "Which is the BEST prompt when asking an agentic CLI to help with code?",
        "code": None,
        "options": [
            'A) "Fix it"',
            'B) "Make my code better"',
            'C) "Add input validation to the parse_fastq function that raises ValueError if the file doesn\'t start with @"',
            'D) "Do something with the function"'
        ]
    },
    {
        "num": 15,
        "section": "Agentic CLI",
        "text": "When using an agentic CLI tool, what should you do before accepting changes?",
        "code": None,
        "options": [
            "A) Always accept changes immediately without review",
            "B) Review the proposed changes to ensure they match your intent",
            "C) Delete all your original code first",
            "D) Disconnect from the internet"
        ]
    },
]


def create_question_image(q, output_path):
    """Create a PNG image for a single question."""

    # Calculate figure height based on content
    base_height = 2.0
    if q["code"]:
        base_height += 0.3 * (q["code"].count("\n") + 1)
    base_height += 0.4 * len(q["options"])

    fig, ax = plt.subplots(figsize=(10, base_height))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, base_height)
    ax.axis("off")

    y = base_height - 0.3

    # Question number and text
    question_text = f"{q['num']}. {q['text']}"
    ax.text(0.2, y, question_text, fontsize=12, fontweight="bold",
            wrap=True, verticalalignment="top",
            fontfamily="sans-serif")
    y -= 0.5

    # Code block if present
    if q["code"]:
        code_lines = q["code"].split("\n")
        code_height = 0.25 * len(code_lines) + 0.2

        # Draw code background
        rect = patches.FancyBboxPatch(
            (0.3, y - code_height), 9.4, code_height,
            boxstyle="round,pad=0.05",
            facecolor="#f5f5f5",
            edgecolor="#cccccc",
            linewidth=1
        )
        ax.add_patch(rect)

        # Draw code text
        for i, line in enumerate(code_lines):
            ax.text(0.5, y - 0.15 - i * 0.25, line, fontsize=11,
                   fontfamily="monospace", color="#333333",
                   verticalalignment="top")

        y -= code_height + 0.3

    # Options
    for option in q["options"]:
        ax.text(0.5, y, option, fontsize=11,
               fontfamily="sans-serif",
               verticalalignment="top")
        y -= 0.35

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight",
                facecolor="white", edgecolor="none")
    plt.close()


def main():
    print(f"Generating {len(questions)} question images...")

    for q in questions:
        output_path = OUTPUT_DIR / f"q{q['num']:02d}.png"
        create_question_image(q, output_path)
        print(f"  Created {output_path.name}")

    print("Done!")


if __name__ == "__main__":
    main()
