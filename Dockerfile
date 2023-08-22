FROM python:3.11-slim
WORKDIR /opt/test_task
COPY . .
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install
#COPY . .

#ENTRYPOINT ["bash", "entrypoint.sh"]


CMD ["python", "manage.py", "runserver",   "0.0.0.0:8000"]

EXPOSE 8000