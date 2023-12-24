FROM python:3.8-slim

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --deploy

COPY app.py .
COPY ./boston-housing-regression/boston_housing_prediction.joblib .

EXPOSE 5000

CMD ["pipenv", "run", "python", "app.py"]
