import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

try:
    from streamlit_player import st_player
except ModuleNotFoundError:
    st_player = None


st.set_page_config(
    page_title="Bite-Sized Learning Hub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


REELS = [
    {
        "id": "r1",
        "title": "Quick Algebra Trick",
        "creator": "Maya Chen",
        "topic": "Mathematics",
        "difficulty": "Beginner",
        "duration": "0:45",
        "video_url": "https://www.youtube.com/watch?v=BJXAx9P9C5Y",
        "likes": 1240,
        "saves": 410,
    },
    {
        "id": "r2",
        "title": "DNA in 90 Seconds",
        "creator": "Dr. Amir",
        "topic": "Biology",
        "difficulty": "Intermediate",
        "duration": "1:30",
        "video_url": "https://www.youtube.com/watch?v=6R4KY0Kq5ew",
        "likes": 980,
        "saves": 360,
    },
    {
        "id": "r3",
        "title": "Design Thinking Crash",
        "creator": "UX Lab",
        "topic": "Design",
        "difficulty": "Beginner",
        "duration": "0:55",
        "video_url": "https://www.youtube.com/watch?v=Q80Xvk_wscI",
        "likes": 1750,
        "saves": 680,
    },
    {
        "id": "r4",
        "title": "Python List Tricks",
        "creator": "CodePulse",
        "topic": "Programming",
        "difficulty": "Intermediate",
        "duration": "1:15",
        "video_url": "https://www.youtube.com/watch?v=A79Qh9wh6m8",
        "likes": 2120,
        "saves": 950,
    },
]

PLAYLISTS = [
    {
        "name": "AI Fundamentals",
        "description": "Bite-sized explainers on GenAI, ML, and prompt craft.",
        "reels": ["r2", "r3", "r4"],
        "progress": 0.65,
        "tags": ["AI", "Prompting"],
    },
    {
        "name": "Math Refresh",
        "description": "Daily algebra and calculus boosts.",
        "reels": ["r1", "r4"],
        "progress": 0.32,
        "tags": ["Math", "STEM"],
    },
    {
        "name": "UX in Minutes",
        "description": "Micro-lessons on user empathy and prototyping.",
        "reels": ["r3"],
        "progress": 0.9,
        "tags": ["Design", "Product"],
    },
]

MICRO_COURSES = [
    {
        "id": "c1",
        "title": "Micro-Course: GenAI Launchpad",
        "level": "Intermediate",
        "duration": "35 min",
        "description": "Understand prompts, evals, and responsible AI with snackable videos.",
        "modules": [
            {"title": "Prompt Patterns", "duration": "8 min"},
            {"title": "Evaluation Basics", "duration": "12 min"},
            {"title": "Responsible AI Lens", "duration": "15 min"},
        ],
        "completion": 0.45,
    },
    {
        "id": "c2",
        "title": "Creative Coding Toolkit",
        "level": "Beginner",
        "duration": "28 min",
        "description": "Build playful games with Python in under an hour.",
        "modules": [
            {"title": "Why Creative Code", "duration": "4 min"},
            {"title": "Mini Game Loop", "duration": "9 min"},
            {"title": "Visual polish", "duration": "15 min"},
        ],
        "completion": 0.7,
    },
]

LEARNER_PROFILE = {
    "name": "Alex Rivers",
    "avatar": "https://avatars.githubusercontent.com/u/9919?s=200&v=4",
    "streak": 12,
    "xp": 4820,
    "badges": ["Prompt Pro", "Consistency Champ", "STEM Sprinter"],
    "saved_reels": ["r1", "r4"],
    "learning_goals": [
        "Practice Python for 15 min/day",
        "Complete GenAI micro-course",
        "Save 5 new STEM reels weekly",
    ],
}

CREATOR_STATS = {
    "name": "Dr. Lina Woods",
    "avatar": "https://images.unsplash.com/photo-1544723795-3fb6469f5b39",
    "followers": 18400,
    "reels_published": 68,
    "micro_courses": 5,
    "watch_time": 182_000,
    "recent_reels": [
        {"title": "Explain CRISPR", "views": 8200, "likes": 640},
        {"title": "Quantum in 90s", "views": 10200, "likes": 720},
        {"title": "Ethical AI Cheat", "views": 5600, "likes": 480},
    ],
}


def init_state():
    if "liked_reels" not in st.session_state:
        st.session_state.liked_reels = set()

    if "saved_reels" not in st.session_state:
        st.session_state.saved_reels = set(LEARNER_PROFILE["saved_reels"])

    if "created_courses" not in st.session_state:
        st.session_state.created_courses = []

    if "uploaded_reels" not in st.session_state:
        st.session_state.uploaded_reels = []


def get_reel(reel_id: str):
    return next((reel for reel in REELS if reel["id"] == reel_id), None)


def stat_card(label: str, value, help_text: str = ""):
    with st.container(border=True):
        st.caption(label.upper())
        st.subheader(value)
        if help_text:
            st.write(help_text)


def render_reel_card(reel: dict, can_interact=True):
    cols = st.columns([2, 1])
    with cols[0]:
        if st_player is not None:
            st_player(reel["video_url"], height=260)
        else:
            st.video(reel["video_url"])
    with cols[1]:
        st.markdown(f"### {reel['title']}")
        st.write(f"{reel['creator']} • {reel['topic']} • {reel['difficulty']}")
        st.write(f"Duration: {reel['duration']}")
        st.write(f"👍 {reel['likes']} | 💾 {reel['saves']}")
        if can_interact:
            liked = reel["id"] in st.session_state.liked_reels
            saved = reel["id"] in st.session_state.saved_reels
            like_button = st.button(
                "❤️ Liked" if liked else "🤍 Like",
                key=f"like_{reel['id']}",
                type="primary" if liked else "secondary",
            )
            save_button = st.button(
                "✅ Saved" if saved else "💾 Save",
                key=f"save_{reel['id']}",
            )
            if like_button:
                if liked:
                    st.session_state.liked_reels.remove(reel["id"])
                else:
                    st.session_state.liked_reels.add(reel["id"])
            if save_button:
                if saved:
                    st.session_state.saved_reels.remove(reel["id"])
                else:
                    st.session_state.saved_reels.add(reel["id"])


def learner_home_feed():
    st.title("🎬 Home Feed")
    st.caption("Scroll through fresh bite-sized lessons tuned to your interests.")
    for reel in REELS:
        render_reel_card(reel)
        st.divider()


def learner_reel_viewer():
    st.title("👀 Reel Viewer")
    default = REELS[0]["id"]
    selected_id = st.selectbox(
        "Choose a reel",
        options=[r["id"] for r in REELS],
        format_func=lambda rid: get_reel(rid)["title"],
        index=0,
    )
    reel = get_reel(selected_id) or get_reel(default)
    if reel:
        st.video(reel["video_url"])
        st.markdown(f"### {reel['title']}")
        st.write(f"By **{reel['creator']}** • Topic: {reel['topic']} • {reel['difficulty']}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("❤️ Like", key=f"viewer_like_{reel['id']}"):
                st.session_state.liked_reels.add(reel["id"])
        with col2:
            if st.button("💾 Save", key=f"viewer_save_{reel['id']}"):
                st.session_state.saved_reels.add(reel["id"])
        st.success("Comments & transcripts coming soon 📜")


def learner_playlists():
    st.title("🗂️ Learning Playlists")
    for playlist in PLAYLISTS:
        with st.container(border=True):
            st.markdown(f"### {playlist['name']}")
            st.write(playlist["description"])
            st.progress(playlist["progress"])
            st.write("Tags:", ", ".join(playlist["tags"]))
            st.caption(
                "Includes: "
                + ", ".join(get_reel(rid)["title"] for rid in playlist["reels"])
            )


def learner_micro_course_details():
    st.title("📚 Micro-Course Details")
    options = [course["title"] for course in MICRO_COURSES]
    selected = st.selectbox("Select a micro-course", options=options)
    course = next(course for course in MICRO_COURSES if course["title"] == selected)
    col1, col2, col3 = st.columns(3)
    col1.metric("Level", course["level"])
    col2.metric("Total Duration", course["duration"])
    col3.metric("Completion", f"{int(course['completion']*100)}%")
    st.progress(course["completion"])
    st.write(course["description"])
    st.subheader("Modules")
    for module in course["modules"]:
        with st.expander(module["title"], expanded=False):
            st.write(f"Duration: {module['duration']}")
            st.info("Placeholder video player coming soon.")


def learner_progress_dashboard():
    st.title("📈 Progress Tracking Dashboard")
    weekly = pd.DataFrame(
        {
            "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "minutes_watch": [12, 18, 25, 30, 22, 15, 10],
            "reels_completed": [2, 3, 4, 5, 4, 3, 1],
        }
    )
    col1, col2, col3 = st.columns(3)
    stat_card("Weekly Watch Time", "2h 12m", "+18% vs last week")
    stat_card("Reels Completed", "22", "Streak day 12 🔥")
    stat_card("Micro-Courses", "2 active", "Finish GenAI by Sunday")
    st.subheader("Weekly watch trend")
    line_chart = (
        alt.Chart(weekly)
        .mark_line(point=True)
        .encode(
            x="day",
            y="minutes_watch",
            tooltip=["day", "minutes_watch", "reels_completed"],
            color=alt.value("#7563DF"),
        )
    )
    st.altair_chart(line_chart, use_container_width=True)
    st.subheader("Goal Tracker")
    for goal in LEARNER_PROFILE["learning_goals"]:
        st.checkbox(goal, value=False)


def learner_profile():
    st.title("👤 Learner Profile")
    st.markdown(f"### {LEARNER_PROFILE['name']}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Learning Streak", f"{LEARNER_PROFILE['streak']} days")
    col2.metric("XP", LEARNER_PROFILE["xp"])
    col3.metric("Badges", len(LEARNER_PROFILE["badges"]))
    st.subheader("Badges")
    st.write(", ".join(LEARNER_PROFILE["badges"]))
    st.subheader("Saved Reels")
    saved = [get_reel(rid) for rid in st.session_state.saved_reels]
    for reel in saved:
        st.write(f"- {reel['title']} ({reel['topic']})")
    st.subheader("Learning Goals")
    for goal in LEARNER_PROFILE["learning_goals"]:
        st.write("•", goal)


def creator_dashboard():
    st.title("🛠️ Creator Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Followers", f"{CREATOR_STATS['followers']:,}")
    col2.metric("Reels Published", CREATOR_STATS["reels_published"])
    col3.metric("Micro-Courses", CREATOR_STATS["micro_courses"])
    col4.metric("Watch Time", f"{CREATOR_STATS['watch_time']:,} min")
    st.subheader("Recent Reels")
    df = pd.DataFrame(CREATOR_STATS["recent_reels"])
    st.dataframe(df, hide_index=True, use_container_width=True)
    st.subheader("Topic Performance")
    topic_df = pd.DataFrame(
        {
            "topic": ["AI", "Biology", "STEM Skills", "Ethics"],
            "views": [12000, 8200, 7600, 5400],
        }
    )
    bar = alt.Chart(topic_df).mark_bar(color="#49A078").encode(x="topic", y="views")
    st.altair_chart(bar, use_container_width=True)


def creator_upload_reel():
    st.title("⬆️ Upload Reel")
    st.caption("30–90s vertical nugget. Keep it crisp, actionable, and aligned to a topic.")
    with st.form("upload_reel"):
        title = st.text_input("Title")
        topic = st.selectbox("Topic", ["AI", "Math", "Design", "Biology", "Other"])
        duration = st.slider("Duration (seconds)", min_value=30, max_value=90, value=60)
        difficulty = st.select_slider(
            "Difficulty", options=["Beginner", "Intermediate", "Advanced"], value="Beginner"
        )
        tags = st.text_input("Tags (comma separated)")
        video_url = st.text_input("Video URL (YouTube / CDN)")
        submitted = st.form_submit_button("Submit Reel")
        if submitted:
            st.session_state.uploaded_reels.append(
                {
                    "title": title or "Untitled Reel",
                    "topic": topic,
                    "duration": duration,
                    "difficulty": difficulty,
                    "tags": tags,
                    "video_url": video_url,
                }
            )
            st.success("Reel submitted! We'll review & publish within 24h.")
    if st.session_state.uploaded_reels:
        st.subheader("Recently Submitted Reels")
        st.table(pd.DataFrame(st.session_state.uploaded_reels))


def creator_create_micro_course():
    st.title("📘 Create Micro-Course")
    with st.form("create_course"):
        title = st.text_input("Course Title")
        level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])
        summary = st.text_area("Quick summary")
        videos = st.multiselect(
            "Attach existing reels",
            options=[reel["title"] for reel in REELS],
        )
        new_video_title = st.text_input("Add new module title")
        new_video_desc = st.text_area("Module notes / takeaway")
        submitted = st.form_submit_button("Save Micro-Course")
        if submitted:
            course = {
                "title": title or "Untitled Course",
                "level": level,
                "summary": summary,
                "videos": videos,
                "new_module": new_video_title,
                "notes": new_video_desc,
            }
            st.session_state.created_courses.append(course)
            st.success("Micro-course drafted! Ready for QA & publish.")
    if st.session_state.created_courses:
        st.subheader("Draft Courses")
        st.json(st.session_state.created_courses)


def creator_analytics():
    st.title("📊 Creator Analytics")
    analytics_df = pd.DataFrame(
        {
            "reel": [reel["title"] for reel in CREATOR_STATS["recent_reels"]],
            "views": [reel["views"] for reel in CREATOR_STATS["recent_reels"]],
            "likes": [reel["likes"] for reel in CREATOR_STATS["recent_reels"]],
            "watch_time": [round(reel["views"] * 0.6, 2) for reel in CREATOR_STATS["recent_reels"]],
        }
    )
    st.dataframe(analytics_df, hide_index=True, use_container_width=True)
    st.subheader("Views vs Likes")
    scatter = px.scatter(
        analytics_df,
        x="views",
        y="likes",
        size="watch_time",
        hover_name="reel",
        color="likes",
        color_continuous_scale="viridis",
    )
    st.plotly_chart(scatter, use_container_width=True)
    st.subheader("Views Breakdown")
    pie = px.pie(analytics_df, values="views", names="reel")
    st.plotly_chart(pie, use_container_width=True)


LEARNER_PAGES = {
    "Home Feed": learner_home_feed,
    "Reel Viewer": learner_reel_viewer,
    "Learning Playlists": learner_playlists,
    "Micro-Course Details": learner_micro_course_details,
    "Progress Tracking Dashboard": learner_progress_dashboard,
    "User Profile": learner_profile,
}

CREATOR_PAGES = {
    "Creator Dashboard": creator_dashboard,
    "Upload Reel": creator_upload_reel,
    "Create Micro-Course": creator_create_micro_course,
    "Analytics": creator_analytics,
}


def sidebar_navigation():
    st.sidebar.title("Bite-Sized Learning")
    role = st.sidebar.radio("Choose your space", ("Learner", "Creator"))
    pages = LEARNER_PAGES if role == "Learner" else CREATOR_PAGES
    page_name = st.sidebar.selectbox("Navigate", list(pages.keys()))
    st.sidebar.divider()
    st.sidebar.caption("Mock data • Demo interface • Streamlit ❤️")
    pages[page_name]()


def main():
    init_state()
    sidebar_navigation()


if __name__ == "__main__":
    main()

