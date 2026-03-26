FROM python:3.12-slim-bookworm
WORKDIR /app

RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*
RUN curl -sSL https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml uv.lock ./

ENV UV_SYSTEM_PYTHON=1
RUN uv sync --locked --no-dev

COPY . .

CMD [ "uv", "run", "gunicorn", "--bind", "0.0.0.0", "-w", "4",  "app:proxy_app"]
