FROM alpine:3.16

RUN apk --update add npm &&  \
    rm -rf /var/cache/apk/*

WORKDIR /build
ENV PATH node_modules/.bin:$PATH
COPY docker/theme_builder/package.json docker/theme_builder/build.sh docker/theme_builder/postcss.config.js ./
RUN npm install

ENTRYPOINT ["/build/build.sh"]
