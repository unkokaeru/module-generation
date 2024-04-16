"""prompts.py: A module for storing the GPT-3 prompts for generating content."""

# Class Generation
CLASS_PROMPT = "You're a program that returns a Python List of the questions in a given PDF text, giving each question by itself and formatting each question with LaTeX where appropriate (equations, numbers, general mathematical notation, etc.), using things like \\frac and \\mathbb, surrounding all LaTeX with $ for inline equations and $$ for block equations. Return nothing else other than the Python List - if you cannot find any questions, return None. Each element of the Python List should be an entire question with its respesctive sub-questions."
MISTAKE_PROMPT = "You're a program that takes a Python list of questions and fixes any mistakes in the formatting of the questions, such as improperly escaped characters (so escape them), incorrectly written LaTeX (so guess what it should be - as long as it works then it's okay), or unknown characters (replace them with known ones, or remove them). If parts of questions (e.g. 1a, 1b) are separate from their main part (e.g. 1), then combine them into one element. Return the fixed Python list of questions."

# Module Page Generation
NOTES_OUTLINE_PROMPT = """
You're a program that takes an outline of lecture content and converts it into a detailed markdown outline of notes with topics, sub-topics, and descriptions of each sub-topic; such as:
1. Functions

#### 1.1 Basic Concepts

- **[[Domain and Range]]**: Understanding the set of inputs (domain) and outputs (range) for functions.
- **[[Graphs of Functions]]**: Visual representation of functions on a coordinate plane.
- **[[Vertical Line Test]]**: A method to determine if a graph represents a function.

#### 1.2 Types of Functions

- **[[Polynomial Functions]]**: Functions like $y = x^n$.
- **[[Rational Functions]]**: Functions expressed as the ratio of two polynomials.
- **[[Trigonometric Functions]]**: Functions based on angles and ratios in a right triangle.
- **[[Exponential Functions]]**: Functions where the variable appears in the exponent.
- **[[Hyperbolic Functions]]**: Functions similar to trigonometric functions but based on hyperbolas.
- **[[Even and Odd Functions]]**: Symmetry properties of functions.
- **[[Piecewise-defined Functions]]**: Functions defined by different expressions over different intervals (e.g., absolute value, signum function).
- **[[Multivariable Functions]]**: Functions with multiple variable inputs.

etc.

The generated outline should be a logical order, ignoring the original order if required.
The topics should cover everything in the original outline (apart from things like revision and overviews), but the sub-topics and descriptions should be purely generated by you as they won't be provided, usually.
Ensure that the final result is in the exact same format as above.
"""

# Notes Generation
NOTE_PROMPT = "You're a program that takes a topic and generates a detailed markdown note aimed at undergraduate mathematicians, including all the information that would be required to understand the topic. This should include definitions, explanations, examples, and any other relevant information - seamlessly intertwine historical context and real-life examples. Finish with three exam questions to test the reader. Return the generated note in markdown format, using LaTeX when appropriate."

# Revision Generation
FLASHCARD_FORMAT = """
### Question

QUESTION

### Answer

ANSWER

---

"""
FLASHCARD_PROMPT = f"You're a program that takes a markdown note and generates a list of flashcards from it, each flashcard containing a question on one side and the answer on the other. Return the list of flashcards in the following format: {FLASHCARD_FORMAT}"

# Summary Generation
SUMMARY_NOTES_PROMPT = "You're a program that takes a list of questions and generates a detailed explanation of how to solve each TYPE of question (generalised, ignoring the specifics of the original questions, unless similar numbers show up often), including the steps, methods, and reasoning behind each step. Use a logical order and bullet points to quickly convey the information. Return the generated notes in markdown format, using LaTeX when appropriate (as in the questions given). Only return the bullet points and nothing else. If you cannot find any questions, return None."
