#!/bin/bash
# Made by Christian
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
