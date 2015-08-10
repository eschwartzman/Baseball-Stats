import re, sys, os
 
if len(sys.argv) < 2:
	sys.exit("Usage: %s filename" % sys.argv[0])
 
filename = sys.argv[1]
 
if not os.path.exists(filename):
    sys.exit("Error: File '%s' not found" % sys.argv[1])


regex = "(.*) batted (\d) times with (\d).*"
f = open(filename)
hits = {};
bats = {};
players = [];
for line in f:
    r= re.match(regex, line)
    if r is not None:
       
    	try:
    		bats[r.group(1)] += float(r.group(2))
        	hits[r.group(1)] += float(r.group(3))  
        	
    	except KeyError:
    		bats[r.group(1)] = float(r.group(2))
    		hits[r.group(1)] = float(r.group(3)) 
    		players.append(r.group(1))
    		
avg = {};    		
for player in players:
	avg[player] = ((hits[player] / bats[player]) )
	
   		
for player in sorted(avg, key=avg.get, reverse=True):
	print "%s: %.3f" % (player, avg[player]) 

f.close()









   

    
