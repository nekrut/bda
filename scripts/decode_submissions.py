#!/usr/bin/env python3
"""Decode and grade quiz submission codes from students."""

import base64
import json
import sys

# Correct answers for Test 1
CORRECT_ANSWERS = "BBBCBCBBBC" + "CCCBC"  # 15 answers: B,B,B,C,B,C,B,B,B,C,C,C,C,B,C

def decode_submission(code):
    """Decode a base64 submission code."""
    try:
        decoded = base64.b64decode(code)
        data = json.loads(decoded)
        return data
    except Exception as e:
        return None

def grade_submission(answers):
    """Grade answers against correct answers."""
    correct = 0
    results = []
    for i, (student, correct_ans) in enumerate(zip(answers, CORRECT_ANSWERS)):
        if student == correct_ans:
            correct += 1
            results.append(f"Q{i+1}: {student} ✓")
        elif student == '-':
            results.append(f"Q{i+1}: - (skipped)")
        else:
            results.append(f"Q{i+1}: {student} ✗ (correct: {correct_ans})")
    return correct, results

def main():
    print("=" * 60)
    print("BMMB554 Test 1 Submission Decoder")
    print("=" * 60)
    print("\nPaste submission codes below (one per line).")
    print("Enter a blank line when done.\n")

    submissions = []
    while True:
        line = input().strip()
        if not line:
            break
        submissions.append(line)

    if not submissions:
        print("No submissions to process.")
        return

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)

    for i, code in enumerate(submissions, 1):
        print(f"\n--- Submission {i} ---")
        data = decode_submission(code)

        if not data:
            print("ERROR: Invalid submission code")
            continue

        print(f"Student ID: {data.get('studentId', data.get('name', 'N/A'))}")
        print(f"Time: {data['time']}")
        print(f"Answers: {data['answers']}")

        score, details = grade_submission(data['answers'])
        print(f"Score: {score}/15 ({score/15*100:.1f}%)")
        print("\nDetails:")
        for detail in details:
            print(f"  {detail}")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
