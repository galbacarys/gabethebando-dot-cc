FROM python:3.12-slim-bookworm
WORKDIR /app

RUN apt-get update && apt-get install -y curl build-essential sqlite3 && rm -rf /var/lib/apt/lists/*
RUN curl -sSL https://astral.sh/uv/install.sh | sh

RUN curl -o litestream.deb -sSL https://github.com/benbjohnson/litestream/releases/download/v0.5.8/litestream-0.5.8-linux-x86_64.deb

RUN dpkg -i litestream.deb && rm litestream.deb

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml uv.lock ./

ENV UV_SYSTEM_PYTHON=1
RUN uv sync --locked --no-dev

COPY . .

CMD [ "uv", "run", "gunicorn", "--bind", "0.0.0.0", "-w", "4",  "app:proxy_app"]
