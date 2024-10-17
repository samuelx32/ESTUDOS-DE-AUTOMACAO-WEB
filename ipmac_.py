import uuid

def get_mac_address():
    mac = hex(uuid.getnode()).replace('0x', '').upper()
    mac_address = '-'.join(mac[i:i+2] for i in range(0, 12, 2))
    return mac_address



meu_mac = ""

if meu_mac == str(get_mac_address()):
    print("Liberado")
else:
    print("Não Autorizado")
