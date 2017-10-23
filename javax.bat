
@rem ----- ExeScript Options Begin -----
@rem ScriptType: console,silent,invoker
@rem DestDirectory: temp
@rem Icon: default
@rem OutputFile: g:\temp\javax.exe
@rem ----- ExeScript Options End -----
@echo off
title %CD%
if %1*==* goto usage

rem cls
rem echo.
echo.
java.exe -splash:"D:\ICONS\Phuzion_Icon_Pack\PNG\Apps\Java.png" -classpath "%SDK_HOME%\jre1.6.0_03\lib\dt.jar";"%SDK_HOME%\jre1.6.0_03\lib\htmlconverter.jar";"%SDK_HOME%\jre1.6.0_03\lib\jconsole.jar";"%SDK_HOME%\jre1.6.0_03\lib\jython.jar";"%SDK_HOME%\jre1.6.0_03\lib\mysql-connector-java-3.0.8-stable-bin.jar";"%SDK_HOME%\jre1.6.0_03\lib\mysql-connector-java-3.2.0-alpha-bin.jar";"%SDK_HOME%\jre1.6.0_03\lib\mysql-connector-java-5.1.5-bin.jar";"%SDK_HOME%\jre1.6.0_03\lib\tools.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\charsets.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\deploy.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\javaws.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\jce.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\jsse.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\management-agent.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\plugin.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\resources.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\rt.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\ext\dnsns.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\ext\localedata.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\ext\sunjce_provider.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\ext\sunmscapi.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\ext\sunpkcs11.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\im\indicim.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\im\thaiim.jar";"%SDK_HOME%\jre1.6.0_03jre1.6.0_03\jre\lib\security\local_policy.jar";"%SDK_HOME%\jre1.6.0_03\jre\lib\security\US_export_policy.jar";"%SDK_HOME%\lib\mysql-connector-java-5.1.5-bin.jar";"%SDK_HOME%\lib\Oranxo.jar";  %1

echo.
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



