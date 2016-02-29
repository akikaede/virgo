import memcache

mc = memcache.Client(['172.22.197.176:11211'], debug=0)
#mc.set('1', '7758')
#var = mc.get('1')
#mc.incr('1')
#var = mc.get('1')
#print var


#pwd = mc.delete('ha1_100001')
pwd = mc.get('ha1_100001')
#mc.incr('ha1_100001')
print pwd
