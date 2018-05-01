import os
path = "C:\Projects\management\LIS_doc\dto"
def processLine(file,file_name):
    fields=[]
    with open(file,'rt',encoding='UTF-8') as f:
        for line in f:
            words=line.split(' ')
            if(words and len(words)>4):
                try:
                    if(words.index('public')>0):
                        fields.append(words[words.index('public')+2])
                        print(fields)
                except ValueError:
                    None
    writeJson(fields,file_name)


def writeJson(fields,file_name):
    lines=["[\n","  {\n"]
    fo=open(path+'\\'+file_name+'.json','w')
    comma=','
    index=0
    for field in fields:
        if(index == len(fields)-1):
            comma=''
        lines.append("      \""+field[:1].lower()+field[1:]+"\":\"\""+comma+"\n")
        index = index+1
    lines.append("  }\n")
    lines.append("]")
    fo.writelines(lines)



def readFolder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            processLine(folder+'\\'+file,file)

readFolder(path)
