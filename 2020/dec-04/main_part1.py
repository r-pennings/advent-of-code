class Passport:
    def __init__(self, passport):
        self.byr = passport['byr'] if 'byr' in passport else ""
        self.iyr = passport['iyr'] if 'iyr' in passport else ""
        self.eyr = passport['eyr'] if 'eyr' in passport else ""
        self.hgt = passport['hgt'] if 'hgt' in passport else ""
        self.hcl = passport['hcl'] if 'hcl' in passport else ""
        self.ecl = passport['ecl'] if 'ecl' in passport else ""
        self.pid = passport['pid'] if 'pid' in passport else ""
        self.cid = passport['cid'] if 'cid' in passport else ""

    def is_valid(self):
        for item in vars(self):
            if not getattr(self, item) and item != 'cid':
                return False
        return True


def process(lines):
    passports = []
    obj = {}
    for line in lines.split('\n'):
        if line == '':
            passports.append(Passport(obj))
            obj = {}
        else:
            for item in line.strip().split(' '):
                key, value = item.split(':')
                obj[key] = value

    # Add the last passport (because it has no \n after it)
    passports.append(Passport(obj))
    return passports


with open("input.txt") as f:
    passports = process(f.read())

valid_passports = [passport for passport in passports if passport.is_valid()]
print("# of valid passports", len(valid_passports))
