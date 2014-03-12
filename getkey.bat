echo off
if %1*==* goto usage
echo -n | openssl s_client -connect %1 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > %2
:usage
echo "example: echo -n | openssl s_client -connect pypi.python.org:443 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > SERVERNAME.cert"

