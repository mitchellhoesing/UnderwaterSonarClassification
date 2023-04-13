import json


with open(r"C:\Users\Mitch\Desktop\Penn State\IST597\UnderwaterSonarClassification\detr\data\UATD_Training\annotations\instances_train2017Original.json") as jsonFile:
    pythonData = json.load(jsonFile)
    jsonWriteFile = open(r"C:\Users\Mitch\Desktop\Penn State\IST597\UnderwaterSonarClassification\detr\data\UATD_Training\annotations\instances_train2017Formatted.json", "w")
    for entry in pythonData["images"]:
        entry["id"] = int(entry["id"])

    pythonData = str(pythonData).replace("\'", "\"")
    jsonWriteFile.write(pythonData)
    jsonWriteFile.close()




