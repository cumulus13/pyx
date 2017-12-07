@echo off
if %1*==* goto usage
echo  %CD%\python setup.py
if NOT EXIST %CD%\setup.py goto error
if %1==-h goto usage
if %1==--help goto usage
if %1==-s goto sdist
if %1==-b goto build
if %1==-B goto build_bdist_wininst
if %1==-t goto build_bdist_wininst_27
if %1==-T goto build_bdist_wininst_27_install
if %1==-r goto build_register
if %1==-R goto build_bdist_wininst_register
if %1==-j goto build_bdist_wininst_register_upload
if %1==-a goto all
if %1==--all goto all
goto end

:build
python setup.py build
goto end

:build_bdist_wininst
python setup.py build
python setup.py bdist_wininst --skip-build
if %2*==* goto end
if %2==-c goto endclean
if %2==--clean goto endclean

:sdist
if %2*==* goto error1
@echo off
python setup.py sdist register -r %2 upload -r %2	
if %3*==* goto end
if %3==-c goto endclean
if %3==--clean goto endclean
goto end

:build_bdist_wininst_27
if %2*==* goto error1
python setup.py build
python setup.py bdist_wininst --skip-build
python setup.py bdist_wininst --skip-build --target-version %2
if %3*==* goto end
if %3==-c goto endclean
if %3==--clean goto endclean

:build_bdist_wininst_27_install
if %2*==* goto error1
python setup.py build
python setup.py bdist_wininst --skip-build
python setup.py bdist_wininst --skip-build --target-version %2
python setup.py install
if %3*==* goto end
if %3==-c goto endclean
if %3==--clean goto endclean

:build_register
if %2*==* goto error1
python setup.py build
python setup.py sdist register -r %2
if %3*==* goto end
if %3==-c goto endclean
if %3==--clean goto endclean
goto end

:build_bdist_wininst_register
if %2*==* goto error1
if %3*==* goto error2
python setup.py build
python setup.py build bdist_wininst
python setup.py build bdist_wininst --target-version %3
python setup.py sdist register -r %2	
if %4*==* goto end
if %4==-c goto endclean
if %4==--clean goto endclean
goto end

:build_bdist_wininst_register_upload
if %2*==* goto error1
if %3*==* goto error2
python setup.py build
python setup.py build bdist_wininst
python setup.py build bdist_wininst --target-version %3
python setup.py sdist register -r %2	
python setup.py sdist upload -r %2	
if %4*==* goto end
if %4==-c goto endclean
if %4==--clean goto endclean
goto end

:all
if %2*==* goto error1
if %3*==* goto error2
python setup.py build
python setup.py build bdist_wininst
python setup.py build bdist_wininst --target-version %3
python setup.py sdist register -r %2	
python setup.py sdist upload -r %2	
python setup.py install
if %4*==* goto end
if %4==-c goto endclean
if %4==--clean goto endclean
goto end

:error
echo.
echo "setup.py" NOT FOUND !!!
echo.
goto usage

:error1
echo.
echo PLEASE DEFINTION PYPI SERVER NAME !!!
echo.
goto usage

:error2
echo.
echo PLEASE DEFINTION VERSION NUMBER (2.7  and more)
echo.
goto usage

:usage
echo.
echo USAGE: %~nx0 -b          build only
echo			  -B          build bdist_winint
echo			  -t          build bdist_winint and version (2.7 and more)*
echo			  -T          build bdist_winint, version (2.7 and more) then install it
echo			  -r          build and register
echo			  -R          build bdist_wininst and register**
echo			  -j          build, bdist_wininst, register and upload, it must defintion with on .pypirc**
echo			  -a, --all   build, bdist_wininst, register, upload and install(.pypirc)**
echo			  -s,         sdist, register and upload and install(.pypirc)**
echo			  -h, --help  print this help
echo			  -c, --clean clean after all***
echo.
echo EXAMPLE: %~nx0 -a pypi
echo          %~nx0 -t 2.7
echo.
echo NOTE: *    option 2 must be version number
echo       **   option 2 must be repository name and option 3 must be version number
echo       ***  option -c, --clean must be end all of option, it can be option 2, option 3 or option 4
goto fin

:endclean
rm -rf build
goto fin

:end
goto fin

:fin