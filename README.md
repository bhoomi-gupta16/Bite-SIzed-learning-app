# Bite-Sized-learning-app
A lightweight, interactive learning platform built with Streamlit that delivers short, easy-to-digest educational content. The app supports both Learners and Creators, and includes video reels, micro-lessons, analytics, and a clean UI designed for quick exploration.


Features
![WhatsApp Image 2025-12-04 at 17 16 06_4703f68a](https://github.com/user-attachments/assets/e4d34f43-6f36-4415-9256-410a563a9b2a)


🔹 1. Dual-Mode Navigation (Learner / Creator)

Sidebar switch to toggle between Learner and Creator spaces.

Dynamic page loading based on selected role.

Clean, minimal sidebar UI with:

Title: "Bite-Sized Learning"

Role selector (radio)

Page selector (selectbox)

Footer caption: "Mock data • Demo interface • Streamlit ❤️"

🔹 2. Reels Section (Micro-learning Videos)

Supports embedding YouTube reels or short clips using streamlit_player (optional).

Fallback logic if streamlit_player isn’t installed.

Each reel contains:

ID

Title

Description

Video URL

Tags / Categories

🔹 3. Interactive Learning Pages

Each page in LEARNER_PAGES and CREATOR_PAGES maps to a function rendering UI content.

Modular design makes adding new pages simple.

Examples:

Concept Explorer

Mini-Quizzes

Creator Dashboard

Content Upload Tool

🔹 4. Visualizations

Supports:

Altair charts

Plotly Express visualizations

Used for:

Learning analytics

Course progress tracking

Content insights
<img width="1494" height="628" alt="Screenshot 2025-12-04 173111" src="https://github.com/user-attachments/assets/e8713980-288f-4f79-9250-b1f4961c71f7" />
<img width="1431" height="313" alt="Screenshot 2025-12-04 173017" src="https://github.com/user-attachments/assets/0c2c770c-38a3-4c1a-85d8-f449693ae58d" />


🔹 5. Responsive Wide Layout

Configured using:

st.set_page_config(
    page_title="Bite-Sized Learning Hub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


This ensures:

Flexible wide-screen experience

Quick access navigation

Mobile-friendly rendering

🔹 6. Mock Data & Demo Mode

The app intentionally uses mock dataset items for:

Reels

Charts

Progress indicators

Creator uploads

Useful for testing and UI prototyping

Why Bite-Sized Learning?

Helps learners consume small, meaningful chunks of knowledge.

Designed for fast scrolling and interactive learning.

Suitable for study platforms, course creators, or micro-learning communities.
<img width="1786" height="821" alt="Screenshot 2025-12-04 173232" src="https://github.com/user-attachments/assets/d33bc64c-a801-467b-ac03-a52c9296111e" />

