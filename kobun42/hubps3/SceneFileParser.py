import xml.etree.ElementTree as ET

class SceneFileParser:

    uuids = []

    def parseSceneXmlAndGetRoot(self, sceneXml):
        tree = ET.parse(sceneXml)
        root = tree.getroot()
        return root
        
    def checkIfRootTagIsValid(self, xmlRoot):
        if xmlRoot == None:
            print('Missing or invalid xml root.')
            return False
        
        if (xmlRoot.tag == '{gap}game' or xmlRoot.tag == 'game'):
            return True
        else:
            print('File does not appear to be a Home scene file.')
            return False
            
    def findGameObjectFolderInXmlRoot(self, xmlRoot):
        if xmlRoot == None:
            print('Missing or invalid xml root.')
            return None
        
        for child in xmlRoot:
            if child.tag == '{gap}gameObjectFolder' or child.tag == 'gameObjectFolder':
                #print("Found Game Object Folder!")
                return child
                
        return None
        
    def isChildAFolder(self, child):
        if child == None:
            print('Potentially malformed or invalid XML?')
            return False
            
        if (child.tag == '{gap}folder' or child.tag == 'folder'):
            return True
        else:
            return False
            
    def isChildAGameObject(self, child, objectTypeFilter='all'):
        if child == None:
            print('Potentially malformed or invalid XML?')
            return False
            
        if (child.tag == '{gap}gameObject' or child.tag == 'gameObject'):
            if child.attrib['{http://www.w3.org/2001/XMLSchema-instance}type'] == 'sceneObjectType' and (objectTypeFilter == 'all' or objectTypeFilter == 'sceneObjectOnly'):
                return True
            elif child.attrib['{http://www.w3.org/2001/XMLSchema-instance}type'] == 'luaGameType' and (objectTypeFilter == 'all' or objectTypeFilter == 'luaGameOnly'):
                return True
            elif child.attrib['{http://www.w3.org/2001/XMLSchema-instance}type'] == 'arcadeGameType' and (objectTypeFilter == 'all' or objectTypeFilter == 'arcadeGameOnly'):
                return True
            else:
                return False
        else:
            return False
            
    def checkForUUIDdupes(self, requestedUUID):
        for uuid in self.uuids:
            if uuid == requestedUUID:
                return True
            
        return False

    def checkFolder(self, folder, objectTypeFilter):
        for child in folder:
            #YANDEREDEV CODING YAAAAAAAAAAAAAAY
            if self.isChildAGameObject(child, objectTypeFilter):
                if 'uuid' not in child.attrib:
                    # Assume using game tag instead.
                    if 'game' not in child.attrib:
                        print("What the heck is this scene file? GIVE IT TO KOBUN42 SO HE CAN FIGURE THIS OUT!!!!!")
                    else:
                        if not self.checkForUUIDdupes(child.attrib['game']):
                            self.uuids.insert(len(self.uuids)-1, child.attrib['game'])
                else:
                    if not self.checkForUUIDdupes(child.attrib['uuid']):
                        self.uuids.insert(len(self.uuids)-1, child.attrib['uuid'])
                    
            if self.isChildAFolder(child):
                self.checkFolder(child, objectTypeFilter)
            

    def getSceneXmlAndParse(self, sceneXml, objectTypeFilter='all'):
        xmlRoot = self.parseSceneXmlAndGetRoot(sceneXml)
        isFileValid = self.checkIfRootTagIsValid(xmlRoot)
        if not isFileValid:
            print("Scene file invalid! Ensure the file is a PlayStation Home scene file and that it is not corrupted.")
            return []
         
        gameObjectFolder = self.findGameObjectFolderInXmlRoot(xmlRoot)
        if gameObjectFolder == None:
            print('Game Object folder missing or invalid.')
            return []
            
        self.checkFolder(gameObjectFolder, objectTypeFilter)
                        
        return self.uuids
