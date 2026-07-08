# Password-strength-Checker
A Python-based password strength analyzer that evaluates complexity, length, and character diversity using clean, fundamental logic.
# Password Strength Checker
Evolution Stages

Stage 1: Core Checks
Goal: Create isolated functions to test individual security rules.
Concepts: Functions, string methods, conditionals, boolean logic.
Checks: Minimum length (8+ characters), uppercase, lowercase, numbers, and special characters (!@#$%^&*). Each function returns True or False.

Stage 2: Scoring System
Goal: Combine individual checks into a unified numeric score and strength level.
Concepts: Lists, loops, accumulator pattern.
Features: Counts passing metrics, weights key rules (like length), and maps the result to labels like Weak or Very Strong.

Stage 3: Actionable Feedback
Goal: Explain why a password scored the way it did so the user can fix it.
Concepts: String formatting, lists, conditionals.
Features: Generates a dynamic list of missing requirements and prints a clear summary of suggestions.

Stage 4: Stretch Goals
Goal: Implement advanced security checks.
Concepts: File handling, sets/dictionaries.
Features: Cross-references input against a file of common passwords (e.g., "qwerty"), detects repeated or sequential characters, and estimates a theoretical "crack time".

Stage 5: Interactive Loop
Goal: Build a robust, continuous application.
Concepts: while loops, input(), exception handling.
Features: Runs continuously so users can test multiple passwords, handles empty inputs gracefully, and exits safely when the user types "quit" or "exit".

Future Roadmap
Upgrade to a desktop interface using tkinter.
Deploy as a web application using Flask.
