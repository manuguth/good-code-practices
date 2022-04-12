FROM python:3.10-slim

# install basic utilities
RUN \
  apt-get -qq -y update && \
  apt-get -qq -y upgrade && \
  apt-get install -y jq git tree hdf5-tools bash-completion && \
  apt-get install -y ffmpeg vim emacs && \
  apt-get install -y gcc libopenmpi-dev openmpi-bin graphviz && \
  apt-get clean && \
  rm -rf /var/lib/apt-get/lists/* && \
  true

# add repository to the image

# python installs
COPY requirements.txt .
RUN \
  pip3 install --upgrade pip && \
  pip3 install -r requirements.txt

RUN useradd -m ftag
COPY . /home/ftag
RUN chown -R ftag:ftag /home/ftag
USER ftag
WORKDIR /home/ftag

CMD /bin/bash

