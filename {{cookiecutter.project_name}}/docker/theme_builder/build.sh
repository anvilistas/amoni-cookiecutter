#!/bin/sh
APP_NAME=$1
OUTPUT_FILE="/app/${APP_NAME}/theme/assets/theme.css"

mkdir /build/src
cp -r /theme/* /build/src
postcss src/index.css -o ${OUTPUT_FILE}
rm -rf build/src
