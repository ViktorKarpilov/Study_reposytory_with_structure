@echo off
rem set /p PathToPSCyr=Enter PSCyr folder name:

mkdir fonts\enc\dvips\pscyr
mkdir fonts\map\dvips\pscyr
copy pscyr\dvips\pscyr\t2a.enc fonts\enc\dvips\pscyr\
copy pscyr\dvips\pscyr\pscyr.map fonts\map\dvips\pscyr\
mkdir tex\latex\pscyr
copy  pscyr\tex\latex\pscyr tex\latex\pscyr\
xcopy /E pscyr\dvipdfm dvipdfm\
xcopy /E pscyr\fonts fonts\

echo # pscyr >> miktex\config\updmap.cfg
echo Map pscyr.map >> miktex\config\updmap.cfg
rmdir pscyr

miktex\bin\mktexlsr
miktex\bin\updmap
