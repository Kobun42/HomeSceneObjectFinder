import sys
import argparse
import xml.etree.ElementTree as ET
from kobun42.hubps3 import SceneFileParser

def initParser():
    # init argparse
    tempParser = argparse.ArgumentParser(
                    prog="HomeSceneObjectFinder",
                    description="Finds PlayStation Home object IDs within scene files.",
                    epilog="Contact Kobun42 if you need help.",
                    add_help=True)
    
    tempParser.add_argument('filename',
                            help="Path of scenefile.") # obviously you need a file.
    tempParser.add_argument('-f', '--filter', choices=['all', 'sceneObjectOnly', 'luaGameOnly', 'arcadeGameOnly'], default='all',
                            help="Filters UUID output to specific object types only.")
    tempParser.add_argument('-p', '--printUUIDList', action='store_true', default=False,
                            help="Prints UUID list to a text file.")
    return tempParser

def main():
    parser = initParser()
    args = parser.parse_args()
    sfParser = SceneFileParser.SceneFileParser()
    uuids = sfParser.getSceneXmlAndParse(args.filename, args.filter)
    
    if (args.printUUIDList == True):
        with open('uuids.txt', 'w') as ul:
            for uuid in uuids:
                ul.write("%s\n" % uuid)
                print(uuid)
    else:
        for uuid in uuids:
            print(uuid)
    
main()