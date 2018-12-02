fH = open("category.dat")
scdb = []
for line in fH:
    dat = line.strip()
    category = dat.split("\n")
    record={}
    for attr in category:
        kv = attr.split(":")
        record[kv[0]] = kv[1]
        scdb+=[record]

print(scdb[1])

e = scdb[1]
print(e['japanese'])