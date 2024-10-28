FROM python:3.10-slim

WORKDIR /app

ENV FLASK_APP=app.app
ENV FLASK_ENV=development

COPY . .
RUN pip install --no-cache-dir -r requirements/requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
