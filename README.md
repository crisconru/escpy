# escpy
Is an implementation of the ESCPOS protocol to use with thermal printer
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
esc_in_bytes = esc.ascii_command('ESC', 'd', 4)
```
2) HEX mode
```
# Ex: 1B 64 04
esc_in_bytes = esc.hex_command('1B', '64', '04')
```
3) DEC mode
```
# Ex: 27 100 4
esc_in_bytes = esc.dec_command(27, 100, 4)
```
You can also transform text with  
```
# Ex: Lorem ipsum ...
esc_in_bytes = esc.string_to_escpos('Lorem ipsum...')
```
