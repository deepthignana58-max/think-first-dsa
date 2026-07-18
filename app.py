import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from problems import PROBLEMS

# --- Setup ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Think First", page_icon="🧠")
st.title("🧠 Think First")
st.caption("Practice DSA the way that actually builds skill — try before you see the answer.")

# --- Session state setup ---
if "stage" not in st.session_state:
    st.session_state.stage = "reasoning"  # reasoning -> unlocked -> code -> final
if "problem_index" not in st.session_state:
    st.session_state.problem_index = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

problem = PROBLEMS[st.session_state.problem_index]

# --- Problem selector ---
titles = [p["title"] for p in PROBLEMS]
selected_title = st.selectbox("Choose a problem:", titles, index=st.session_state.problem_index)
new_index = titles.index(selected_title)
if new_index != st.session_state.problem_index:
    st.session_state.problem_index = new_index
    st.session_state.stage = "reasoning"
    st.session_state.feedback = ""
    st.rerun()

st.subheader(f"{problem['title']}  ·  {problem['topic']}")
st.write(problem["statement"])
st.code(problem["example"])

st.divider()

# --- STAGE 1: Reasoning input (locked) ---
if st.session_state.stage == "reasoning":
    st.write("### 🔒 Solution is locked")
    st.write("Before we show any hints or solution, explain **your approach** in your own words. What would you try, and why?")
    reasoning = st.text_area("Your reasoning:", height=120, key="reasoning_input")

    if st.button("Check my reasoning"):
        if not reasoning or len(reasoning.strip()) < 10:
            st.warning("Please write a real attempt — a few words won't count.")
        else:
            with st.spinner("Checking your reasoning..."):
                prompt = f"""You are a strict but fair DSA tutor evaluating a student's reasoning attempt.

Problem: {problem['statement']}
Correct ideal approach: {problem['ideal_approach']}

Student's reasoning attempt: "{reasoning}"

Judge whether this shows GENUINE problem-solving effort — meaning the student is actually thinking about the problem, even if their approach is wrong, incomplete, or not optimal.
REJECT only if the attempt is: gibberish, a copy-pasted answer with no explanation, extremely lazy ("idk", "just tell me", one word), or completely unrelated to the problem.

Respond in this EXACT format:
VERDICT: GENUINE or REJECT
FEEDBACK: <2-3 sentences. If GENUINE, briefly acknowledge what's right/missing and give one Socratic hint to nudge them further, without revealing the full answer. If REJECT, explain what's missing and ask a guiding question to get them started, without revealing the answer.>
"""
                response = model.generate_content(prompt)
                result = response.text

                if "VERDICT: GENUINE" in result:
                    feedback = result.split("FEEDBACK:")[1].strip() if "FEEDBACK:" in result else result
                    st.session_state.feedback = feedback
                    st.session_state.stage = "unlocked"
                    st.rerun()
                else:
                    feedback = result.split("FEEDBACK:")[1].strip() if "FEEDBACK:" in result else result
                    st.error("Not quite — try again with more of your own thinking.")
                    st.info(feedback)

# --- STAGE 2: Unlocked - show hint + let them proceed ---
elif st.session_state.stage == "unlocked":
    st.write("### 🔓 Unlocked!")
    st.success(st.session_state.feedback)
    st.write("Now try writing actual code for your approach (pseudocode is fine too).")
    code_attempt = st.text_area("Your code / pseudocode attempt:", height=150, key="code_input")

    if st.button("Show full explanation"):
        st.session_state.stage = "final"
        st.session_state.code_attempt = code_attempt
        st.rerun()

# --- STAGE 3: Final explanation ---
elif st.session_state.stage == "final":
    st.write("### ✅ Full Explanation")
    st.write(f"**Ideal approach:** {problem['ideal_approach']}")

    if st.session_state.get("code_attempt"):
        with st.spinner("Comparing your code to the ideal approach..."):
            prompt = f"""A student attempted this DSA problem: {problem['statement']}
Ideal approach: {problem['ideal_approach']}
Student's code/pseudocode attempt: {st.session_state.code_attempt}

In 3-4 sentences, kindly explain how close their attempt is to the ideal approach, what they got right, and what they could improve. Be encouraging but honest."""
            response = model.generate_content(prompt)
            st.info(response.text)

    if st.button("Try another problem"):
        st.session_state.stage = "reasoning"
        st.session_state.feedback = ""
        st.rerun()