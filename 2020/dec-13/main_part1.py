lines = [line for line in open("input.txt")]

bus_id = 0
current_time = start_time = int(lines[0])
bus_ids = [int(bus_id) for bus_id in lines[1].split(",") if bus_id.isdigit()]
while bus_id == 0:
    current_time += 1
    for bus in bus_ids:
        if current_time % bus == 0:
            bus_id = bus
            break

print("Minutes", bus_id * (current_time - start_time))
