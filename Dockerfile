FROM python:3.9 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt && apt-get update && apt-get install -y ffmpeg libsm6 libxext6

COPY ./number_generator /code/number_generator

EXPOSE 80

CMD ["uvicorn", "number_generator.api.api:app", "--host", "0.0.0.0", "--port", "80"]
