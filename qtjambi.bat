@echo off

if not exist com_trolltech_qt_core.dll mklink com_trolltech_qt_core.dll e:\qtjambi\lib\com_trolltech_qt_core.dll
if not exist com_trolltech_qt_gui.dll mklink com_trolltech_qt_gui.dll e:\qtjambi\lib\com_trolltech_qt_gui.dll
if not exist com_trolltech_qt_network.dll mklink com_trolltech_qt_network.dll e:\qtjambi\lib\com_trolltech_qt_network.dll
if not exist com_trolltech_qt_opengl.dll mklink com_trolltech_qt_opengl.dll e:\qtjambi\lib\com_trolltech_qt_opengl.dll
if not exist com_trolltech_qt_phonon.dll mklink com_trolltech_qt_phonon.dll e:\qtjambi\lib\com_trolltech_qt_phonon.dll
if not exist com_trolltech_qt_sql.dll mklink com_trolltech_qt_sql.dll e:\qtjambi\lib\com_trolltech_qt_sql.dll
if not exist com_trolltech_qt_svg.dll mklink com_trolltech_qt_svg.dll e:\qtjambi\lib\com_trolltech_qt_svg.dll
if not exist com_trolltech_qt_webkit.dll mklink com_trolltech_qt_webkit.dll e:\qtjambi\lib\com_trolltech_qt_webkit.dll
if not exist com_trolltech_qt_xml.dll mklink com_trolltech_qt_xml.dll e:\qtjambi\lib\com_trolltech_qt_xml.dll
if not exist com_trolltech_qt_xmlpatterns.dll mklink com_trolltech_qt_xmlpatterns.dll e:\qtjambi\lib\com_trolltech_qt_xmlpatterns.dll
if not exist com_trolltech_tools_designer.dll mklink com_trolltech_tools_designer.dll e:\qtjambi\lib\com_trolltech_tools_designer.dll
if not exist qtjambi.dll mklink qtjambi.dll e:\qtjambi\lib\qtjambi.dll

java -classpath e:\qtjambi\qtjambi-4.4.3_01.jar; %1
del *.log
del *.dll