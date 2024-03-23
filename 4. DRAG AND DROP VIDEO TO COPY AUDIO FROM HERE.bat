@echo off
echo === Merge Audio from MP4 Files ===
echo.

set input1=COMPOSITE_SEGMENTS_COMBINED.mp4
set input2=%~1

if "%input2%"=="" (
    echo No file was dropped. Exiting...
    pause
    exit /b
)

rem Extracting file name and extension of the dropped file
for %%I in ("%input2%") do (
    set "filename=%%~nI"
    set "extension=%%~xI"
)

set output=%filename%_MATTED.mp4

ffmpeg -i "%input1%" -i "%input2%" -c copy -map 0:v:0 -map 1:a:0 "%output%"

echo.
echo Output file "%output%" has been created.
pause
