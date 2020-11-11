@echo off
adb shell "service call audio 3 i32 3 i32 %1 i32 1"