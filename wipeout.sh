SSH_ARGS="-q -o ConnectTimeout=5 -o PreferredAuthentications=publickey"
SSH_USER="mamboa"

if [ "$1" ]; then
	for m in $(echo $1|sed 's/,/ /g'); do
		ssh $SSH_ARGS $SSH_USER@$m "echo Wiping out $SSH_USER@$m"
		ssh $SSH_ARGS $SSH_USER@$m "ps | awk '{print \$2}'|xargs kill -9 2>&1 > /dev/null" 2>&1 > /dev/null
		ssh $SSH_ARGS $SSH_USER@$m "ps -aux|grep -i $SSH_USER| awk '{print \$2}'|xargs kill -9 2>&1 > /dev/null" 2>&1  > /dev/null
		ssh $SSH_ARGS $SSH_USER@$m "ps -ef|grep -i $SSH_USER| awk '{print \$2}'|xargs kill -9 2>&1 >/dev/null" 2>&1 > /dev/null
		ssh $SSH_ARGS $SSH_USER@$m "killall -u $SSH_USER 2>&1 > /dev/null" 2>&1 > /dev/null
		ssh $SSH_ARGS $SSH_USER@$m "killall -9 -u $SSH_USER 2>&1 > /dev/null" 2>&1 > /dev/null
		ssh $SSH_ARGS $SSH_USER@$m "rm -rf mambo 2>&1 > /dev/null" 2>&1 > /dev/null &
	done
fi
