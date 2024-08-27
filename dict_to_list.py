#convert a dict too list
foot=[]
football = {"Name":"Cristiano Ronaldo","Age":39
}

print(football.keys())
print(football.values())

for key in football.items():
    foot.append(key)
print(foot)