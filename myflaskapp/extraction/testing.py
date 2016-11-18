import json
from mediameter.cliff import Cliff


def test():
    
    filename = 'test_corpus.txt'
    with open(filename) as f:
        mylist = f.read().splitlines()

    my_cliff = Cliff('http://localhost', 8999)
    
    num_lines_searched = 0
    num_Canada_London = 0
    
    for line in mylist:
        query = str(line)
        if len(query) >= 1 and query[0] != "/":
            num_lines_searched += 1
        
        print '================================='
        print query
        
        result = my_cliff.parseText(query, demonyms=True)
        print result
        if '6058560' and '-81.23304' in str(result):  # if id and lon values in string, it's the correct London
            num_Canada_London += 1
            print '****'
        print '================================='
        
    print str(num_Canada_London) + " / " + str(num_lines_searched)
    
# 6058560

# 29/74


# if result['results']['places']['focus']['cities']:
        #     if result['results']['places']['focus']['cities']['id'].value() == '6058560':
        #         print "TRUE"
        #         num_Canada_London += 1

test()



