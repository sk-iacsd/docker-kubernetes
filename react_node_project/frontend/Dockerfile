# This is for prod build, for that we will use nginx, to depoly static fles only
# first base image is for creating the dev version and then build from it, and we need to provide the alias 
# as next base image can reuse the files from this one

FROM node:alpine3.18 as builder

WORKDIR /app

COPY ./package.json .
RUN npm install

COPY . .

RUN npm run build

# we need the build folder from the above work, so that we can use those static files only in prod not the all packages

FROM nginx
COPY --from=builder /app/build /usr/share/nginx/html
