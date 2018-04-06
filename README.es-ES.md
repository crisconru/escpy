# escpy
Es una implementación del protocolo ESCPOS para usar con impresoras térmicas.
## Modo de uso
Primero de todo debes import el módulo.  
```
from escpos import ESCPOS
esc = ESCPOS()
```
Luego tienes 3 opciones diferentes para enviar comandos ESCPOS. En el ejemplo vamos a mandar el mismo comando, imprimir lo que haya en el buffer de entrada y luego 4 saltos de linea.  
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
También puedes transformar un texto normal a bytes para poder ser enviado.  
```
# Ex: Lorem ipsum ...
esc_in_bytes = esc.string_to_escpos('Lorem ipsum...')
```

