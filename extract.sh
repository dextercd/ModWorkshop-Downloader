#!/bin/sh

cd Extract/
for f in ../Download/*; do
    aunpack -D "$f" >/dev/null
done
