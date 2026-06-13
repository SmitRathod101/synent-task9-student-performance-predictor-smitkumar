import streamlit as st
import pickle
import numpy as np

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# =====================================
# LOAD MODEL
# =====================================

with open("model/model.pkl", "rb") as file:
    model = pickle.load(file)

# =====================================
# CSS
# =====================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    max-width:95%;
}

.stSlider{
    margin-bottom:-5px;
}

.stSelectbox{
    margin-bottom:-5px;
}

[data-testid="stMetric"]{
    text-align:center;
}

.stProgress{
    margin-bottom:0px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.title("🎓 Student Performance Predictor")

st.caption(
    "Machine Learning Dashboard for Academic Performance Prediction"
)

# =====================================
# LAYOUT
# =====================================

left, right = st.columns([1.15, 0.85])

# =====================================
# INPUT SECTION
# =====================================

with left:

    st.subheader("📋 Student Information")

    hours = st.slider(
        "Hours Studied",
        0,
        12,
        6
    )

    previous_scores = st.slider(
        "Previous Scores",
        0,
        100,
        70
    )

    activities = st.selectbox(
        "Extracurricular Activities",
        ["No", "Yes"]
    )

    sleep_hours = st.slider(
        "Sleep Hours",
        0,
        12,
        7
    )

    papers = st.slider(
        "Practice Papers",
        0,
        20,
        5
    )

    predict = st.button(
        "🚀 Predict Performance",
        use_container_width=True
    )

# =====================================
# RESULTS
# =====================================

with right:

    st.subheader("📊 Prediction Results")

    if predict:

        activity_value = 1 if activities == "Yes" else 0

        features = np.array([[
            hours,
            previous_scores,
            activity_value,
            sleep_hours,
            papers
        ]])

        prediction = model.predict(features)[0]

        st.metric(
            "Predicted Score",
            f"{prediction:.2f}"
        )

        st.progress(
            min(int(prediction), 100)
        )

        if prediction >= 85:

            st.success("🌟 Excellent Performance")

            recommendations = [
                "Maintain your current study routine",
                "Continue solving practice papers"
            ]

        elif prediction >= 70:

            st.info("👍 Good Performance")

            recommendations = [
                "Increase revision frequency",
                "Practice more sample papers"
            ]

        elif prediction >= 50:

            st.warning("⚠️ Average Performance")

            recommendations = [
                "Increase daily study time",
                "Solve more practice papers"
            ]

        else:

            st.error("📚 Needs Improvement")

            recommendations = [
                "Create a study timetable",
                "Practice core concepts daily"
            ]

        st.markdown("### 🎯 Recommendations")

        st.write(f"✓ {recommendations[0]}")
        st.write(f"✓ {recommendations[1]}")

    else:

        st.info(
            "👈 Enter student details and click Predict Performance."
        )

# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "Built with Python • Scikit-Learn • Streamlit"
)