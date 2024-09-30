import pymem

def get_pointer_value(pm, base_address, offsets):
    """Segue a cadeia de ponteiros corretamente e retorna o endereço final"""
    address = pm.read_longlong(base_address)
    print(f"  Base address: {hex(base_address)}, Initial address: {hex(address)}")
    for i, offset in enumerate(offsets[:-1]):
        try:
            new_address = pm.read_longlong(address + offset)
            print(f"  Offset {i}: {hex(offset)}, Address: {hex(address + offset)}, Value: {hex(new_address)}")
            address = new_address
        except Exception as e:
            print(f"  Error at offset {i}: {hex(offset)}, Address: {hex(address + offset)}, Error: {str(e)}")
            return None
    final_address = address + offsets[-1]
    print(f"  Final offset: {hex(offsets[-1])}, Final address: {hex(final_address)}")
    return final_address

def monitor_pointers():
    print("HYDRA PHOENIX COLLECTOR MEMORY MONITOR")
    
    process_name = 'PathOfExile.exe'
    pm = pymem.Pymem(process_name)
    pid = pm.process_id
    print(f"Connecting \"{process_name}\" {pid}")
    
    pointers = [
        {'base_address': pm.base_address + 0x0308AB70, 'offsets': [0x8, 0x18, 0x238, 0x168, 0x8]},
        {'base_address': pm.base_address + 0x03450B70, 'offsets': [0x8, 0xC8, 0x28, 0x138, 0x238, 0x168, 0x18]},
        {'base_address': pm.base_address + 0x0308ABA8, 'offsets': [0x28, 0x18, 0x28, 0x238, 0x168, 0x28]},
        {'base_address': pm.base_address + 0x0308AB38, 'offsets': [0x8, 0x18, 0x238, 0x168, 0x38]},
        {'base_address': pm.base_address + 0x0308AB70, 'offsets': [0x38, 0x18, 0x2B8, 0xE8, 0x48]},
        {'base_address': pm.base_address + 0x0308AB38, 'offsets': [0x8, 0x18, 0x2B8, 0xD0, 0x8]},
        {'base_address': pm.base_address + 0x0308ABA8, 'offsets': [0x38, 0x18, 0x2B8, 0xD0, 0x18]},
        {'base_address': pm.base_address + 0x0308ABE0, 'offsets': [0x58, 0x18, 0x2B8, 0xD0, 0x28]},
        {'base_address': pm.base_address + 0x0308AB70, 'offsets': [0x28, 0x18, 0x2B8, 0xD0, 0x38]},
        {'base_address': pm.base_address + 0x0308ABA8, 'offsets': [0x38, 0x18, 0x238, 0x150, 0x48]},
    ]
    
    for i, pointer in enumerate(pointers, 1):
        print(f"\nPointer {i}")
        final_address = get_pointer_value(pm, pointer['base_address'], pointer['offsets'])
        if final_address is None:
            print(f"  Could not resolve pointer {i}")
            continue
        
        try:
            stock = pm.read_int(final_address)
            price_base = pm.read_short(final_address - 8)
            price_base_2 = pm.read_short(final_address - 6)
            
            print(f"  STOCK: {stock}")
            print(f"  Price Base: {price_base}")
            print(f"  Price Base 2: {price_base_2}")
        
            if 1 <= i <= 5:
                if price_base_2 != 0:  
                    price = price_base / price_base_2
                    value_to_move = stock / price
                    print(f"Price: {price}")
                    print(f"Value to move: {value_to_move}")
                else:
                    print("Price: Division by zero")
                    print("Value to move: Not calculated due to division by zero")
            elif 6 <= i <= 10:
                if price_base != 0:  
                    price = price_base_2 / price_base
                    value_to_move = price_base_2 * stock
                    print(f"Price: {price}")
                    print(f"Value to move: {value_to_move}")
                else:
                    print("Price: Division by zero")
                    print("Value to move: Not calculated due to division by zero")
        
        except Exception as e:
            print(f"  Error reading values: {str(e)}")

if __name__ == "__main__":
    monitor_pointers()
