

class ESCPOS:
    # HEX representation of non alphabetical ESCPOS characters
    esc_hex = {
        'NUL': '00',
        'SOH': '01',
        'STX': '02',
        'ETX': '03',
        'EOT': '04',
        'ENQ': '05',
        'ACK': '06',
        'BEL': '07',
        'BS': '08',
        'TAB': '09',
        'LF': '0A',
        'VT': '0B',
        'FF': '0C',
        'CR': '0D',
        'SO': '0E',
        'SI': '0F',
        'DLE': '10',
        'DC1': '11',
        'DC2': '12',
        'DC3': '13',
        'DC4': '14',
        'NAK': '15',
        'SYN': '16',
        'ETB': '17',
        'CAN': '18',
        'EM': '19',
        'SUB': '1A',
        'ESC': '1B',
        'FS': '1C',
        'GS': '1D',
        'RS': '1E',
        'US': '1F',
        'SP': '20',
        'DEL': '7F'
    }
    # DECIMAL representation of non alphabetical ESCPOS characters
    esc_dec = {
        'NUL': 0,
        'SOH': 1,
        'STX': 2,
        'ETX': 3,
        'EOT': 4,
        'ENQ': 5,
        'ACK': 6,
        'BEL': 7,
        'BS': 8,
        'HT': 9,
        'LF': 10,
        'VT': 11,
        'FF': 12,
        'CR': 13,
        'SO': 14,
        'SI': 15,
        'DLE': 16,
        'DC1': 17,
        'DC2': 18,
        'DC3': 19,
        'DC4': 20,
        'NAK': 21,
        'SYN': 22,
        'ETB': 23,
        'CAN': 24,
        'EM': 25,
        'SUB': 26,
        'ESC': 27,
        'FS': 28,
        'GS': 29,
        'RS': 30,
        'US': 31,
        'SP': 32,
        'DEL': 127
    }
    encode = 'utf-8'

    def encoding(self, enc='utf-8'):
        self.encode = enc
    ''' ESC @ | ESC d n | FF | ESC ff | ...                                 '''
    def ascii_command(self, *args):
        msg = bytearray()
        for i in args:
            if i in self.esc_dec:
                aux = chr(self.esc_dec[i]).encode(self.encode)
            elif isinstance(i, str):
                aux = i.encode(self.encode)
            elif isinstance(i, int):
                aux = chr(i).encode(self.encode)
            else:
                print('Error - {} is non an ASCII character allowed')
                continue
            msg.extend(aux)
        return msg
    ''' 1B 40 | 1B 64 n | 0c | 1B 0C | ...                                  '''
    def hex_command(self, *args):
        msg = bytearray()
        for i in args:
            try:
                msg.extend(bytes.fromhex(i))
            except TypeError:
                print('Error - {} non-string character')
            except ValueError:
                print('Error - {} non-hexadecimal character')
        return msg
    ''' 27 64 | 27 100 n | 12 | 27 12 | ...                                 '''
    def dec_command(self, *args):
        msg = bytearray()
        for i in args:
            if isinstance(i, int):
                try:
                    aux = bytes(chr(i), self.encode)
                except (ValueError, OverflowError):
                    print('Error - {} is too big')
                else:
                    msg.extend(aux)
            else:
                print('Error - {} is not int')
        return msg
    ''' Lorem ipsum ...                                                     '''
    def string_to_escpos(self, txt):
        if isinstance(txt, str):
            return txt.encode(self.encode)
        else:
            print('Error - non-string is given')
