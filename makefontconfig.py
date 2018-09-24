import plistlib
import os
import random

def makeFontConfig( inputFile ):
    
    strFileName = os.path.splitext(os.path.basename(inputFile))[0]
    dirName = os.path.splitext(inputFile)[0]
    
    fFontFile = open(inputFile, 'r')
    strFontContent = fFontFile.read()
    
    
    #dictPayloadContent = {
    #    'Font' : plistlib.Data(strFontContent),
    #    'PayloadIdentifier' : strFileName,
    #    'PayloadType' : 'com.apple.font',
    #    'PayloadUUID' : strUUID,
    #    'PayloadVersion' : 1,        
    #}
    
    payloadData = {
        'PayloadContent' : [ plistlib.Dict( Font = plistlib.Data(strFontContent), 
                                          PayloadIdentifier = strFileName,
                                          PayloadType = 'com.apple.font',
                                          PayloadUUID = genRandomUUID(),
                                          PayloadVersion = 1
                                          ) 
                             ],
        'PayloadDisplayName' : strFileName,
        'PayloadIdentifier': "com.twizzyindy.ios12."+ strFileName,
        'PayloadOrganization': "Lockify YGN",
        'PayloadType' : "Configuration",
        'PayloadUUID' : genRandomUUID(), # TODO : random generate uuid
        'PayloadVersion' : 1
        
    }
    
    outConfig = open( dirName + '.mobileconfig', 'w')
    plistlib.writePlist(payloadData, outConfig)
    
    return

def genRandomUUID():
    
    # i'ma lazy guy
    #a = random.randint(1, 0xFFFFFFFF)
    a1 = random.randint(1, 0xFF )
    a2 = random.randint(1, 0xFF )
    a3 = random.randint(1, 0xFF )
    a4 = random.randint(1, 0xFF )
    
    b1 = random.randint(1, 0xFF )
    b2 = random.randint(1, 0xFF )
    b3 = random.randint(1, 0xFF )
    b4 = random.randint(1, 0xFF )
    b5 = random.randint(1, 0xFF )
    b6 = random.randint(1, 0xFF )
    
    #c = random.randint(1, 0xFFFFFFFFFFFF )
    c1 = random.randint(1, 0xFF )
    c2 = random.randint(1, 0xFF )
    c3 = random.randint(1, 0xFF )
    c4 = random.randint(1, 0xFF )
    c5 = random.randint(1, 0xFF )
    c6 = random.randint(1, 0xFF )
    
    result = "".join('{:02X}{:02X}{:02X}{:02X}-{:02X}{:02X}-{:02X}{:02X}-{:02X}{:02X}-{:02X}{:02X}{:02X}{:02X}{:02X}{:02X}').format(
        a1, a2, a3, a4, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, c5, c6
    )
    return result
        
    
def usage():
    print("\n\nMobileConfig Maker by TwizzyIndy")
    print("9/20/2018")
    print("\n\nUsage : python makefontconfig.py {YOUR TTF FONT FILE}\n\n")
    #print("  -UUID : specify UUID for config")
    return

def main():
    
    if(len(os.sys.argv) < 2):
        usage()
        return
    
    inputTTF = os.sys.argv[1]
    
    ext =  os.path.splitext(os.path.basename(inputTTF))[1]

    if( ext != ".ttf" or ext != ".TTF" ):
        print("\nNot supported file format\n")
        return
    
    makeFontConfig( inputTTF )
    
if __name__ == "__main__":
    main()