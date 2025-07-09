FROM python:3.11-slim

WORKDIR /main-container

COPY requirements/requirements.txt /main-container/
COPY src-file/main-endpoint.py /main-container/
COPY models/logistic-regression-new.pkl /main-container/
COPY models/svc-new.pkl /main-container/
COPY models/decision-tree-new.pkl /main-container/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main-endpoint:main_api", "--host", "0.0.0.0", "--port", "8080"]
