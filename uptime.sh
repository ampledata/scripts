	
KNOWN_HOSTS=$(cat $HOME/.ssh/known_hosts |awk '{print $1}'|tr -s ',' '\n'|sort|uniq)

for k in $KNOWN_HOSTS; do
	UPTIME=$( ssh -q -o ConnectTimeout=5 -o PreferredAuthentications=publickey gba@$k uptime || \
	ssh -q -o ConnectTimeout=5 -o PreferredAuthentications=publickey galbrecht@$k uptime ) 
	if [ "$UPTIME" ]; then
		echo "$k $UPTIME"
	fi
done
