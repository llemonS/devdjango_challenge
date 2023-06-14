FROM node:13.12.0-alpine
ADD . /devdjango_challenge/frontend
WORKDIR /devdjango_challenge/frontend
COPY package.json package-lock.json /devdjango_challenge/frontend
RUN npm install 
RUN npm install react-scripts@3.4.1 -g 
EXPOSE 3000
VOLUME /devdjango_challenge/frontend