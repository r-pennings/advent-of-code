# t1 = timestamp
# t2 = timestamp + 1
# etc.

def find_bus(current_time, bus_ids, index=0):
    print(current_time, index)
    while index < len(bus_ids):
        if (current_time + index) % int(bus_ids[index]) > 0:
            return False

        find_bus(current_time, bus_ids, index+1)
    return True

lines = [line for line in open("input.txt")]

bus_id = 0
current_time = start_time = int(lines[0])
bus_ids = [int(bus_id) for bus_id in lines[1].split(",") if bus_id.isdigit()]
while bus_id == 0:
    current_time += 1

    if find_bus(current_time, bus_ids):
        break

print("Minutes", bus_id * (current_time - start_time))
