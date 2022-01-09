#!/bin/bash
# Made by Christian
curl -sI GET $1 | grep "Allow" | cut -f2- -d " "
