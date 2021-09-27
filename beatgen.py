import os, json

#function
def beatconvert(value):
    return value*48

#inputs
codename = input("Input your mapname: ")
codenamelow = codename.lower()
bpm=float(input("Input the BPM: "))
math=round(60000/bpm)
generatedbeats=0
beatamount=int(input("How many beats do you want: "))

musictrack={}
musictrack["__class"]="Actor_Template"
musictrack["WIP"]=0
musictrack["LOWUPDATE"]=0
musictrack["UPDATE_LAYER"]=0
musictrack["PROCEDURAL"]=0
musictrack["STARTPAUSED"]=0
musictrack["FORCEISENVIRONMENT"]=0
beats=[]
signaturetape={
"__class": "MusicSignature",
"marker": 8,
"beats": 4}
sectiontape={
"__class": "MusicSection",
"marker": 16,
"sectionType": 8,
"comment": ""
}
signatureclip=[signaturetape]
sectionclip=[sectiontape]

#generate beats
while generatedbeats<=beatamount:
    convertbeat=beatconvert(math*generatedbeats)
    beats.append(convertbeat)
    print(convertbeat)
    generatedbeats+=1

#end of musictrack
structure={}
structure["__class"]="MusicTrackStructure"
structure["markers"]=beats
structure["signatures"]=signatureclip
structure["sections"]=sectionclip
structure["startBeat"]=0
structure["endBeat"]=len(beats)
structure["videoStartTime"]=0
structure["previewEntry"]=round(len(beats)/4)
structure["previewLoopStart"]=round(len(beats)/3)
structure["previewLoopEnd"]=round(len(beats)/2)
structure["volume"]=0

mtdata={}
mtdata["__class"]="MusicTrackData"
mtdata["structure"]=structure
mtdata["path"]="world/maps/"+codenamelow+"/audio/"+codenamelow+".wav"
mtdata["url"]="jmcs://jd-contents/"+codename+"/"+codename+".ogg"

mttemplate={}

mttemplate["__class"]="MusicTrackComponent_Template"
mttemplate["trackData"]=mtdata

components=[mttemplate]

musictrack["COMPONENTS"]=components

try:
    os.mkdir("output")

except:
    pass

json.dump(musictrack,open("output/"+codenamelow+"_musictrack.tpl.ckd","w"))