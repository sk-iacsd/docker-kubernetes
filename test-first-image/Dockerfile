# Adding the base image(OS) from docker hub for custome image
FROM alpine:latest

# Adding the packages for redis
RUN apk add --update redis

# command to run in docker
CMD ["redis-server"]