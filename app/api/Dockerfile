FROM python:3.10.8

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN python3 -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet')"

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]