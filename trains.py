trains = {100:"Shiv Ganga","stops":{1:{"station":"VNS","distance":0},2:{"station":"LKO","distance":30},3:{"station":"NDLS","distance":50}}}
print(trains)
trainname = trains.get(100)
print(trainname)
stops = trains.get("stops")
print(stops)
for key in stops:
    print(stops.get(key))