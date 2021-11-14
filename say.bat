@echo off
echo Dim Speak >> %HOMEDRIVE%%HOMEPATH%\speak.vbs
echo Set Speak=CreateObject("sapi.spvoice") >> %HOMEDRIVE%%HOMEPATH%\speak.vbs
echo Speak.Speak "%*">> %HOMEDRIVE%%HOMEPATH%\speak.vbs
%HOMEDRIVE%%HOMEPATH%\speak.vbs
del %HOMEDRIVE%%HOMEPATH%\speak.vbs