#!/usr/bin/env bash

mkdir -p dist

VERSION=2012.2.1
TYPE=dev
SNAPTAG=$(git log --oneline | wc -l)
if [ "$1" = "release" ] ; then
    SNAPTAG=""
    TYPE=""
fi

tar -czf dist/openstackpuppetmodules-${VERSION}${TYPE}${SNAPTAG}.tar.gz --exclude='.git*' modules 

