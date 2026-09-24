import streamlit as st

st.set_page_config(
    page_title="PyQuest - Python Quiz",
    page_icon="🐍",
    layout="centered"
)

questions = [
    {
        "question": "Which of the following is a Python data type?",
        "options": ["HTML", "CSS", "Integer", "Browser"],
        "answer": "Integer"
    },
    {
        "question": "Which statement is used to make a decision in Python?",
        "options": ["if", "for", "print", "input"],
        "answer": "if"
    },
    {
        "question": "Which data structure stores multiple values in an ordered way?",
        "options": ["Set", "Function", "Module", "List"],
        "answer": "List"
    },
    {
        "question": "Which symbol is used to create a dictionary?",
        "options": ["[]", "{}", "()", "<>"],
        "answer": "{}"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["function", "fun", "def", "define"],
        "answer": "def"
    },
    {
        "question": "Which loop is commonly used to repeat through a list?",
        "options": ["if", "for", "try", "def"],
        "answer": "for"
    },
    {
        "question": "Which block is used to handle errors in Python?",
        "options": ["if-else", "for-loop", "def", "try-except"],
        "answer": "try-except"
    }
]


def calculate_score():
    score = 0

    for i, question in enumerate(questions):
        selected = st.session_state.get(f"answer_{i}")

        if selected == question["answer"]:
            score += 1

    return score


if "started" not in st.session_state:
    st.session_state.started = False

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "name" not in st.session_state:
    st.session_state.name = ""

if "score" not in st.session_state:
    st.session_state.score = 0


# ---------------- START SCREEN ----------------

if not st.session_state.started:

    st.title("🐍 PyQuest")
    st.subheader("Python Quiz Challenge")

    st.write(
        "Test your Python knowledge with this interactive quiz!"
    )

    name = st.text_input("Enter your name:")

    if st.button("🚀 Start Quiz"):

        if name.strip() == "":
            st.warning("Please enter your name first.")

        else:
            st.session_state.name = name.strip()
            st.session_state.started = True
            st.session_state.submitted = False

            st.rerun()


# ---------------- QUIZ SCREEN ----------------

elif not st.session_state.submitted:

    st.title("🐍 PyQuest")

    st.subheader(
        f"Good luck, {st.session_state.name}! 🎯"
    )

    st.write("Choose one answer for each question.")

    with st.form("quiz_form"):

        for i, question in enumerate(questions):

            st.radio(
                question["question"],
                ["-- Select an answer --"] + question["options"],
                key=f"answer_{i}"
            )

            st.write("")

        submitted = st.form_submit_button(
            "✅ Submit Quiz"
        )

    if submitted:

        st.session_state.score = calculate_score()
        st.session_state.submitted = True

        st.rerun()


# ---------------- RESULT SCREEN ----------------

else:

    st.title("🎉 Quiz Completed!")

    score = st.session_state.score
    total = len(questions)

    st.write(
        f"Well done, {st.session_state.name}!"
    )

    st.subheader(
        f"Your Score: {score}/{total}"
    )

    if score == total:

        st.success(
            "Excellent! You answered everything correctly! 🏆"
        )

    elif score >= 5:

        st.success(
            "Great job! You have a good knowledge of Python! 👏"
        )

    elif score >= 3:

        st.info(
            "Good attempt! Keep practising Python. 📚"
        )

    else:

        st.warning(
            "Keep learning and try again! 💪"
        )

    if st.button("🔄 Restart Quiz"):

        st.session_state.started = False
        st.session_state.submitted = False
        st.session_state.name = ""
        st.session_state.score = 0

        for i in range(len(questions)):
            st.session_state.pop(f"answer_{i}", None)

        st.rerun()


# ---------------- TOPICS ----------------

with st.expander("📚 Python Topics Used"):

    st.write("""
    • Variables and data types
    • Input and output
    • Conditional statements
    • Lists
    • Dictionaries
    • Functions
    • Loops
    • Exception handling
    """)
