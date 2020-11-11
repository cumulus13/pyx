@echo off
REM  In the external application (or BAT file) the following environment variables available, pre-set by Hard Disk Sentinel:
    REM  HDS_TimeStamp : date and time of the actual alert in fixed format yyyymmdd hhmmss
    REM  HDS_TimeStampClean : date and time of the alert in user-friendly format (current Windows regional setting)
    REM  HDS_Host : current host (computer) name
    REM  HDS_Alert : the alert (eg. Overheat)
    REM  HDS_Disk : affected disk(s)
    REM  HDS_Threshold : threshold configured (contain Celsius/Fahrenheit or % symbols)
    REM  HDS_ThresholdValue : threshold configured (only the number)
    REM  HDS_Health : generic health information of all drives
    REM  HDS_Partition : generic partition information of all drives
    REM  HDS_LowestDiskHealth: the lowest health % value of all drives

"c:\Program Files (x86)\Growl for Windows\growlnotify.com" /t:REGISTER /i:f:\icons\Phuzion_Icon_Pack\png\Misc\Bug.png /a:HDDSentinel /ai:f:\icons\Phuzion_Icon_Pack\png\Misc\Bug.png /r:Notification /n:Notify "REGISTER FIRST !"

"c:\Program Files (x86)\Growl for Windows\growlnotify.com" /t:Message /i:f:\icons\Phuzion_Icon_Pack\png\Misc\Bug.png /a:HDDSentinel /n:Notification "[ HDS_TimeStamp ]: HDS_Alert => HDS_Disk ~ HDS_Threshold (HDS_ThresholdValue) [ HDS_LowestDiskHealth ]" /s:true

"c:\Program Files (x86)\Growl for Windows\growlnotify.com" /t:REGISTER /i:f:\icons\Phuzion_Icon_Pack\png\Misc\Bug.png /a:HDDSentinel /ai:f:\icons\Phuzion_Icon_Pack\png\Misc\Bug.png /r:Notification /n:Notify "REGISTER FIRST !" /host:192.168.43.1 /post:23353

"c:\Program Files (x86)\Growl for Windows\growlnotify.com" /t:Message /i:f:\icons\Phuzion_Icon_Pack\png\Misc\Bug.png /a:HDDSentinel /n:Notification "[ HDS_TimeStamp ]: HDS_Alert => HDS_Disk ~ HDS_Threshold (HDS_ThresholdValue) [ HDS_LowestDiskHealth ]" /s:true  /host:192.168.43.1 /post:23353