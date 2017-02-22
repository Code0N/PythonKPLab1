tempstr = ''
filevar = open('urllist.txt', 'r')
templist = [i.replace('\n', '') for i in filevar]
for i in templist:
    if i.startswith('www.'):
        tempstr = 'https://' + i
        if not i.endswith('.com'):
            tempstr += '.com'
        print(tempstr)