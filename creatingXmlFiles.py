def createFiles(data):
    for d in data:
        sno,name,loc=d["sno"],d["name"],d["loc"]
        with open(f"./automatedInputFiles/{sno}{name}.xml","w") as f1:
            f1.writelines(f"<root><sno>{sno}</sno><name>{name}</name><location>{loc}</location></root>")
data = [{"sno":1,"name":"Fazil","loc":"chennai"},{"sno":2,"name":"Vishak","loc":"Hyderabad"},{"sno":3,"name":"sharath","loc":"Banglore"}]
createFiles(data)