@echo off
setlocal
rem 入力ファイルと出力ファイルのパスを設定
set INPUT_FILE=.\in\0001.txt
set OUTPUT_FILE=.\out\0001.txt

rem Pythonスクリプトを実行し、標準入力と標準出力をファイルから行う
python .\A.py < %INPUT_FILE% > %OUTPUT_FILE%

endlocal
