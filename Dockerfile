#FROM python:3

#ADD . .

#RUN pip install --upgrade pip


#CMD ["python", "-m", "unittest", "discover", "-s", "Tests"]

FROM python:3.7


COPY . /web
WORKDIR /web
RUN pip install -r ./requirements.txt
ENTRYPOINT ["python"]
CMD ["/web/Database/sqlite_create.py"]