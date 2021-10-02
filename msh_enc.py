import os, struct, json

try:
    os.mkdir("input")
    os.mkdir("output")

    print('The directories have been made.')
    
    input('Insert your msh.ckd files in input and then run the tool again to deserialize them.')
    exit()

except:
    pass

for graphmaterial in os.listdir("input"):
    if graphmaterial.endswith(".msh.ckd"):
        print(graphmaterial)
        with open('input/'+graphmaterial) as m:
            msh=json.load(m)
        header_len=int((22*len(msh))+166)
        graphmsh=open('output/'+graphmaterial,'wb')
        graphmsh.write(b'\x00\x00\x00\x01'+struct.pack('>I',header_len)+b'\xE6\xA9\x35\xE1')
        if msh["__class"]=="GFXMaterialShader_Template":
            graphmsh.write(struct.pack('>I',header_len))
            graphmsh.write(struct.pack('>I',msh["flags"]))
            graphmsh.write(struct.pack('>I',msh["renderRegular"]))
            graphmsh.write(struct.pack('>I',msh["renderFrontLight"]))
            graphmsh.write(struct.pack('>I',msh["renderBackLight"]))
            graphmsh.write(struct.pack('>I',msh["useAlphaTest"]))
            graphmsh.write(struct.pack('>I',msh["alphaRef"]))
            graphmsh.write(struct.pack('>I',msh["separateAlpha"]))
            graphmsh.write(b'\x00\x00\x00\x00')
            graphmsh.write(struct.pack('>I',msh["textureBlend"]))
            graphmsh.write(struct.pack('>I',msh["materialtype"]))
            graphmsh.write(struct.pack('>I',msh["lightingType"]))
            graphmsh.write(b'\x00\x00\x00\x64')#matParams
            graphmsh.write(struct.pack('>I',msh["matParams"]["matParams0F"]))
            graphmsh.write(struct.pack('>I',msh["matParams"]["matParams1F"]))
            graphmsh.write(struct.pack('>I',msh["matParams"]["matParams2F"]))
            graphmsh.write(struct.pack('>I',msh["matParams"]["matParams3F"]))
            graphmsh.write(struct.pack('>I',msh["matParams"]["matParams0I"]))
            graphmsh.write(struct.pack('>I',msh["matParams"]["matParams0VX"]))
            graphmsh.write(struct.pack('>I',msh["matParams"]["matParams0VY"]))
            graphmsh.write(struct.pack('>I',msh["matParams"]["matParams0VZ"]))
            graphmsh.write(struct.pack('>I',msh["matParams"]["matParams0VW"]))
            graphmsh.write(struct.pack('>I',msh["blendmode"]))
            graphmsh.write(b'\x00\x00\x00\x3C')#MaterialLayer
            graphmsh.write(struct.pack('>I',msh["Layer1"]["Enabled"]))
            graphmsh.write(struct.pack('>I',msh["Layer1"]["TexAdressingModeU"]))
            graphmsh.write(struct.pack('>I',msh["Layer1"]["TexAdressingModeV"]))
            graphmsh.write(struct.pack('>I',msh["Layer1"]["Filtering"]))
            diffusecolor1=msh["Layer1"]["DiffuseColor"]
            graphmsh.write(struct.pack('>f',diffusecolor1[0])+struct.pack('>f',diffusecolor1[1])+struct.pack('>f',diffusecolor1[2])+struct.pack('>f',diffusecolor1[3]))
            graphmsh.write(struct.pack('>I',msh["Layer1"]["TextureUsage"]))
            try:
                graphmsh.write(struct.pack('>I',len(msh["Layer1"]["UVModifiers"])))
                for uvmodifier1 in msh["Layer1"]["UVModifiers"]:
                    graphmsh.write(b'\x00\x00\x00\x30')
                    graphmsh.write(struct.pack('>I',uvmodifier1["TranslationU"]))
                    graphmsh.write(struct.pack('>I',uvmodifier1["TranslationV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier1["AnimTranslationU"]))
                    graphmsh.write(struct.pack('>I',uvmodifier1["AnimTranslationV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier1["Rotation"]))
                    graphmsh.write(struct.pack('>f',uvmodifier1["RotationOffsetU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier1["RotationOffsetV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier1["AnimRotation"]))
                    graphmsh.write(struct.pack('>f',uvmodifier1["ScaleU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier1["ScaleV"]))
                    graphmsh.write(struct.pack('>f',uvmodifier1["ScaleOffsetU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier1["ScaleOffsetV"]))
            except:
                graphmsh.write(b'\x00\x00\x00\x00')
            graphmsh.write(struct.pack('>I',msh["BlendLayer2"]))
            graphmsh.write(b'\x00\x00\x00\x3C')#MaterialLayer
            graphmsh.write(struct.pack('>I',msh["Layer2"]["Enabled"]))
            graphmsh.write(struct.pack('>I',msh["Layer2"]["TexAdressingModeU"]))
            graphmsh.write(struct.pack('>I',msh["Layer2"]["TexAdressingModeV"]))
            graphmsh.write(struct.pack('>I',msh["Layer2"]["Filtering"]))
            diffusecolor2=msh["Layer2"]["DiffuseColor"]
            graphmsh.write(struct.pack('>f',diffusecolor2[0])+struct.pack('>f',diffusecolor2[1])+struct.pack('>f',diffusecolor2[2])+struct.pack('>f',diffusecolor2[3]))
            graphmsh.write(struct.pack('>I',msh["Layer2"]["TextureUsage"]))
            try:
                graphmsh.write(struct.pack('>I',len(msh["Layer2"]["UVModifiers"])))
                for uvmodifier2 in msh["Layer2"]["UVModifiers"]:
                    graphmsh.write(b'\x00\x00\x00\x30')
                    graphmsh.write(struct.pack('>I',uvmodifier2["TranslationU"]))
                    graphmsh.write(struct.pack('>I',uvmodifier2["TranslationV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier2["AnimTranslationU"]))
                    graphmsh.write(struct.pack('>I',uvmodifier2["AnimTranslationV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier2["Rotation"]))
                    graphmsh.write(struct.pack('>f',uvmodifier2["RotationOffsetU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier2["RotationOffsetV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier2["AnimRotation"]))
                    graphmsh.write(struct.pack('>f',uvmodifier2["ScaleU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier2["ScaleV"]))
                    graphmsh.write(struct.pack('>f',uvmodifier2["ScaleOffsetU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier2["ScaleOffsetV"]))
            except:
                graphmsh.write(b'\x00\x00\x00\x00')
            graphmsh.write(struct.pack('>I',msh["BlendLayer3"]))
            graphmsh.write(b'\x00\x00\x00\x3C')#MaterialLayer
            graphmsh.write(struct.pack('>I',msh["Layer3"]["Enabled"]))
            graphmsh.write(struct.pack('>I',msh["Layer3"]["TexAdressingModeU"]))
            graphmsh.write(struct.pack('>I',msh["Layer3"]["TexAdressingModeV"]))
            graphmsh.write(struct.pack('>I',msh["Layer3"]["Filtering"]))
            diffusecolor3=msh["Layer3"]["DiffuseColor"]
            graphmsh.write(struct.pack('>f',diffusecolor3[0])+struct.pack('>f',diffusecolor3[1])+struct.pack('>f',diffusecolor3[2])+struct.pack('>f',diffusecolor3[3]))
            graphmsh.write(struct.pack('>I',msh["Layer3"]["TextureUsage"]))
            try:
                graphmsh.write(struct.pack('>I',len(msh["Layer3"]["UVModifiers"])))
                for uvmodifier3 in msh["Layer3"]["UVModifiers"]:
                    graphmsh.write(b'\x00\x00\x00\x30')
                    graphmsh.write(struct.pack('>I',uvmodifier3["TranslationU"]))
                    graphmsh.write(struct.pack('>I',uvmodifier3["TranslationV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier3["AnimTranslationU"]))
                    graphmsh.write(struct.pack('>I',uvmodifier3["AnimTranslationV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier3["Rotation"]))
                    graphmsh.write(struct.pack('>f',uvmodifier3["RotationOffsetU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier3["RotationOffsetV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier3["AnimRotation"]))
                    graphmsh.write(struct.pack('>f',uvmodifier3["ScaleU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier3["ScaleV"]))
                    graphmsh.write(struct.pack('>f',uvmodifier3["ScaleOffsetU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier3["ScaleOffsetV"]))
            except:
                graphmsh.write(b'\x00\x00\x00\x00')
            graphmsh.write(struct.pack('>I',msh["BlendLayer4"]))
            graphmsh.write(b'\x00\x00\x00\x3C')#MaterialLayer
            graphmsh.write(struct.pack('>I',msh["Layer4"]["Enabled"]))
            graphmsh.write(struct.pack('>I',msh["Layer4"]["TexAdressingModeU"]))
            graphmsh.write(struct.pack('>I',msh["Layer4"]["TexAdressingModeV"]))
            graphmsh.write(struct.pack('>I',msh["Layer4"]["Filtering"]))
            diffusecolor4=msh["Layer4"]["DiffuseColor"]
            graphmsh.write(struct.pack('>f',diffusecolor4[0])+struct.pack('>f',diffusecolor4[1])+struct.pack('>f',diffusecolor4[2])+struct.pack('>f',diffusecolor4[3]))
            graphmsh.write(struct.pack('>I',msh["Layer4"]["TextureUsage"]))
            try:
                graphmsh.write(struct.pack('>I',len(msh["Layer4"]["UVModifiers"])))
                for uvmodifier4 in msh["Layer4"]["UVModifiers"]:
                    graphmsh.write(b'\x00\x00\x00\x30')
                    graphmsh.write(struct.pack('>I',uvmodifier4["TranslationU"]))
                    graphmsh.write(struct.pack('>I',uvmodifier4["TranslationV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier4["AnimTranslationU"]))
                    graphmsh.write(struct.pack('>I',uvmodifier4["AnimTranslationV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier4["Rotation"]))
                    graphmsh.write(struct.pack('>f',uvmodifier4["RotationOffsetU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier4["RotationOffsetV"]))
                    graphmsh.write(struct.pack('>I',uvmodifier4["AnimRotation"]))
                    graphmsh.write(struct.pack('>f',uvmodifier4["ScaleU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier4["ScaleV"]))
                    graphmsh.write(struct.pack('>f',uvmodifier4["ScaleOffsetU"]))
                    graphmsh.write(struct.pack('>f',uvmodifier4["ScaleOffsetV"]))
            except:
                graphmsh.write(b'\x00\x00\x00\x00')

        graphmsh.close()