FROM python:3.9
RUN mkdir -p /src
WORKDIR  /src
ADD demo.py demo.py
EXPOSE 10000
CMD [ "python3" , "demo.py" ]