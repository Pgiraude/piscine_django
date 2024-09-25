#!/bin/bash

html= curl -s "$1" | grep -oP '(?<=href=")[^"]+'
