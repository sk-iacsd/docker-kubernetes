# get the base image
FROM python:3-alpine

# define the workdir, it will create if not available
WORKDIR /app

# copy reqiuirement to install
COPY ./requirements.txt ./

# install the dependencies
RUN pip install -r requirements.txt

# Copy the remaining dir to container
COPY . .
EXPOSE 5000

CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
