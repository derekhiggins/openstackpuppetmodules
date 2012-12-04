#!/usr/bin/env bash

mkdir -p dist

VERSION=2012.2.1
TYPE=dev
SNAPTAG=$(git log --oneline | wc -l)
if [ "$1" = "release" ] ; then
    SNAPTAG=""
    TYPE=""
fi

VERSIONEDNAME=openstackpuppetmodules-${VERSION}${TYPE}${SNAPTAG}

tar -cvzf dist/${VERSIONEDNAME}.tar.gz \
    --exclude='.git*' \
    --transform="s,^,${VERSIONEDNAME}/,S" \
    --show-transformed-names \
    modules LICENSE README

