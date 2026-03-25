FROM python:3.12-slim-bookworm
WORKDIR /app

RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*
RUN curl -sSL https://astral.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

COPY pyproject.toml uv.lock ./

ENV UV_SYSTEM_PYTHON=1
RUN uv sync --locked --no-dev

COPY . .

CMD [ "uv", "run", "gunicorn", "-w", "4",  "app:proxy_app"]
