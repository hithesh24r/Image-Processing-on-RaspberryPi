#!/bin/bash

# Installing AWSCLI on Raspberry Pi
sudo apt-get install awscli -y
aws --version

# Defining variables to use them in the commands below
access_key="ENTER_YOUR_AWS_ACCESSKEY_HERE"
secret_access_key="ENTER_YOUR_AWS_SECRET_ACCESSKEY_HERE"
region="ENTER_YOUR_REGION_HERE"
bucket_name="ENTER_THE_NAME_OF_THE_S3_BUCKET_HERE"
mount_path="/home/pi/bucket"    # Change the path with the mount path you would like to configure

# aws configuration through awscli
aws configure set default.region $region    # Configuring region for AWSCLI
aws configure set aws_access_key_id $access_key   # Configuring AWS Accesskey
aws configure set aws_secret_access_key $secret_access_key    # Configurong AWS Secret Accesskey

# Synchronizing the mount path with AWS S3 Bucket
# Changes made in mount path are reflected in bucket and vice-versa
aws s3 sync $mount_path s3://$bucket_name
echo $access_key:$secret_access_key > "$HOME/.passwd_s3fs"
chmod 600 "$HOME/.passwd_s3fs"
s3fs $bucket_name $mount_path -o passwd_file="${HOME}/.passwd_s3fs",nonempty,allow_other,mp_umask=002,uid=1000,gid=1000 -o url=http://s3.$region.amazonaws.com,endpoint=$region,use_path_re>echo $bucket_name $mount_path fuse.s3fs _netdev,allow_other 0 0 >> "/etc/fstab"

# Confirmation Message
echo Mount location $mount_path successfully connected to the bucket $bucket_name
