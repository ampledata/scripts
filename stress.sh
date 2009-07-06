#!/bin/sh

function rsleep() {
        MY_SLEEP=$( expr $RANDOM / 100 )
        echo "sleeping for $MY_SLEEP"
        sleep $MY_SLEEP
}

while true; do python stress.py ; rsleep;done
