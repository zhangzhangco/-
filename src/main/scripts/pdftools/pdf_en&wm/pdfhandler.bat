@echo off

for /f %%a in ('dir /b *.pdf') do (
gs.exe -sPDFPassword=jkl;' -sOwnerPassword=jkl;' -sUserPassword=jkl;' -dBATCH -dNOPAUSE -dAutoRotatePages=/None -q  -dFirstPage=1 -dLastPage=4 -sOutputFile="../mediastandards-registry-china/src/site/pdf/%%a" -sDEVICE=pdfwrite  mark.ps %%a)