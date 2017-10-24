configs=`cat localservices.config`
services=''
ctr=0
port=''
for config in $configs
	do
		rem=$(( $ctr % 2 ))
 
		if [ $ctr -eq 1 ]
			then
				port=$config
		fi

		if [ $rem -eq 0 ]
			then
				services="$services$config/app.yaml "
		fi
		ctr=$((ctr+1))
	done
echo `dev_appserver.py $services --port $port`