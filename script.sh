#!/bin/bash

# terminate any existing node web services
kill $(ps au | grep node | grep -v 'grep' | awk '{print $2}')

if [ $terminate ]
then
  echo 'just terminate'
  exit
fi

echo 'after terminate'
