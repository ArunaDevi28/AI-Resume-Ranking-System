import streamlit as st
import pandas as pd
import plotly.express as px
import random
import io

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="SkillGraph AI",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0f172a;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #020617;
}

h1, h2, h3, h4 {
    color: white;
}

.stButton>button {
    background: linear-gradient(90deg,#7c3aed,#2563eb);
    color: white;
    border-radius: 12px;
    height: 50px;
    border: none;
    font-size: 18px;
    font-weight: bold;
}

.stTextArea textarea {
    background-color: #1e293b;
    color: white;
    border-radius: 12px;
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
}

.metric-card {
    background: linear-gradient(135deg,#1e293b,#0f172a);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🚀 SkillGraph AI")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Analytics",
        "AI Insights",
        "Leaderboard"
    ]
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🚀 AI Resume Ranking System")

st.markdown("""
### Intelligent Candidate Ranking Platform

Upload resumes + job description and get: 
""")

# ---------------------------------------------------
# JOB DESCRIPTION
# ---------------------------------------------------

job_description = st.text_area(
    "📄 Enter Job Description",
    height=200,
    placeholder="""
Looking for AI/ML Engineer with:
- Python
- Machine Learning
- NLP
- Deep Learning
- SQL
- Streamlit
- Transformers
"""
)

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_files = st.file_uploader(
    "📂 Upload Candidate Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------

if st.button("🔍 Analyze Candidates"):

    if not job_description:
        st.warning("Please enter job description.")
        st.stop()

    if not uploaded_files:
        st.warning("Please upload resumes.")
        st.stop()

    # ---------------------------------------------------
    # AI DEMO DATA
    # ---------------------------------------------------

    candidates = []

    for file in uploaded_files:

        ats = random.randint(70, 99)
        match = random.randint(65, 98)

        recommendation = (
            "Highly Recommended"
            if match >= 85
            else "Recommended"
        )

        candidates.append({
            "Candidate": file.name,
            "ATS Score": ats,
            "Match Score": match,
            "Recommendation": recommendation
        })

    # ---------------------------------------------------
    # DATAFRAME
    # ---------------------------------------------------

    df = pd.DataFrame(candidates)

    df = df.sort_values(
        by="Match Score",
        ascending=False
    ).reset_index(drop=True)

    df["Rank"] = df.index + 1

    df = df[
        [
            "Rank",
            "Candidate",
            "ATS Score",
            "Match Score",
            "Recommendation"
        ]
    ]

    # ---------------------------------------------------
    # DASHBOARD
    # ---------------------------------------------------

    if menu == "Dashboard":

        st.markdown("## 📊 Dashboard")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Candidates",
                len(df)
            )

        with col2:
            st.metric(
                "Highest Match Score",
                f"{df['Match Score'].max()}%"
            )

        with col3:
            st.metric(
                "Average ATS Score",
                f"{round(df['ATS Score'].mean(),1)}%"
            )

        # ---------------------------------------------------
        # TABLE
        # ---------------------------------------------------

        st.markdown("## 🏆 Ranked Candidates")

        st.dataframe(
            df,
            width='stretch'
        )

        # ---------------------------------------------------
        # DOWNLOAD XLSX
        # ---------------------------------------------------

        st.markdown("## ⬇ Export Report")

        output = io.BytesIO()

        with pd.ExcelWriter(
            output,
            engine='openpyxl'
        ) as writer:

            df.to_excel(
                writer,
                index=False,
                sheet_name='Candidates'
            )

        excel_data = output.getvalue()

        st.download_button(
            label="⬇ Download XLSX Report",
            data=excel_data,
            file_name="recommended_candidates.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        st.success("Analysis Completed Successfully!")

    # ---------------------------------------------------
    # ANALYTICS
    # ---------------------------------------------------

    elif menu == "Analytics":

        st.markdown("## 📈 Candidate Analytics")

        fig = px.bar(
            df,
            x="Candidate",
            y="Match Score",
            color="Match Score",
            text="Match Score"
        )

        st.plotly_chart(
            fig,
            width='stretch'
        )

        fig2 = px.pie(
            df,
            names="Recommendation",
            title="Recommendation Distribution"
        )

        st.plotly_chart(
            fig2,
            width='stretch'
        )

    # ---------------------------------------------------
    # AI INSIGHTS
    # ---------------------------------------------------

    elif menu == "AI Insights":

        st.markdown("## 🧠 AI Insights")

        for _, row in df.iterrows():

            st.markdown(f"""
            <div class="card">
                <h3>{row['Candidate']}</h3>

                <p>
                <b>ATS Score:</b> {row['ATS Score']}%
                </p>

                <p>
                <b>Match Score:</b> {row['Match Score']}%
                </p>

                <p>
                Missing Skills:
                Docker, Kubernetes, LangChain
                </p>

                <p>
                Suggested Learning Path:
                SQL → NLP → Transformers
                </p>

                <p>
                <b>{row['Recommendation']}</b>
                </p>

            </div>
            """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # LEADERBOARD
    # ---------------------------------------------------

    elif menu == "Leaderboard":

        st.markdown("## 🏅 Top Candidates")

        top_df = df.sort_values(
            by="Match Score",
            ascending=False
        )

        for _, row in top_df.iterrows():

            st.markdown(f"""
            <div class="card">
                <h2>#{row['Rank']} - {row['Candidate']}</h2>

                <h3>
                Match Score: {row['Match Score']}%
                </h3>

                <h4>
                ATS Score: {row['ATS Score']}%
                </h4>

                <p>
                {row['Recommendation']}
                </p>

            </div>
            """, unsafe_allow_html=True)

else:

    st.info("Upload resumes and click Analyze Candidates.")