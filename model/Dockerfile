#this specifies the base image for the container. we are using lightweight python 3.9 image (slim variant) to keep the image size small
FROM python:3.9-slim  

#set the working direcrtory inside the container to /app, all subsequent commands eg copy, run will execute in this directory
WORKDIR /app

#Copy the requirements file from local to /app directory in the container
COPY requirements.txt .

#Install python dependencies inside the container, --no-cache-dir flag ensures no chached files are stores, reducing the image size
RUN pip install --no-chache-dir -r requirements.txt

#This copies all the files from your locak model folder into the /app directory in the container
COPY . .

#this specifies the default command to run when the container starts. In this case, it runs the train.py script by default.
CMD ["python","train.py"]