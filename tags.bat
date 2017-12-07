@echo off
mp3test -rq "%CD%"
tagscan "%CD%" 
echo ----------------------------------------------------------------
mp3test -rq "%CD%"