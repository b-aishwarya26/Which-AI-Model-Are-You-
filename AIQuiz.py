import streamlit as st

st.title("Which AI Model Are You? 🤖")
st.write("Answer the following 15 questions to find out which AI model best matches your personality!")

# Scores for AI models
chatgpt_score, gemini_score, claude_score, llama_score = 0, 0, 0, 0

# Question 1
q1 = st.radio(
    "When learning something new, what’s your approach?",
    ["Watch a demo and experiment (Hands-on Learning)",
     "Read articles and research in depth",
     "Discuss ideas with others and brainstorm",
     "Analyze multiple sources for different perspectives"],
    index=None
)
if q1 == "Watch a demo and experiment (Hands-on Learning)":
    chatgpt_score += 1
elif q1 == "Read articles and research in depth":
    llama_score += 1
elif q1 == "Discuss ideas with others and brainstorm":
    claude_score += 1
elif q1 == "Analyze multiple sources for different perspectives":
    gemini_score += 1

# Question 2
q2 = st.radio(
    "What kind of responses do you prefer when asking a question?",
    ["Detailed and structured, like an article",
     "Fast and creative, even if it's not perfect",
     "Ethical and well-thought-out",
     "Scientific and research-backed"],
    index=None
)
if q2 == "Detailed and structured, like an article":
    gemini_score += 1
elif q2 == "Fast and creative, even if it's not perfect":
    chatgpt_score += 1
elif q2 == "Ethical and well-thought-out":
    claude_score += 1
elif q2 == "Scientific and research-backed":
    llama_score += 1

# Question 3
q3 = st.radio(
    "Which best describes your thinking style?",
    ["Innovative and fast-thinking",
     "Logical and data-driven",
     "Ethical and philosophical",
     "Deep and technical"],
    index=None
)
if q3 == "Innovative and fast-thinking":
    chatgpt_score += 1
elif q3 == "Logical and data-driven":
    gemini_score += 1
elif q3 == "Ethical and philosophical":
    claude_score += 1
elif q3 == "Deep and technical":
    llama_score += 1

# Question 4
q4 = st.radio(
    "If you had an AI assistant, what would you use it for?",
    ["Creative brainstorming and content generation",
     "Analyzing reports and making data-driven decisions",
     "Making ethical and fair decisions",
     "Developing AI research and models"],
    index=None
)
if q4 == "Creative brainstorming and content generation":
    chatgpt_score += 1
elif q4 == "Analyzing reports and making data-driven decisions":
    gemini_score += 1
elif q4 == "Making ethical and fair decisions":
    claude_score += 1
elif q4 == "Developing AI research and models":
    llama_score += 1

# Question 5
q5 = st.radio(
    "What excites you the most?",
    ["Telling stories and imagining new worlds",
     "Finding patterns in large data sets",
     "Making the world a better place",
     "Solving complex technical problems"],
    index=None
)
if q5 == "Telling stories and imagining new worlds":
    chatgpt_score += 1
elif q5 == "Finding patterns in large data sets":
    gemini_score += 1
elif q5 == "Making the world a better place":
    claude_score += 1
elif q5 == "Solving complex technical problems":
    llama_score += 1

# Question 6
q6 = st.radio(
    "How do you solve problems?",
    ["Think outside the box and try creative solutions",
     "Analyze data and trends before making a decision",
     "Consider the ethical implications first",
     "Break down the problem into technical components"],
    index=None
)
if q6 == "Think outside the box and try creative solutions":
    chatgpt_score += 1
elif q6 == "Analyze data and trends before making a decision":
    gemini_score += 1
elif q6 == "Consider the ethical implications first":
    claude_score += 1
elif q6 == "Break down the problem into technical components":
    llama_score += 1

# Question 7-15 (Similar structure as above)
questions = [
    ("What’s your preferred way to communicate?",
     ["Casual and fun", "Clear and concise", "Thoughtful and respectful", "Precise and technical"]),
    
    ("What’s your ideal work environment?",
     ["Collaborative and fun", "Data-driven and structured", "Ethical and mission-driven", "Independent and research-oriented"]),
    
    ("What motivates you the most?",
     ["Creativity and self-expression", "Facts and knowledge", "Justice and fairness", "Technical challenges"]),
    
    ("How do you handle debates?",
     ["Come up with quick and fun arguments", "Support claims with data", "Consider both sides fairly", "Break arguments down logically"]),
    
    ("What do you think AI should focus on?",
     ["Making life more entertaining", "Helping people analyze data", "Ensuring responsible AI usage", "Advancing research"]),
    
    ("If you could have a superpower, what would it be?",
     ["Inspiring creativity in others", "Knowing everything instantly", "Bringing peace and fairness", "Solving impossible technical problems"]),
    
    ("How do you handle mistakes?",
     ["Laugh them off and try again", "Analyze the cause and improve", "Think about the ethical consequences", "Debug and fix them"]),
    
    ("Which AI-related field interests you the most?",
     ["Chatbots and NLP", "Data science and analytics", "AI ethics and fairness", "Deep learning and neural networks"]),
    
    ("What do you value the most?",
     ["Creativity", "Knowledge", "Ethics", "Technical expertise"])
]

# Assigning scores based on answers
for i, (question, options) in enumerate(questions):
    answer = st.radio(question, options, index=None, key=f"q{i+7}")
    if answer == options[0]:
        chatgpt_score += 1
    elif answer == options[1]:
        gemini_score += 1
    elif answer == options[2]:
        claude_score += 1
    elif answer == options[3]:
        llama_score += 1

# Calculate the result
if st.button("Find Out Your AI Match!"):
    max_score = max(chatgpt_score, gemini_score, claude_score, llama_score)

    if chatgpt_score == max_score:
        st.subheader("You are **ChatGPT**! 🎨💬")
        st.write("You're creative, conversational, and love brainstorming new ideas. You excel at making discussions fun and engaging!")
    elif gemini_score == max_score:
        st.subheader("You are **Gemini**! 📊📚")
        st.write("You're analytical, informative, and great at processing large amounts of data. You love learning and providing detailed insights.")
    elif claude_score == max_score:
        st.subheader("You are **Claude**! 🌱🧠")
        st.write("You're thoughtful, ethical, and always consider the moral implications of AI. You value responsible and fair decision-making.")
    elif llama_score == max_score:
        st.subheader("You are **LLaMA**! 🔬📖")
        st.write("You're research-focused, deep-thinking, and love diving into technical topics. You enjoy working with scientific advancements.")

    st.write("No matter which AI you are, you're unique and intelligent in your own way! 🚀")
