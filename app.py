import streamlit as st

# Page settings
st.set_page_config(
    page_title="PyQuest - Python Quiz",
    page_icon="🐍",
    layout="centered"
)

# Quiz questions stored in a list of dictionaries
questions = [
    {
        "question": "Which of the following is a Python data type?",
        "options": ["Integer", "Number", "Character", "Decimal"],
        "answer": "Integer"
    },
    {
        "question": "Which statement is used to make a decision in Python?",
        "options": ["if", "repeat", "check", "choose"],
        "answer": "if"
    },
    {
        "question": "Which data structure stores multiple values in an ordered way?",
        "options": ["List", "Function", "Class", "Module"],
        "answer": "List"
    },
    {
        "question": "Which symbol is used to create a dictionary?",
        "options": ["[]", "()", "{}", "<>"],
        "answer": "{}"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which loop is commonly used to repeat through a list?",
        "options": ["for", "if", "switch", "select"],
        "answer": "for"
    },
    {
        "question": "Which block is used to handle errors in Python?",
        "options": ["try-except", "if-else", "for-while", "check-error"],
        "answer": "try-except"
    }
]

# Function to calculate the score
def calculate_score(answers):
    score = 0

    for index, answer in enumerate(answers):
        if answer == questions[index]["answer"]:
            score += 1

    return score


# Website title
st.title("🐍 PyQuest")
st.subheader("Python Quiz Challenge")

st.write(
    "Test your Python knowledge with this interactive quiz!"
)

# Store quiz state
if "started" not in st.session_state:
    st.session_state.started = False

if "submitted" not in st.session_state:
    st.session_state.submitted = False


# Start screen
if not st.session_state.started:

    name = st.text_input("👤 Enter your name")

    if st.button("🚀 Start Quiz"):

        if name.strip() == "":
            st.warning("Please enter your name before starting the quiz.")
        else:
            st.session_state.name = name
            st.session_state.started = True
            st.rerun()


# Quiz screen
else:

    st.success(f"Welcome, {st.session_state.name}! 🎉")

    answers = []

    for number, question in enumerate(questions, start=1):

        st.write(f"### Question {number}")
        st.write(question["question"])

        selected = st.radio(
            "Choose your answer:",
            question["options"],
            key=f"question_{number}"
        )

        answers.append(selected)

    st.write("---")

    if st.button("🏆 Submit Quiz"):

        try:
            score = calculate_score(answers)

            st.session_state.score = score
            st.session_state.submitted = True

        except Exception:
            st.error("Something went wrong. Please try again.")


# Result screen
if st.session_state.get("submitted", False):

    score = st.session_state.score
    total = len(questions)

    st.write("---")
    st.header("🎉 Quiz Completed!")

    st.write(
        f"**{st.session_state.name}**, your score is:"
    )

    st.metric("Your Score", f"{score} / {total}")

    if score == total:
        st.success("🌟 Perfect score! Excellent Python knowledge!")

    elif score >= 5:
        st.success("👏 Great job! You have a strong understanding of Python.")

    elif score >= 3:
        st.info("👍 Good attempt! Keep practising Python.")

    else:
        st.warning("📚 Keep learning and try the quiz again!")

    if st.button("🔄 Restart Quiz"):
        st.session_state.clear()
        st.rerun()


# Topics used in the project
with st.expander("📚 Python Topics Used"):
    st.write("""
    1. Variables and Data Types
    2. Lists
    3. Dictionaries
    4. If-Else Conditions
    5. For Loops
    6. Functions
    7. Exception Handling
    """)
