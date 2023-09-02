# get the base image
FROM python:alpine3.18

# define the workdir, it will create if not available
WORKDIR /usr/app

# copy reqiuirement to install
COPY ./requirements.txt ./

# install the dependencies
RUN pip install -r requirements.txt

# Copy the remaining dir to container
COPY ./ ./

CMD ["python", "calculator.py"]
