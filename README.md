# 🧠 Think First — AI-Powered DSA Practice Tool

## Problem
Students increasingly reach for AI tools the moment they see a coding problem — often before attempting to think it through themselves. This instant-answer culture is quietly eroding independent problem-solving skills, which are exactly what technical interviews and real engineering work demand.

## Solution
**Think First** flips the usual AI-tutor model. Instead of answering on demand, it locks the explanation and hints until the student submits their own reasoning attempt. An AI evaluator checks whether the attempt shows genuine problem-solving effort — not a perfect answer, just real thinking. Lazy or copy-pasted attempts are rejected with a guiding question instead of a solution. Genuine attempts unlock a Socratic hint, followed by a chance to write code, and finally a full explanation compared against the student's own attempt.

## How It Works
1. **Pick a problem** from a curated set of 5 classic DSA problems (Two Sum, Reverse Linked List, Valid Parentheses, Binary Search, Fibonacci with Memoization)
2. **Write your reasoning** — your approach in plain words, before seeing any hints
3. **AI evaluates your reasoning** — genuine attempts unlock; lazy/gibberish attempts get rejected with a guiding question
4. **Write code** based on your unlocked understanding
5. **See the full explanation** — including AI feedback comparing your code attempt to the ideal approach

## AI Methods Used
- Google Gemini (`gemini-2.5-flash`) is used for two core tasks:
  - **Reasoning classification**: judges whether a student's written approach reflects genuine effort vs. a lazy/empty attempt, using a structured prompt with clear accept/reject criteria
  - **Adaptive feedback generation**: produces Socratic hints (not answers) for accepted attempts, and generates a personalized comparison between the student's final code and the ideal approach

## Tech Stack
- **Frontend & App**: Streamlit
- **AI**: Google Gemini API (`google-generativeai`)
- **Language**: Python

## Setup Instructions
1. Clone the repo, then create and activate a virtual environment
2. Install dependencies with `pip install -r requirements.txt`
3. Create a `.env` file with `GOOGLE_API_KEY=your_api_key_here`
4. Run with `streamlit run app.py`

## Live Demo
🔗 https://think-first-dsa-7pfbnmo84e6i7zzcdy8kfg.streamlit.app/

## Future Improvements
- Expand the problem bank across more DSA topics and difficulty levels
- Track user progress over time
- Support code execution to verify correctness, not just reasoning quality