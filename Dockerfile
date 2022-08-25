FROM python:3.8 as base


ENV POETRY_HOME=${HOME}/.poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY . .
RUN poetry install

EXPOSE 5100

COPY /todo_app/ ./todo_app/


# production stage
FROM base as production
ENTRYPOINT [ "poetry", "run", "gunicorn", "--workers=2", "--bind", "0.0.0.0:80", "todo_app.app:create_app()" ]


# dev stage
FROM base as development
ENTRYPOINT [ "poetry", "run", "flask", "run", "--host", "0.0.0.0", "--port", "80"]


# testing stage
FROM base as test
ENTRYPOINT ["poetry", "run", "pytest"]