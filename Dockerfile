FROM python:3.11-slim
WORKDIR /workspace
COPY . .
CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
