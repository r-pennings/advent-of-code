class Orbit:
    def __init__(self, name):
        self.name = name
        self.orbit = None
        self.indirects = 0

    def set_orbit(self, orbit):
        self.orbit = orbit

    def add_indirect(self):
        self.indirects += 1


def get_data(data):
    orbits = {}
    for line in data:
        inner, outer = line.strip().split(')')
        if inner not in orbits:
            orbits[inner] = Orbit(inner)
        if outer not in orbits:
            orbits[outer] = Orbit(outer)
        orbits[outer].set_orbit(orbits[inner])
    return orbits


with open("input.txt") as f:
    orbits = get_data(f)

total = 0
for orbit in orbits.values():
    if orbit.orbit is not None:
        total += 1

        current_orb = orbit.orbit
        while current_orb.orbit is not None:
            orbit.add_indirect()
            total += 1
            current_orb = current_orb.orbit

print("# of orbits", total)
