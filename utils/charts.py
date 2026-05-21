import plotly.graph_objects as go
import streamlit as st

def show_gauge_chart(failure_probability):

    gauge_chart = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=failure_probability,
            title={'text': "Failure Risk %"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "red"},
                'steps': [
                    {'range': [0, 30], 'color': "lightgreen"},
                    {'range': [30, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "salmon"}
                ]
            }
        )
    )

    st.plotly_chart(gauge_chart, use_container_width=True)