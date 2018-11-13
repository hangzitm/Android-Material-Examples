#/bin/bash
P_NAME=$1      
P_BUILD_ID=$2   
P_RELEASE=$3   
P_DATE=$4       

P_SOURCE_APK="app/build/outputs/apk/app-$P_RELEASE.apk"
P_TARGET_DIR="/opt/home/jenkins_build/android/output/$P_NAME"
P_TARGET_APK="$P_TARGET_DIR/$P_DATE-$P_VERSION-$P_RELEASE#$P_BUILD_ID.apk"


mkdir -p $P_TARGET_DIR
cp $P_SOURCE_APK $P_TARGET_APK


