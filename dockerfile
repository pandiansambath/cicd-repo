FROM python:3.8-slim
WORKDIR /docdir
COPY . .
RUN pip install pytest
CMD ["python", "calc.py"]