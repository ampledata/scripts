#!/bin/sh
# script to automatically commit all new files and changes to git

PATH=$PATH:/opt/local/bin
export PATH

cd $HOME/src/scripts && git --work-tree=$HOME/src/scripts add $HOME/src/scripts/*
git --work-tree=$HOME/src/scripts commit -qam "$0 automatic commit" 
git --work-tree=$HOME/src/scripts push

cd $HOME
git --work-tree=$HOME commit -qam "$0 automatic commit" 
git --work-tree=$HOME push

