f1 = open("file9","r")
f2 = open("file0","r")
f3 = open("undertale.ini","r")
final = open("undertale.sav","w")
        
def add(f,final):
    for i in f:
        i = i.replace("\n", "")
        i = i.replace(" ", "")
        final.write(i + '\\r')
        break

    for i in f:
        i = i.replace("\n", "")
        i = i.replace(" ", "")
        final.write('\\n'+ i + '\\r')
    size=final.tell()             
    final.truncate(size-2)
    final.seek(size-2,0)
    final.write('"')

final.write('{ "default": "", "file9": "')

add(f1,final)

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
        final.write('\\n'+ r[0] + '=\\"' + p + '\\"' + '\\r')
        
final.write('\\n", "file0": "')
add(f2,final)
final.write(chr(32) + chr(125) + chr(0))

f1.close()
f2.close()
f3.close()
final.close()
