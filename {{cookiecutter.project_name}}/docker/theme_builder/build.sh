#!/bin/sh
APP_NAME=$1
OUTPUT_FILE="/app/${APP_NAME}/theme/assets/theme.css"

mkdir /build/src
cp -r /theme/* /build/src
find -type f -exec sed -i -r 's/(%color:.*%)/"--substitution--\1--substitution--";/' {} \;
find -type f -exec sed -i 's/%anvil-banner-height%/var(--anvil-banner-height)/' {} \;
postcss src/index.css -o theme.css
sed -i 's/"--substitution--//g' theme.css
sed -i 's/--substitution--"//g' theme.css
sed -i 's/var(--anvil-banner-height)/%anvil-banner-height%/g' theme.css
mv theme.css ${OUTPUT_FILE}
rm -rf build/src
