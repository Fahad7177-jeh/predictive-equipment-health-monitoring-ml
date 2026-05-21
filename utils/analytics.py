import streamlit as st
import plotly.express as px

def show_analytics(history_df):

    st.divider()

    st.subheader("📊 Analytics Dashboard")

    # KPI Calculations
    total_predictions = len(history_df)

    total_failures = len(
        history_df[
            history_df["prediction"] == "Failure"
        ]
    )

    total_healthy = len(
        history_df[
            history_df["prediction"] == "Healthy"
        ]
    )

    average_risk = history_df[
        "failure_probability"
    ].mean()

    # KPI Cards
    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric(
            "Total Predictions",
            total_predictions
        )

    with k2:
        st.metric(
            "Total Failures",
            total_failures
        )

    with k3:
        st.metric(
            "Healthy Machines",
            total_healthy
        )

    with k4:
        st.metric(
            "Average Risk %",
            f"{average_risk:.2f}"
        )

    st.divider()

    # Pie Chart
    pie_chart = px.pie(
        history_df,
        names="prediction",
        title="Healthy vs Failure Distribution"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

    # Failure Probability Trend
    trend_chart = px.line(
        history_df,
        x="created_at",
        y="failure_probability",
        title="Failure Probability Trend Over Time",
        markers=True
    )

    st.plotly_chart(
        trend_chart,
        use_container_width=True
    )