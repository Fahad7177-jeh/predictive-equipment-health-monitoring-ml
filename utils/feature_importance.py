import matplotlib.pyplot as plt
import streamlit as st

def show_feature_importance(feature_names, feature_importance):

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(feature_names, feature_importance)

    ax.set_xlabel("Features")
    ax.set_ylabel("Importance Score")
    ax.set_title("Feature Importance")

    st.pyplot(fig)