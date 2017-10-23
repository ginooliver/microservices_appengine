configs=`cat localservices.config`
services=''
ctr=0
for config in $configs
	do
		rem=$(( $ctr % 2 ))
 
		if [ $rem -eq 0 ]
			then
				services="$services$config/app.yaml "
		fi
		ctr=$((ctr+1))
	done
echo `dev_appserver.py $services`