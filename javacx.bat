@echo off
title %CD%
if %1*==* goto usage

javac.exe -classpath "c:\Program Files\Java\jdk1.6.0_03\lib\dt.jar";"c:\Program Files\Java\jdk1.6.0_03\lib\htmlconverter.jar";"c:\Program Files\Java\jdk1.6.0_03\lib\jconsole.jar";"c:\Program Files\Java\jdk1.6.0_03\lib\jython.jar";"c:\Program Files\Java\jdk1.6.0_03\lib\mysql-connector-java-3.0.8-stable-bin.jar";"c:\Program Files\Java\jdk1.6.0_03\lib\mysql-connector-java-3.2.0-alpha-bin.jar";"c:\Program Files\Java\jdk1.6.0_03\lib\mysql-connector-java-5.1.5-bin.jar";"c:\Program Files\Java\jdk1.6.0_03\lib\tools.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\charsets.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\deploy.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\javaws.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\jce.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\jsse.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\management-agent.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\plugin.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\resources.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\rt.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\ext\dnsns.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\ext\localedata.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\ext\sunjce_provider.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\ext\sunmscapi.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\ext\sunpkcs11.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\im\indicim.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\im\thaiim.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\security\local_policy.jar";"c:\Program Files\Java\jdk1.6.0_03\jre\lib\security\US_export_policy.jar";  %1

goto end

:usage
echo.
echo.
echo        usage      :%0 [File *.class] [but not using extention .class]
echo.
echo        example    : %0 server [it's same %0 server.class]
echo.
echo.
goto end

:end



