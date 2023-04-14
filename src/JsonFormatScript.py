import json


with open(r"C:\Users\Mitch\Desktop\PennState\IST597\UnderwaterSonarClassification\detr\data\UATD_Training\annotations\instances_val2017.json") as jsonFile:
    pythonData = json.load(jsonFile)
    jsonWriteFile = open(r"C:\Users\Mitch\Desktop\PennState\IST597\UnderwaterSonarClassification\detr\data\UATD_Training\annotations\instances_val2017Formatted.json", "w")
    for entry in pythonData["images"]:
        entry["id"] = int(entry["id"])

    pythonData = str(pythonData).replace("\'", "\"")
    jsonWriteFile.write(pythonData)
    jsonWriteFile.close()




