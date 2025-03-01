@echo off
for /f "tokens=1,* delims= " %%A in (for_analysis.txt) do (
    python3 analysis.py %%A %%B
)