#!/bin/sh
# script to automatically commit all new files and changes
# (c)2009 greg albrecht (gba@gregalbrecht.com)

git add *
git commit -am "$0 automatic commit"
git push
