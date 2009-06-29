#!/bin/sh
# script to automatically commit all new files and changes
# (c)2009 greg albrecht (gba@gregalbrecht.com)

cd $HOME/src/scripts && git add $HOME/src/scripts/*
git commit -qam "$0 automatic commit" > /dev/null
git push

cd $HOME
git commit -qam "$0 automatic commit" > /dev/null
git push

