import hashlib
idx = 0
while True:
    idx += 1
    m = hashlib.sha256()
    m.update(("to hash %s" % idx).encode('utf8'))
    m.digest()
    if idx > 100000:
        idx = 0

