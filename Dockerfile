FROM python:3.11

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY ./blog ./blog/
COPY ./mysite ./mysite/ 
COPY manage.py .
COPY requirements.txt . 

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 8000

# run the command
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]