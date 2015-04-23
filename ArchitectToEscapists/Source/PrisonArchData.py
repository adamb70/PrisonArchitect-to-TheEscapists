import re ,sys, os, linecache
import time

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


print objectvals

def getTileData(prisonfile):
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
        if 'Type                 Guard' in string:
            objectlist.remove(string)
        elif 'Type                 Visitor' in string:
            objectlist.remove(string)
        elif 'Type                 Prisoner' in string:
            objectlist.remove(string)
        elif 'Type                 Chief' in string:
            objectlist.remove(string)
        elif 'Type                 Workman' in string:
            objectlist.remove(string)
        elif 'Type                 Warden' in string:
            objectlist.remove(string)
        elif 'Type                 Accountant' in string:
            objectlist.remove(string)
        elif 'Type                 Foreman' in string:
            objectlist.remove(string)
        elif 'Type                 Foreman' in string:
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
        n = re.split(r'(Pos.y ........)*', n)
        n = n[0] + n[1]
        n = n.replace(", '            0',", '  ')
        n = n.replace("'", '')
        n = n.replace(",", '')
        n = n.replace('Type  ', 'Type ').strip()
        n = n.replace('Type ', '').replace('Pos.x ', '').replace('Pos.y ', '')
        objects.append(n.split())

    return objects


def findTileValue(materialname, objectvalfile):
    with open(objectvalfile) as matlist:
        for line in matlist:
            if line.startswith(materialname):
                return line.split('= ')[1].strip()


def findObjectValue(objectname, objectfile):
    with open(objectvals) as objlist:
        for line in objlist:
            if line.startswith(objectname):
                return line.split('= ')[-1].strip()


def writetilearray(tiledata):
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
            if X == '7':
                try:
                    if dic[str(n)][k+1] == '7':
                        dic[str(n)][k:k+1] = [findTileValue('SidewaysWall', tilevals)]
                except:
                    pass
            if X == '21':
                try:
                    if dic[str(n)][k+1] == '21':
                        dic[str(n)][k:k+1] = [findTileValue('SidewaysFence', tilevals)]
                except:
                    pass
            if X == '77':
                try:
                    if dic[str(n)][k+1] == '77':
                        dic[str(n)][k:k+1] = [findTileValue('SidewaysPerimeterWall', tilevals)]
                except:
                    pass
            k += 1
    for n in range(int(NumTilesY)):   # Format for each line in Tiles
        tilearray.append(str(n) + '=' + str(dic[str(n)]).replace("'", '').replace(', ', '_').replace('[', '').replace(']', '') + '_' + '\n')
    return tilearray


def writeobjectarray(objectdata):
    objectlist = []
    for object in objectdata:
        type = object[0]
        X = object[1]
        Y = object[2]
        type = findObjectValue(type, objectvals)
        if type != None:
            objectlist.append(X.split('.')[0] + 'x' + Y.split('.')[0] + 'x' + type)
    returnlist = []
    for n in range(len(objectlist)):
        returnlist.append(str(n+1) + '=' + objectlist[n] + '\n')
    return returnlist


def writeFile(prisonfile, tileset):
    template = templatemap
    output = outputpath + str(prisonfile.split('/')[-1].replace('.prison', '.proj'))
    i = 0
    templatedata = linecache.getlines(template)
    newfiledata = []
    print time.time()
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
            print 'middle' + str(time.time())
            global ObjectStart
            ObjectStart = i
        newfiledata.append(line)
    print 'last' + str(time.time())
    objdata = writeobjectarray(getObjectData(prisonfile))
    newfiledata[ObjectStart:ObjectEnd] = objdata
    newfiledata[TileStart+len(objdata):TileEnd+len(objdata)] = writetilearray(getTileData(prisonfile))

    with open(output, 'w') as outfile:
        for n in newfiledata:
            outfile.writelines(n)