#!/bin/sh
##
## Add SSH key from SecurePass
##


get_ssh_key()
{
   local user="$1"
   sshkey=$(sp-user-xattrs $user list|grep sshkey |cut -d: -f2)
   sshkey=${sshkey%%}
   echo $sshkey
}

if [ "x$1" == "x" ]
then
   echo "Please specify the username"
   exit 1
fi

KEY=$(get_ssh_key $1)
rc=$(grep "$KEY" ~/.ssh/authorized_keys)

if [ -z "$rc" ] 
then 
   echo $KEY >> ~/.ssh/authorized_keys; 
   echo "Key added"
fi
