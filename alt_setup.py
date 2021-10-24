import json, struct
from unidecode import unidecode

with open('alt_stuff.json','rb') as alt:
    altcontent=json.load(alt)
    
altcount=struct.pack(">I",len(altcontent["ALTMAP"]))

for alt in altcontent["ALTMAP"]:
    altmapname=unidecode(alt["MapName"])
    altcount+=struct.pack('>I',len(altmapname))+altmapname.encode()+b'\x00\x00\x00\x04\xFF\xFF\xFF\xFF'+struct.pack('>I',alt["LocaleId"])+b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF'
    print(alt["MapName"]+' - '+str(alt["LocaleId"]))

with open('alt.ckd','wb') as g:
    g.write(altcount)
    g.close()

print('modify gameconfig.isg.ckd where the list of alt codenames are listed.')
input()