FROM python:3.8-slim
WORKDIR /app
COPY . .
CMD ["sh", "-c", "python app.py && python car.py && exec bash"]
