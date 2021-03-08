FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

ARG git_owner="singnet"
ARG git_repo="semantic-segmentation"
ARG git_branch="master"
ARG snetd_version

ENV SINGNET_DIR=/opt/singnet
ENV SERVICE_NAME=semantic-segmentation

RUN mkdir -p ${SI