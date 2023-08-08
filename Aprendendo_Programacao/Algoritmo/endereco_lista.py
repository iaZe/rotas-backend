import array

def get_memory_addresses_list(lst):
    addresses = []
    for item in lst:
        address = id(item)
        addresses.append(address)
    return addresses

def get_memory_addresses_array(arr):
    addresses = []
    for item in arr:
        address = id(item)
        addresses.append(address)
    return addresses

my_list = ['1', '2', '3', '4', '5']
memory_addresses_list = get_memory_addresses_list(my_list)
print(memory_addresses_list)

my_array = array.array('i', [1, 2, 3, 4, 5])
memory_addresses_array = get_memory_addresses_array(my_array)
print(memory_addresses_array)