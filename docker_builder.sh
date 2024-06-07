#!/bin/bash

if [ $# -lt 1 ]; then
  echo "버전을 입력하세요."
  exit 1
fi

version=$1
export VERSION="v$version"
echo VERSION;

# mkdir empty folder
{
  mkdir media
}||{
  echo ""
}


# docker compose build
docker compose up --build -d