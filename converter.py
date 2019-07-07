def add(f, final):
    for i in f:
        i = i.replace("\n", "")
        i = i.replace(" ", "")
        final.write(i + '\\r')
        break

    for i in f:
        i = i.replace("\n", "")
        i = i.replace(" ", "")
        final.write('\\n' + i + '\\r')
        size = final.tell()
        final.truncate(size-2)
        final.seek(size-2, 0)
        final.write('"')


def add2(file, file2):
    while True:
        char = file2.read(1)
        if not char:
            break
        if char == "\\":
            while file2.read(1) != "n":
                pass
            file.write("\n")
        elif char == '"':
            break
        else:
            file.write(char)

    file.close()


def pc_to_switch():
    f1 = open("file9", "r")
    f2 = open("file0", "r")
    f3 = open("undertale.ini", "r")
    final = open("undertale.sav", "w")

    final.write('{ "default": "", "file9": "')

    add(f1, final)

    final.write(', "config.ini": "", "undertale.ini": "')
    for i in f3:
        i = i.replace("\n", "")
        i = i.replace(" ", "")
        if i.startswith("["):
            final.write(i + '\\r')
        else:
            r = i.split("=")
            p = r[1].split('"')
            p = p[1]
            final.write('\\n' + r[0] + '=\\"' + p + '\\"' + '\\r')

    final.write('\\n", "file0": "')
    add(f2, final)
    final.write(chr(32) + chr(125) + chr(0))

    f1.close()
    f2.close()
    f3.close()
    final.close()


def switch_to_pc():
    f = open("file9", "w+")
    f2 = open("undertale.sav", "r")
    f2.seek(27)
    f3 = open("undertale.ini", "w+")
    f4 = open("file0", "w+")

    add2(f, f2)

    f2.seek(f2.tell() + 38)

    while True:
        char = f2.read(1)
        if not char:
            break
        if char == "\\":
            n = f2.read(1)
            if n != '"':
                while f2.read(1) != "n":
                    pass
                f3.write("\n")
            else:
                f3.write('"')

        elif char == ",":
            size = f3.tell()
            f3.truncate(size-1)
            f3.seek(size-1, 0)
            break
        else:
            f3.write(char)

    f3.close()

    f2.seek(f2.tell() + 11)

    add2(f4, f2)


print("Undertale-Save-Converter")
print("1) Pc to Switch")
print("2) Switch to PC")
selection = input("> ")

if selection == 1:
    pc_to_switch()
elif selection == 2:
    switch_to_pc()
