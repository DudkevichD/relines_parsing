FROM python:3.8
RUN mkdir -p /usr/srs/app/
WORKDIR /usr/srs/app/
COPY . /usr/srs/app/
RUN pip install -r requirements.txt
CMD ["python"]
