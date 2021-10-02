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
        m=open("input/"+graphmaterial,"rb")
        m.read(12)
        material={}
        material["__class"]="GFXMaterialShader_Template"
        m.read(4)#GFXMaterialShader_Template
        material["flags"]=struct.unpack('>I',m.read(4))[0]
        material["renderRegular"]=struct.unpack('>I',m.read(4))[0]
        material["renderFrontLight"]=struct.unpack('>I',m.read(4))[0]
        material["renderBackLight"]=struct.unpack('>I',m.read(4))[0]
        material["useAlphaTest"]=struct.unpack('>I',m.read(4))[0]
        material["alphaRef"]=struct.unpack('>I',m.read(4))[0]
        material["separateAlpha"]=struct.unpack('>I',m.read(4))[0]
        m.read(4)
        material["textureBlend"]=struct.unpack('>I',m.read(4))[0]
        material["materialtype"]=struct.unpack('>I',m.read(4))[0]
        material["lightingType"]=struct.unpack('>I',m.read(4))[0]
        m.read(4)#matParams
        matparams={}
        matparams["matParams0F"]=struct.unpack('>I',m.read(4))[0]
        matparams["matParams1F"]=struct.unpack('>I',m.read(4))[0]
        matparams["matParams2F"]=struct.unpack('>I',m.read(4))[0]
        matparams["matParams3F"]=struct.unpack('>I',m.read(4))[0]
        matparams["matParams0I"]=struct.unpack('>I',m.read(4))[0]
        matparams["matParams0VX"]=struct.unpack('>I',m.read(4))[0]
        matparams["matParams0VY"]=struct.unpack('>I',m.read(4))[0]
        matparams["matParams0VZ"]=struct.unpack('>I',m.read(4))[0]
        matparams["matParams0VW"]=struct.unpack('>I',m.read(4))[0]
        material["matParams"]=matparams
        material["blendmode"]=struct.unpack('>I',m.read(4))[0]
        m.read(4)#MaterialLayer
        layer1={}
        layer1["__class"]="MaterialLayer"
        layer1["Enabled"]=struct.unpack('>I',m.read(4))[0]
        layer1["AlphaThreshold"]=-1
        layer1["TexAdressingModeU"]=struct.unpack('>I',m.read(4))[0]
        layer1["TexAdressingModeV"]=struct.unpack('>I',m.read(4))[0]
        layer1["Filtering"]=struct.unpack('>I',m.read(4))[0]
        layer1["DiffuseColor"]=[struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0]]
        layer1["TextureUsage"]=struct.unpack('>I',m.read(4))[0]
        uvmodifier=struct.unpack('>I',m.read(4))[0]
        for x in range(uvmodifier):
            uvmodifier1={}
            uvmodifier1["__class"]="UVModifier"
            m.read(4)
            uvmodifier1["TranslationU"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier1["TranslationV"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier1["AnimTranslationU"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier1["AnimTranslationV"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier1["Rotation"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier1["RotationOffsetU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier1["RotationOffsetV"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier1["AnimRotation"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier1["ScaleU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier1["ScaleV"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier1["ScaleOffsetU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier1["ScaleOffsetV"]=struct.unpack('>f',m.read(4))[0]
            layer1["UVModifiers"]=[uvmodifier1]
        material["Layer1"]=layer1
        material["BlendLayer2"]=struct.unpack('>I',m.read(4))[0]
        m.read(4)#MaterialLayer
        layer2={}
        layer2["__class"]="MaterialLayer"
        layer2["Enabled"]=struct.unpack('>I',m.read(4))[0]
        layer2["AlphaThreshold"]=-1
        layer2["TexAdressingModeU"]=struct.unpack('>I',m.read(4))[0]
        layer2["TexAdressingModeV"]=struct.unpack('>I',m.read(4))[0]
        layer2["Filtering"]=struct.unpack('>I',m.read(4))[0]
        layer2["DiffuseColor"]=[struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0]]
        layer2["TextureUsage"]=struct.unpack('>I',m.read(4))[0]
        uvmodifier=struct.unpack('>I',m.read(4))[0]
        for x in range(uvmodifier):
            uvmodifier2={}
            uvmodifier2["__class"]="UVModifier"
            m.read(4)
            uvmodifier2["TranslationU"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier2["TranslationV"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier2["AnimTranslationU"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier2["AnimTranslationV"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier2["Rotation"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier2["RotationOffsetU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier2["RotationOffsetV"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier2["AnimRotation"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier2["ScaleU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier2["ScaleV"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier2["ScaleOffsetU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier2["ScaleOffsetV"]=struct.unpack('>f',m.read(4))[0]
            layer2["UVModifiers"]=[uvmodifier2]
        material["Layer2"]=layer2
        material["BlendLayer3"]=struct.unpack('>I',m.read(4))[0]
        m.read(4)#MaterialLayer
        layer3={}
        layer3["__class"]="MaterialLayer"
        layer3["Enabled"]=struct.unpack('>I',m.read(4))[0]
        layer3["AlphaThreshold"]=-1
        layer3["TexAdressingModeU"]=struct.unpack('>I',m.read(4))[0]
        layer3["TexAdressingModeV"]=struct.unpack('>I',m.read(4))[0]
        layer3["Filtering"]=struct.unpack('>I',m.read(4))[0]
        layer3["DiffuseColor"]=[struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0]]
        layer3["TextureUsage"]=struct.unpack('>I',m.read(4))[0]
        uvmodifier=struct.unpack('>I',m.read(4))[0]
        for x in range(uvmodifier):
            uvmodifier3={}
            uvmodifier3["__class"]="UVModifier"
            m.read(4)
            uvmodifier3["TranslationU"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier3["TranslationV"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier3["AnimTranslationU"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier3["AnimTranslationV"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier3["Rotation"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier3["RotationOffsetU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier3["RotationOffsetV"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier3["AnimRotation"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier3["ScaleU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier3["ScaleV"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier3["ScaleOffsetU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier3["ScaleOffsetV"]=struct.unpack('>f',m.read(4))[0]
            layer3["UVModifiers"]=[uvmodifier3]
        material["Layer3"]=layer3
        material["BlendLayer4"]=struct.unpack('>I',m.read(4))[0]
        m.read(4)#MaterialLayer
        layer4={}
        layer4["__class"]="MaterialLayer"
        layer4["Enabled"]=struct.unpack('>I',m.read(4))[0]
        layer4["AlphaThreshold"]=-1
        layer4["TexAdressingModeU"]=struct.unpack('>I',m.read(4))[0]
        layer4["TexAdressingModeV"]=struct.unpack('>I',m.read(4))[0]
        layer4["Filtering"]=struct.unpack('>I',m.read(4))[0]
        layer4["DiffuseColor"]=[struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0],struct.unpack('>f',m.read(4))[0]]
        layer4["TextureUsage"]=struct.unpack('>I',m.read(4))[0]
        uvmodifier=struct.unpack('>I',m.read(4))[0]
        for x in range(uvmodifier):
            uvmodifier4={}
            uvmodifier4["__class"]="UVModifier"
            m.read(4)
            uvmodifier4["TranslationU"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier4["TranslationV"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier4["AnimTranslationU"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier4["AnimTranslationV"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier4["Rotation"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier4["RotationOffsetU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier4["RotationOffsetV"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier4["AnimRotation"]=struct.unpack('>I',m.read(4))[0]
            uvmodifier4["ScaleU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier4["ScaleV"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier4["ScaleOffsetU"]=struct.unpack('>f',m.read(4))[0]
            uvmodifier4["ScaleOffsetV"]=struct.unpack('>f',m.read(4))[0]
            layer4["UVModifiers"]=[uvmodifier4]
        material["Layer4"]=layer4

        json.dump(material,open("output/"+graphmaterial,"w"))
