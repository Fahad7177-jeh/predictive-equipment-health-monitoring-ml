import pandas as pd
import joblib

# Load model
model = joblib.load("models/predictive_maintenance_model.pkl")

def predict_machine_failure(
    air_temp,
    process_temp,
    rpm,
    torque,
    tool_wear
):

    sample_data = pd.DataFrame(
        [[
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear
        ]],
        columns=[
            'Air temperature [K]',
            'Process temperature [K]',
            'Rotational speed [rpm]',
            'Torque [Nm]',
            'Tool wear [min]'
        ]
    )

    prediction = model.predict(sample_data)

    probability = model.predict_proba(sample_data)

    failure_probability = probability[0][1] * 100

    healthy_probability = probability[0][0] * 100

    return (
        prediction,
        failure_probability,
        healthy_probability
    )