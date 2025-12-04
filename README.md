# Bite-Sized-learning-app
A lightweight, interactive learning platform built with Streamlit that delivers short, easy-to-digest educational content. The app supports both Learners and Creators, and includes video reels, micro-lessons, analytics, and a clean UI designed for quick exploration.


Features


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
