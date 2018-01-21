FROM python:3.6.4-jessie
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt
CMD ["./test.sh"]