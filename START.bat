@echo off
chcp 65001 >nul
title GDH - Global Distribution Holdings (server local)
echo.
echo  ========================================
echo   GDH - server local pentru folderul dist
echo  ========================================
echo.
echo  Deschide in browser: http://localhost:8752
echo  Ctrl+C opreste serverul.
echo.

cd /d "%~dp0"
start "" "http://localhost:8752"
python -m http.server 8752 --directory dist
