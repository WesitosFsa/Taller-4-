#!/usr/bin/bash
mkdir -p splits
split -l 33 -d logs.txt splits/part_ --additional-suffix=.txt