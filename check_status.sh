#!/bin/bash 

MARKER=1 
FDATE=`date "+%Y.%m.%d %H:%M:%S"` 
LOG="/home/pprb_test/prometheus.log" 

if [[ $MARKER = 1 ]] 
then 
echo "${FDATE} Marker: ${MARKER}, check prometheus PID ">>$LOG 
PID=`ps -ef | grep prometheus | grep -v grep | grep -v '.sh' | awk '{print $2}'` 
if [[ $PID = "" ]] 
then 
echo "${FDATE} PID not found, try to run prometheus">>$LOG 
cd /home/pprb_test/prometheus-2.22.2.linux-amd64 | nohup ./prometheus & 
PID=`ps -ef | grep prometheus | grep -v grep | grep -v '.sh' | awk '{print $2}'` 
echo "${FDATE} influx run, PID=${PID}">>$LOG 
else 
echo "${FDATE} PID=$PID, nothing to do">>$LOG 
fi 
else 
echo "${FDATE} Marker = ${MAR
