@echo off
curl -H "public-api-token: c5c3a2976e32ad7297e0732fd7a554e4" -X PUT -d "urlToShorten=%1" https://api.shorte.st/v1/data/url 