#!/usr/bin/env bash

mount=${1:-/media/owain/NYANPY}

for a in *.py
do
  md5new=$(md5sum ${a} | awk '{print $1}')
  md5orig=$(md5sum ${mount}/${a} 2> /dev/null | awk '{print $1}')
  if [ "${md5new}" == "${md5orig}" ] 
  then
    echo "Skipping ${a} as file has not changed."
  else 
    echo "Copying ${a} to ${mount}."
    cp ${a} ${mount}/${a}
  fi
done
