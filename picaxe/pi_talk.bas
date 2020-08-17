
init:
 hi2csetup i2cslave, %10100000 
 
main:

;read pot values
readadc 1,b1
readadc 2, b2
readadc 4, b3
readadc 5, b4

;for push buttons
if pinC.7 = 1 then let b5=1
ELSE let b5=0
ENDIF 
if pinC.6 = 1 then let b6=1
ELSE let b6=0
ENDIF 
if pinC.5 = 1 then let b7=1
ELSE let b7=0
ENDIF 
if pinC.4 = 1 then let b8=1
ELSE let b8=0
ENDIF 
if pinC.3 = 1 then let b9=1
ELSE let b9=0
ENDIF 
if pinC.2 = 1 then let b10=1
ELSE let b10=0
ENDIF 

;put into internal memory
put 1, b1
put 2, b2
put 3, b3
put 4, b4

put 5, b5 
put 6, b6
put 7, b7 
put 8, b8 
put 9, b9
put 10, b10  

pause 50
;debug
goto main
