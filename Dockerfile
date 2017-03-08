FROM python
WORKDIR /work
RUN apt-get update && apt-get install -y vim
