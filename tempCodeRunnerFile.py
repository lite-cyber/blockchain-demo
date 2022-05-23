import hashlib
filename = input("Enter the file name for md5 hash generation: ")
with open(filename,"rb") as f:
    bytes = f.read() # read file as bytes
    readable_hash = hashlib.md5(bytes).hexdigest()
    print(readable_hash)
    hashobject = open('uploadhash.txt', 'w')
    hashobject.write(readable_hash)
    hashobject.close()