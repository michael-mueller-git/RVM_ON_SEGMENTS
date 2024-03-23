@echo off
if "%~1" == "" (
    echo Drag and drop a video file onto this batch file to split it into 1-minute segments.
    pause
    exit /b
)

set /p time="Time in seconds per segment:"

set input_file=%~1
set output_folder=%~dpn1_segments
\

mkdir "%output_folder%"

ffmpeg -i "%input_file%" -c copy -f segment -segment_time "%time%" -reset_timestamps 1 "%output_folder%\output_%%03d.mp4"

cd "%output_folder%"
(for %%i in (*.mp4) do @echo file '%%i') > file_list.txt

echo Video has been split into 1-minute segments.
pause