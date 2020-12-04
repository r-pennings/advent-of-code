class Orbit:
    def __init__(self, name):
        self.name = name
        self.orbit = None
        self.indirects = []

    def set_orbit(self, orbit):
        self.orbit = orbit

    def add_indirect(self, orbit):
        self.indirects.append(orbit)


def get_data(_file):
    orbits = {}
    for line in _file:
        orbit, name = line.strip().split(')')
        if orbit not in orbits:
            orbits[orbit] = Orbit(orbit)
        if name not in orbits:
            orbits[name] = Orbit(name)
        orbits[name].set_orbit(orbits[orbit])
    return orbits


with open("input.txt") as f:
    orbits = get_data(f)

total = 0
for orbit in orbits.values():
    if orbit.orbit is not None:
        total += 1

        current_orb = orbit.orbit
        while current_orb.orbit is not None:
            orbit.add_indirect(current_orb)
            total += 1
            current_orb = current_orb.orbit

san_indirects = [o.name for o in orbits.get('SAN').indirects]
you_indirects = [o.name for o in orbits.get('YOU').indirects]

intersections = set(san_indirects).intersection(set(you_indirects))

indices_san = [san_indirects.index(x) for x in intersections]
indices_you = [you_indirects.index(x) for x in intersections]

shortest_path = min(indices_san) + min(indices_you)
print("shortest path", shortest_path)
