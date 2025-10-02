FROM python:3.10
WORKDIR /LinkedinScraper
COPY requirements.txt /LinkedinScraper/
RUN pip install -r requirements.txt
COPY . /LinkedinScraper
CMD python app.py
