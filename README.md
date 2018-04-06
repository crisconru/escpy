# escpy
Is and implementation of the ESCPOS protocol to use with thermal printer
## Usage
First of all you should import the module  
```
from escpos import ESCPOS
esc = ESCPOS()
```
Then you have 3 different option to send an ESCPOS command. We are going to send the same command, print the text in buffer and then 4 feed lines  
1) ASCII mode
```
# Ex: ESC d 4
esc.ascii_command('ESC', 'd', 'n')
```
2)