
def buildTable(filename):
    file_a = open('firewall-policies.csv', 'r').readlines()
    accessTable = {}
    
    if file_a[0] == 'id,mac_0,mac_1\n':
        file_a.pop(0)
        
    for line in file_a:
        line = line.split(',')
        index = int(line[0])
        side_a = line[1].strip()
        side_b = line[2].strip()
        accessTable[index] = (side_a, side_b)
        
    return accessTable
        
x = buildTable('firewall-policies.csv')