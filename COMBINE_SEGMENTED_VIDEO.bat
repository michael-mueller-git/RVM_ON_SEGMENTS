@echo off
if "%~1" == "" (
    echo Drag and drop a folder containing segmented video files onto this batch file to combine them into one.
    pause
    exit /b
)

set input_folder=%~1
set output_file=output_combined.mp4

ffmpeg -f concat -safe 0 -i "%input_folder%\file_list.txt" -c copy "%output_file%"

echo Segmented videos have been combined into "%output_file%".
pause
