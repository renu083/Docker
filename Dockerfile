FROM python:3
ADD movierate.py / 
RUN pip install Requests
CMD [ "python", "./movierate.py" ]
