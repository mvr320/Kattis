#! /bin/bash
problem="${PWD##*/}"
url="https://open.kattis.com/problems/$problem/file/statement/samples.zip"
curl $url > samples.zip
unzip samples.zip
rm samples.zip
