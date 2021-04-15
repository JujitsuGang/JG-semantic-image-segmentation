FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

ARG git_owner="singnet"
ARG git_repo="semantic-segmentation"
ARG git_branch="master"
ARG snetd_version

ENV SINGNET_DIR=/opt/singnet
ENV SERVICE_NAME=semantic-segmentation

RUN mkdir -p ${SINGNET_DIR}

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa && \
      apt-get update && \
      apt-get upgrade -y && \
      apt-get install -y python3.6 python3.6-dev build-essential cmake libgtk2.0-dev python3.6-tk && \
      curl https://bootstrap.pypa.io/get-pip.py | python3.6

RUN apt-get update && \
    apt-get install -y 