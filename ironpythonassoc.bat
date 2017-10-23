@echo off

ASSOC .ipy=IronPythonScript
ASSOC .ipy2=IronPython2WindowScript
ASSOC .ipy4=IronPython4WindowScript
ASSOC .ipyw=IronPythonWindowScript
ASSOC .ipyw2=IronPython2WindowScript
ASSOC .ipyw4=IronPython4WindowScript

FTYPE IronPython2Script="c:\Program Files\IronPython 2.6\ipy.exe" %1 %*
FTYPE IronPython2WindowScript="c:\Program Files\IronPython 2.6\ipyw.exe" %1 %*
FTYPE IronPython4Script="h:\IronPython 2.7\ipy.exe" %1 %*
FTYPE IronPython4WindowScript="h:\IronPython 2.7\ipyw.exe" %1 %*
FTYPE IronPythonScript="h:\IronPython 2.7\ipy.exe" %1 %*
FTYPE IronPythonWindowScript="c:\Program Files\IronPython 2.6\ipyw.exe" %1 %*


:end