import re, sys, os, linecache

tilevalpath = 'Source\\Files\\tilevals.txt'
objectvalpath = 'Source\\Files\\objects.txt'
templatepath = 'Source\\Files\\TemplateMap.txt'
outputpath = 'Output\\'

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

tilevals = os.path.join(application_path, tilevalpath)
objectvals = os.path.join(application_path, objectvalpath)
templatemap = os.path.join(application_path, templatepath)
outputpath = os.path.join(application_path, outputpath)


def getTileData(prisonfile):
    """Reads the Prison Architect file and returns formatted tile data for use later."""
    datalist = []
    global NumCellsX
    global NumCellsY
    global celldatastart
    with open(prisonfile, 'r') as infile:
        for num, data in enumerate(infile):
            if data.startswith('NumCellsX'):
                NumCellsX = data.replace('NumCellsX            ', '')
            if data.startswith('NumCellsY'):
                NumCellsY = data.replace('NumCellsY            ', '')
            if data.startswith('BEGIN Cells'):
                celldatastart = num
            if data.startswith('END'):
                break
            else:
                datalist.append(data)

    dataarray = []

    for i, line in enumerate(datalist):
        if i > celldatastart:
            line = line.replace('    BEGIN ', '')
            line = line.replace('  END', '')
            dataarray.append(line.replace('\n', ''))
    del datalist

    tilelist = []
    for line in dataarray:
        coords = line[1:6].split('"')[0]
        if 'Mat' in line:
            mat = line.split('Mat ')[1].split('  Con')[0]
        else:
            mat = 'Dirt'
        tiledata = []
        tiledata.extend(coords.split(' '))
        tiledata.append(mat)
        tilelist.append(tiledata)
    return tilelist, NumCellsX, NumCellsY


def getObjectData(prisonfile):
    """Takes the data for objects directly from the Prison Architect file and formats it for
       use in the later functions to create an array of object values"""
    datalist = []
    global NumCellsX
    global NumCellsY
    global objectdatastart
    with open(prisonfile, 'r') as infile:
        for num, data in enumerate(infile):
            if data.startswith('NumCellsX'):
                NumCellsX = data.replace('NumCellsX            ', '')
            if data.startswith('NumCellsY'):
                NumCellsY = data.replace('NumCellsY            ', '')
            if data.startswith('BEGIN Objects'):
                objectdatastart = num
            if data.startswith('BEGIN Rooms'):
                break
            else:
                datalist.append(data)

    dataarray = []
    for i, line in enumerate(datalist):
        if i > objectdatastart+1:
            dataarray.append(line.replace('\n', ''))
    del datalist

    mylist = []
    linenum = 0
    varcount = 0
    varlinedic = {}
    objectlist = []
    for line in dataarray:
        line = line.replace('BEGIN', '[').replace('END', ']')
        linenum += 1
        if line.startswith('    ['):
            varcount += 1

        varlinedic[varcount] = linenum
        mylist.append(line.strip())

    for key in varlinedic:
        if key == varlinedic[key]:
            objectlist.append(mylist[varlinedic[key]-1:varlinedic[key]])
        else:
            objectlist.append(mylist[varlinedic[key-1]:varlinedic[key]])

    for string in objectlist[0:len(objectlist)]:
        if 'Guard' in str(string):
            objectlist.remove(string)
        elif 'Visitor' in str(string):
            objectlist.remove(string)
        elif 'Prisoner' in str(string):
            objectlist.remove(string)
        elif 'Chief' in str(string):
            objectlist.remove(string)
        elif 'Workman' in str(string):
            objectlist.remove(string)
        elif 'Warden' in str(string):
            objectlist.remove(string)
        elif 'Accountant' in str(string):
            objectlist.remove(string)
        elif 'Foreman' in str(string):
            objectlist.remove(string)
        elif 'Cook ' in str(string):
            objectlist.remove(string)
        else:
            pass

    objects = []
    for n in objectlist:
        n = re.split(r'(\bType)*', str(n))
        n = n[1] + n[2]
        n = n.replace('                ', ' ')
        n = re.split(r'SubType..', n)
        n = n[0].strip() + n[1]

        n = re.split(r'(Pos.y .......)*', n)

        if 'Or.' in n[2]:
            n[2] = re.split(r'(Or.......)*', n[2])[1] + "' '" + re.split(r'(Or.......)*', n[2])[-2]
        else:
            n = n[0] + n[1]

        n = str(n)
        n = str(n)
        n = n.replace(", '            0',", '  ')
        n = n.replace("'", '')
        n = n.replace(",", '')
        n = n.replace('"', '')
        n = n.replace('[', '')
        n = n.replace(']', '')
        n = n.replace('   ', ' ')
        n = n.replace('  ', ' ')
        n = n.replace('Type  ', 'Type ').strip()
        n = n.replace('Type ', '').replace('Pos.x ', '').replace('Pos.y ', '').replace('Or.x', '').replace('Or.y', '')

        objects.append(n.split())

    return objects


def findTileValue(materialname, tilevalfile):
    """Takes the tile name from Prison Architect and returns the tile value
       for The Escapists."""
    with open(tilevalfile) as matlist:
        for line in matlist:
            if line.startswith(materialname):
                return line.split('= ')[1].strip()


def findObjectValue(objectname):
    """Takes the object name from Prison Architect and returns the tile value
       for The Escapists."""
    with open(objectvals) as objlist:
        for line in objlist:
            if line.startswith(objectname):
                return line.split('= ')[-1].strip()


def writetilearray(tiledata):
    """Takes tile data from Prison Architect file, finds the equivalent tile value
       for The Escapists, and writes it to an array for use in the output file."""
    tilearray = []
    dic = {}
    NumTilesX = tiledata[1]
    NumTilesY = tiledata[2]
    tiledata = tiledata[0]
    for X, Y, Z in tiledata:
        dic[Y] = []
    for X, Y, Mat in tiledata:
        materialvalue = findTileValue(Mat, tilevals)
        dic[Y].append(materialvalue)
    for n in range(int(NumTilesY)):  # Find adjacent wall tiles and replace with sideways walls
        k = 0
        for X in dic[str(n)]:
            if X in ('6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'):  # If tiles are wall variants
                # Initialise the variables:
                above = False
                right = False
                below = False
                left = False
                origin = True
                try:  # Find if adjacent tiles are the same type, then set them to the correct tile type
                    if dic[str(n+1)][k] in ('6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'):
                        below = True
                    if dic[str(n-1)][k] in ('6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'):
                        above = True
                    if dic[str(n)][k-1] in ('6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'):
                        left = True
                    if dic[str(n)][k+1] in ('6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'):
                        right = True

                    if origin and right:
                        dic[str(n)][k:k+1] = [findTileValue('SidewaysWall', tilevals)]
                    if origin and left:
                        dic[str(n)][k:k+1] = [findTileValue('SidewaysWall', tilevals)]

                    if below and right:
                        dic[str(n)][k] = [findTileValue('WallTopLeft', tilevals)]
                    if below and left:
                        dic[str(n)][k] = [findTileValue('WallTopRight', tilevals)]
                    if above and right:
                        dic[str(n)][k] = [findTileValue('WallBottomLeft', tilevals)]
                    if above and left:
                        dic[str(n)][k] = [findTileValue('WallBottomRight', tilevals)]

                    if above and right and left:
                        dic[str(n)][k] = [findTileValue('WallTNorth', tilevals)]
                    if above and left and below:
                        dic[str(n)][k] = [findTileValue('WallTEast', tilevals)]
                    if below and right and left:
                        dic[str(n)][k] = [findTileValue('WallTSouth', tilevals)]
                    if above and right and below:
                        dic[str(n)][k] = [findTileValue('WallTWest', tilevals)]
                    if above and right and below and left:
                        dic[str(n)][k] = [findTileValue('WallCross', tilevals)]
                except:
                    pass

            if X in ('90', '91', '92'):  # If tiles are outer electric fences
                # Initialise the variables:
                above = False
                right = False
                below = False
                left = False
                origin = True
                try:  # Find if adjacent tiles are the same type, then set them to the correct tile type
                    if dic[str(n+1)][k] in ('90', '91', '92'):
                        below = True
                    if dic[str(n-1)][k] in ('90', '91', '92'):
                        above = True
                    if dic[str(n)][k-1] in ('90', '91', '92'):
                        left = True
                    if dic[str(n)][k+1] in ('90', '91', '92'):
                        right = True

                    if origin and right:
                        dic[str(n)][k:k+1] = [findTileValue('SidewaysPerimeterWall', tilevals)]
                    if origin and left:
                        dic[str(n)][k:k+1] = [findTileValue('SidewaysPerimeterWall', tilevals)]

                    if below and right:
                        dic[str(n)][k] = [findTileValue('PerimeterWallConnector', tilevals)]
                    if below and left:
                        dic[str(n)][k] = [findTileValue('PerimeterWallConnector', tilevals)]
                    if above and right:
                        dic[str(n)][k] = [findTileValue('PerimeterWallConnector', tilevals)]
                    if above and left:
                        dic[str(n)][k] = [findTileValue('PerimeterWallConnector', tilevals)]
                except:
                    pass

            if X in ('20', '21', '22', '23', '24', '25'):  # If tiles are fence variants
                # Initialise the variables:
                above = False
                right = False
                below = False
                left = False
                origin = True
                try:  # Find if adjacent tiles are the same type, then set them to the correct tile type
                    if dic[str(n+1)][k] in ('20', '21', '22', '23', '24', '25'):
                        below = True
                    if dic[str(n-1)][k] in ('20', '21', '22', '23', '24', '25'):
                        above = True
                    if dic[str(n)][k-1] in ('20', '21', '22', '23', '24', '25'):
                        left = True
                    if dic[str(n)][k+1] in ('20', '21', '22', '23', '24', '25'):
                        right = True

                    if origin and right:
                        dic[str(n)][k:k+1] = [findTileValue('SidewaysFence', tilevals)]
                    if origin and left:
                        dic[str(n)][k:k+1] = [findTileValue('SidewaysFence', tilevals)]

                    if below and right:
                        dic[str(n)][k] = [findTileValue('FenceTL', tilevals)]
                    if below and left:
                        dic[str(n)][k] = [findTileValue('FenceTR', tilevals)]
                    if above and right:
                        dic[str(n)][k] = [findTileValue('FenceBL', tilevals)]
                    if above and left:
                        dic[str(n)][k] = [findTileValue('FenceBR', tilevals)]

                    if above and right and left:
                        dic[str(n)][k] = [findTileValue('FenceConnector', tilevals)]
                    if above and left and below:
                        dic[str(n)][k] = [findTileValue('FenceConnector', tilevals)]
                    if below and right and left:
                        dic[str(n)][k] = [findTileValue('FenceConnector', tilevals)]
                    if above and right and below:
                        dic[str(n)][k] = [findTileValue('FenceConnector', tilevals)]
                    if above and right and below and left:
                        dic[str(n)][k] = [findTileValue('FenceConnector', tilevals)]
                except:
                    pass
            k += 1
    for n in range(int(NumTilesY)):   # Format for each line in Tiles
        tilearray.append(str(n) + '=' + str(dic[str(n)]).replace("'", '').replace(', ', '_').replace('[', '').replace(']', '') + '_' + '\n')
    return tilearray


def writeobjectarray(objectdata):
    """Uses the object data from Prison Architect and finds the values for The Escapists.
       Takes the values and writes them to an array for use in the output file."""
    objectlist = []
    for object in objectdata:
        type = object[0]
        X = object[1]
        Y = object[2]
        if len(object) == 5:
            Or_x = object[3]
            Or_y = object[4]
        type = findObjectValue(type)

        if type == findObjectValue('Bed'):  # Find bed orientation
            newY = int(Y.split('.')[0])-1
            if len(object) == 5:
                if round(float(Or_x.replace('-', '')), 1) == 1.0:
                    objectlist.append(str(int(X.split('.')[0])-1) + 'x' + Y.split('.')[0] + 'x' + findObjectValue('SidewaysBed'))
                else:
                    objectlist.append(X.split('.')[0] + 'x' + str(newY) + 'x' + type)
            else:
                objectlist.append(X.split('.')[0] + 'x' + str(newY) + 'x' + type)

        elif type == findObjectValue('MetalDetector'):  # Find detector orientation
            if len(object) == 5:
                if round(float(Or_x.replace('-', '')), 1) == 1.0:
                    objectlist.append(X.split('.')[0] + 'x' + Y.split('.')[0] + 'x' + findObjectValue('MetalDetectorVertical'))
                else:
                    objectlist.append(X.split('.')[0] + 'x' + Y.split('.')[0] + 'x' + type)
            else:
                objectlist.append(X.split('.')[0] + 'x' + Y.split('.')[0] + 'x' + type)

        elif type == findObjectValue('Toilet'):  # Find toilet orientation
            if len(object) == 5:
                if round(float(Or_x), 1) == 1.0:
                    objectlist.append(X.split('.')[0] + 'x' + Y.split('.')[0] + 'x' + findObjectValue('ToiletRight'))
                elif round(float(Or_x), 1) == -1.0:
                    objectlist.append(X.split('.')[0] + 'x' + Y.split('.')[0] + 'x' + findObjectValue('ToiletLeft'))
                else:
                    objectlist.append(X.split('.')[0] + 'x' + Y.split('.')[0] + 'x' + type)
            else:
                objectlist.append(X.split('.')[0] + 'x' + Y.split('.')[0] + 'x' + type)

        elif type is not None:
            objectlist.append(X.split('.')[0] + 'x' + Y.split('.')[0] + 'x' + type)

    returnlist = []
    for n in range(len(objectlist)):
        returnlist.append(str(n+1) + '=' + objectlist[n] + '\n')
    return returnlist


def writeUndergroundarray(grounddata):
    """Finds if tile is an electric fence. If it is, it will set the underground
       tile as an electric fence too. Same for fence connectors."""
    tilearray = []
    dic = {}
    ugroundarray = []
    for n in grounddata:
        tilearray.append(n.strip().split('=')[1].split('_'))
    for num, line in enumerate(tilearray):
        dic[num] = line
    for n in range(len(tilearray)):
        k = 0
        for tile in dic[n]:
            if dic[n][k] not in ('90', '91', '92'):
                dic[n][k] = '0'
            if dic[n][k] == '92':
                if dic[n][k+1] == '0' and dic[n][k-1] == '0' and dic[n+1][k] == '0' and dic[n-1][k] == '0':
                    dic[n][k] = '0'
            k += 1
    for n in range(len(dic)):   # Format for each line in Tiles
        ugroundarray.append(str(n) + '=' + str(dic[n]).replace('[', '').replace(']', '').replace("'", "").replace(', ', '_') + '_' + '\n')

    return ugroundarray


def writeFile(prisonfile, tileset):
    """Takes all of the data for the map and writes it to and array,
       then writes the array to the outfile"""
    template = templatemap
    output = outputpath + str(prisonfile.split('/')[-1].replace('.prison', '.proj'))
    i = 0
    templatedata = linecache.getlines(template)
    newfiledata = []
    for line in templatedata:
        i += 1
        if line.startswith('Tileset='):
            line = line.replace(line, 'Tileset=' + tileset + '\n')
        if line.startswith('[Tiles]'):
            global TileStart
            global ObjectEnd
            TileStart = i
            ObjectEnd = i-1
        if line.startswith('[Vents]'):
            global TileEnd
            TileEnd = i-1
        if line.startswith('[Objects]'):
            global ObjectStart
            ObjectStart = i
        if line.startswith('[Underground]'):
            global UgroundStart
            UgroundStart = i
        newfiledata.append(line)
    objdata = writeobjectarray(getObjectData(prisonfile))
    tiledata = writetilearray(getTileData(prisonfile))

    newfiledata[ObjectStart:ObjectEnd] = objdata
    newfiledata[TileStart+len(objdata):TileEnd+len(objdata)] = tiledata
    newfiledata[(UgroundStart+len(objdata)+len(tiledata))-108:UgroundStart+len(objdata)+len(tiledata)] = writeUndergroundarray(writetilearray(getTileData(prisonfile)))
    with open(output, 'w') as outfile:
        for line in newfiledata:
            outfile.writelines(line)
