rem run 'where anaconda' and save the resulting path into @ana
@echo off
for /f %%i in ('where anaconda') do set @ana=%%i

rem set p_dir to be a string activating the conda environment
@echo off
set _path=%@ana%
@echo _path
for %%a in ("%_path%") do set "p_dir=%%~dpa"
SET p_dir=%p_dir%activate

rem activate the conda environment
call %p_dir%

rem install virtualenv
call pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org virtualenv

rem create a virtual environment in the code folder
call virtualenv Code\venv

rem activate this new virtual environment
call Code\venv\Scripts\activate

rem if there is an error at this point, don't install anything
if %errorlevel% neq 0 exit

rem install the accompanying requirements file
call pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r Code\requirements.txt

rem install jupyter into the virtual environment
call pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org jupyter

rem install ipython into the virtual environment
call pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org ipython

rem add the virtual environment as a kernel in the local jupyter notebook
call ipython kernel install --user --name=venv

rem leave the window open
cmd /k
