import streamlit as st

def one_piece_expert_system(problem):
    rules = [
        {"problem": "Luffy is in trouble", "solution": "Summon the crew and prepare for an adventure!"},
        {"problem": "Zoro lost his way", "solution": "Look for three directions and wait for Zoro to find his way back."},
        {"problem": "Nami needs help", "solution": "Assist Nami with navigation or any weather-related issues."},
        {"problem": "Sanji is cooking", "solution": "Wait eagerly for Sanji's delicious meal."},
    ]

    for rule in rules:
        if problem == rule['problem']:
            return rule['solution']

    return "No solution found."

st.title("One Piece Expert System")

problem = st.selectbox("Select your problem", ["Luffy is in trouble", "Zoro lost his way", "Nami needs help", "Sanji is cooking"])

solution = one_piece_expert_system(problem)

st.subheader("Solution:")
st.write(solution)
