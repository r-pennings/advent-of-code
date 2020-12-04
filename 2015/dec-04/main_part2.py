import hashlib
import time

start_time = time.time()

input_string = 'iwrupvqb'

def find_md5_hash(zeros):
    num = 0
    while True:
        num += 1
        hash = hashlib.md5((input_string + str(num)).encode()).hexdigest()
        if hash.startswith('0' * zeros):
            break
    return num

print("Index", find_md5_hash(6))
print("Execution time: %s seconds" % (time.time() - start_time))