# python-automation
Automate the boring stuff
#Generating xml files
1.Each dictionary in a list are user data.\
2.These data are populated to xml data values.\
e,g : <root><sno>{sno}</sno><name>{name}</name><location>{loc}</location></root> \
[{"sno":1,"name":"Fazil","loc":"chennai"},{"sno":2,"name":"Vishak","loc":"Hyderabad"},{"sno":3,"name":"sharath","loc":"Banglore"}]

#Running python files as batch
1. Sample python files created in samplePythonfiles directory.\
2. Each file take it in list using os.listdir().\
3. Each file executed using os.system.\
Note: Using os.system() we can any  runnable commands as we do in command prompt