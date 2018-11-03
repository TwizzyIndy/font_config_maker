import plistlib
import os

def extract_font(path):
    f = open(path, mode='r')
    
    content = plistlib.readPlistFromString(f.read())
    
    font = content['PayloadContent'][0]['Font']
    #fontData = font.data
    fontName = content['PayloadDisplayName']

    
    o = open(fontName + ".ttf", mode='w')
    
    o.write(font.data)
    
    return

def main():
    if len(os.sys.argv) < 2:
        return
    
    extract_font(os.sys.argv[1])
    return

    
if __name__ == "__main__":
    main()