import streamlit as st
import joblib

# Import custom functions
from utils.predict import predict_machine_failure
from utils.charts import show_gauge_chart
from utils.feature_importance import show_feature_importance
from utils.database import (
    save_prediction,
    get_prediction_history
)
from utils.analytics import show_analytics
from utils.auth import (
    register_user,
    login_user
)

# Page configuration
st.set_page_config(
    page_title="Predictive Equipment Health Monitoring",
    page_icon="⚙️",
    layout="wide"
)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ==============================
# AUTHENTICATION SECTION
# ==============================

menu = st.sidebar.selectbox(
    "Menu",
    ["Login", "Register"]
)

# REGISTER
if menu == "Register":

    st.title("📝 Register")

    new_username = st.text_input("Username")

    new_password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        try:

            register_user(
                new_username,
                new_password
            )

            st.success("User Registered Successfully")

        except:

            st.error("Username Already Exists")


# LOGIN
elif menu == "Login":

    st.title("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            username,
            password
        )

        if user:

            st.session_state.logged_in = True

            st.success("Login Successful")

        else:

            st.error("Invalid Username or Password")

# ==============================
# MAIN DASHBOARD
# ==============================

if st.session_state.logged_in:

    # Load model
    model = joblib.load(
        "models/predictive_maintenance_model.pkl"
    )

    # Feature importance
    feature_importance = model.feature_importances_

    feature_names = [
        'Air Temp',
        'Process Temp',
        'RPM',
        'Torque',
        'Tool Wear'
    ]

    # Sidebar info
    st.sidebar.title("⚙️ System Information")

    st.sidebar.info(
        """
        This application predicts machine failure using Machine Learning.

        Model Used:
        - Random Forest Classifier

        Features:
        - Air Temperature
        - Process Temperature
        - RPM
        - Torque
        - Tool Wear
        """
    )

    # Logout button
    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()

    # Main title
    st.title(
        "⚙️ Predictive Equipment Health Monitoring System"
    )

    st.markdown(
        "### Enter machine parameters to predict equipment failure"
    )

    st.divider()

    # Columns
    col1, col2 = st.columns(2)

    # LEFT COLUMN
    with col1:

        air_temp = st.number_input(
            "Air Temperature [K]",
            min_value=250.0,
            max_value=400.0,
            value=300.0
        )

        process_temp = st.number_input(
            "Process Temperature [K]",
            min_value=250.0,
            max_value=400.0,
            value=310.0
        )

        rpm = st.number_input(
            "Rotational Speed [rpm]",
            min_value=0,
            max_value=5000,
            value=1500
        )

    # RIGHT COLUMN
    with col2:

        torque = st.number_input(
            "Torque [Nm]",
            min_value=0.0,
            max_value=100.0,
            value=40.0
        )

        tool_wear = st.number_input(
            "Tool Wear [min]",
            min_value=0,
            max_value=300,
            value=100
        )

    st.divider()

    # Prediction button
    if st.button(
        "🔍 Predict Machine Health",
        use_container_width=True
    ):

        (
            prediction,
            failure_probability,
            healthy_probability
        ) = predict_machine_failure(
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear
        )

        # Prediction label
        prediction_label = (
            "Healthy"
            if prediction[0] == 0
            else "Failure"
        )

        # Save to MySQL
        save_prediction(
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear,
            failure_probability,
            prediction_label
        )

        # Gauge chart
        show_gauge_chart(
            failure_probability
        )

        st.subheader("📊 Prediction Results")

        # Metrics
        m1, m2 = st.columns(2)

        with m1:
            st.metric(
                "Failure Probability",
                f"{failure_probability:.2f}%"
            )

        with m2:
            st.metric(
                "Healthy Probability",
                f"{healthy_probability:.2f}%"
            )

        st.divider()

        # Risk level
        if failure_probability < 30:

            st.success(
                "🟢 Low Risk Machine"
            )

        elif failure_probability < 70:

            st.warning(
                "🟡 Medium Risk Machine"
            )

        else:

            st.error(
                "🔴 High Risk Machine"
            )

        # Final prediction
        if prediction[0] == 0:

            st.success(
                "✅ Machine is Healthy"
            )

        else:

            st.error(
                "⚠️ Machine Failure Predicted"
            )

    # Feature Importance
    st.divider()

    st.subheader(
        "📈 Feature Importance Analysis"
    )

    show_feature_importance(
        feature_names,
        feature_importance
    )

    # Prediction History
    st.divider()

    st.subheader(
        "🗂 Prediction History Dashboard"
    )

    history_df = get_prediction_history()

    # Filter dropdown
    filter_option = st.selectbox(
        "Filter Predictions",
        [
            "All",
            "Failure Only",
            "Healthy Only",
            "High Risk (>70%)"
        ]
    )

    # Apply filters
    if filter_option == "Failure Only":

        history_df = history_df[
            history_df["prediction"] == "Failure"
        ]

    elif filter_option == "Healthy Only":

        history_df = history_df[
            history_df["prediction"] == "Healthy"
        ]

    elif filter_option == "High Risk (>70%)":

        history_df = history_df[
            history_df[
                "failure_probability"
            ] > 70
        ]

    # Show dataframe
    st.dataframe(
        history_df,
        use_container_width=True
    )

    # Analytics
    show_analytics(history_df)

    # Download reports
    st.divider()

    st.subheader("📥 Download Reports")

    csv = history_df.to_csv(index=False)

    st.download_button(
        label="⬇ Download Prediction History CSV",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv"
    )