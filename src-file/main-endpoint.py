# Standard python imports
from typing import Union, Annotated

# Non standard Python imports
import joblib
import pandas as pd
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

main_api = FastAPI()
logistic_regression_model = joblib.load("/main-container/logistic-regression-new.pkl")
svc_model = joblib.load("/main-container/svc-new.pkl")
decision_tree_model = joblib.load("/main-container/decision-tree-new.pkl")

class BaseFeatures (BaseModel):
    network_packet_size: Annotated[int, Field(..., strict=True)]
    protocol_type: Annotated[str, Field(strict=True)]
    login_attempts: Annotated[int, Field(strict=True)]
    session_duration: Annotated[int, Field(..., strict=True)]
    encryption_used: Annotated[str, Field(strict=True)]
    ip_reputation_score: Annotated[float, Field(strict=True)]
    failed_logins: Annotated[int, Field(strict=True)]
    unusual_time_access: Annotated[int, Field(strict=True)]

class ModelPrediction (BaseModel):
    model_prediction: Annotated[int, Field(description="The model's prediction")]

@main_api.get("/")
def hello ():
    return {"message": "Hello world"}

@main_api.post("/predict", response_model=ModelPrediction)
def predict_post (model: Annotated[str, Query(strict=True)], features: BaseFeatures):
    # Assembling the input
    temp_pd = {
        "network_packet_size": features.network_packet_size,
        "protocol_type": features.protocol_type,
        "login_attempts": features.login_attempts,
        "session_duration": features.session_duration,
        "encryption_used": features.encryption_used,
        "ip_reputation_score": features.ip_reputation_score,
        "failed_logins": features.failed_logins,
        "unusual_time_access": features.unusual_time_access
    }
    main_pd = pd.DataFrame(temp_pd, index=[0], columns=temp_pd.keys())

    if model == "logistic":
        model_prediction = logistic_regression_model.predict(main_pd)
    elif model == "svc":
        model_prediction = svc_model.predict(main_pd)
    elif model == "tree":
        model_prediction = decision_tree_model.predict(main_pd)
    else:
        print("[-] Error: Selected model is incorrect or none")

    return ModelPrediction(model_prediction=int(model_prediction))
