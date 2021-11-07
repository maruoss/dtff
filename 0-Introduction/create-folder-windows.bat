:: A script that sets an environment variable and creates a user-specified
:: folder in it.

:: Turn off display
@echo off

:: Set temporary environment variable
@REM set RESEARCH_PATH=C:\Users\Mathiass\Documents\Projects


@REM IF DEFINED RESEARCH_PATH (echo RESEARCH_PATH exists) else (echo RESEARCH_PATH does not exist. Will use default path.)
@REM IF not DEFINED RESEARCH_PATH set RESEARCH_PATH=C:\Users\Mathiass\Documents\Projects

@REM :: Go to (windows) environment variable directory
@REM cd %RESEARCH_PATH%

@REM :: Prompt name from user
@REM set /p folder_name="Enter folder name: "

@REM :: Create folder with entered folder name
@REM md %folder_name%


:: Gives syntax error. Cannot save set /p foldername to variable, so mkdir doesnt recognize %foldername% on the same line
@REM IF DEFINED RESEARCH_PATH (
@REM echo RESEARCH_PATH exists & cd %RESEARCH_PATH% & set /p foldername="How do you want to name your folder? "  & echo %foldername% & mkdir %foldername%
@REM ) else (
@REM     echo RESEARCH_PATH does not exist. Abort.
@REM )

:: The below works fine. (Preferebly on cmd prompt, not Powershell)
IF DEFINED RESEARCH_PATH (
echo RESEARCH_PATH exists & cd %RESEARCH_PATH% & set /p foldername="How do you want to name your folder? "
) else (
    echo RESEARCH_PATH does not exist. Abort.
)

IF DEFINED RESEARCH_PATH (
echo Creating folder %foldername% in %RESEARCH_PATH% & mkdir %foldername%
) else (
    echo RESEARCH_PATH still does not exist. Abort.
)