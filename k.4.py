with open("taskfile.dat", encoding="utf-8") as f:
    lines = f.readlines()

    k = 0
    n = 0
    for i in lines:
        d = lines.split
        for l in d:
            if '1' in d:
                k += 1
            if k > 6:
                n += 1
with open("output.dat", 'w', encoding="utf-8") as g:
    g.write(n)