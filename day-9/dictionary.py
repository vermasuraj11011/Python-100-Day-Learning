dic = {
    "India": "Asia",
    "Usa": "North America",
    "UK": "Europe",
}

for key in dic:
    print(key)
    print(dic[key])

dic["India"] = "South Asia"
print(dic["India"])

dic["Pakistan"] = "Asia"

print(dic)



