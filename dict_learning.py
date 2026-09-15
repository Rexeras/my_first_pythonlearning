import my_module


mycarinfo = {
    "name": "toyota",
    "model": 2026,
    "color": "black"
}

print(mycarinfo.get("name"))
print(mycarinfo.keys())

mycarinfo["madein"] = "china"

print(mycarinfo)

my_module.greetings()