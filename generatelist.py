import xmltodict, json

xmlFile = "NaPTAN.xml"

with open("./NaPTAN.xml", "r", encoding="utf-8") as naptan_file:
    f = naptan_file.read()

    root = xmltodict.parse(f)
    tree = root['NaPTAN']

    stations = []

    for stop in tree['StopPoints'].items():
        for items in stop[1]:
            if "OffStreet" in items['StopClassification']:
                if "Rail" in items['StopClassification']['OffStreet']:
                    if "AnnotatedRailRef" in items['StopClassification']['OffStreet']['Rail']:
                        template = {
                            'atcoCode': "",
                            'tiplocCode': "",
                            'crsCode': "",
                            'stationName': "",
                            'lat': 0.0,
                            'long': 0.0
                        }

                        template['atcoCode'] = items['AtcoCode']
                        template['tiplocCode'] = items['StopClassification']['OffStreet']['Rail']['AnnotatedRailRef']['TiplocRef']
                        template['crsCode'] = items['StopClassification']['OffStreet']['Rail']['AnnotatedRailRef']['CrsRef']
                        template['stationName'] = items['StopClassification']['OffStreet']['Rail']['AnnotatedRailRef']['StationName']

                        if "Translation" in items['Place']['Location']:
                            template['lat'] = items['Place']['Location']['Translation']['Latitude']
                            template['long'] = items['Place']['Location']['Translation']['Longitude']

                        stations.append(template)
                        print("Added station "+items['StopClassification']['OffStreet']['Rail']['AnnotatedRailRef']['TiplocRef'])

                        # print(items['StopClassification']['OffStreet']['Rail']['AnnotatedRailRef']['TiplocRef'])

    with open('stations.json', 'w') as stationfile:
        json.dump(stations, stationfile)

print("Station file done")