import json
from pprint import pp


def transformation(payload_json):
    result_json = []
    common_data = {
        "collectionType": payload_json["collectionType"],
        "createdBy": payload_json["createdBy"],
        "createdDate": payload_json["createdDate"],
        "product": payload_json["productId"],
        "origin": payload_json["origin"],
        "event_timestamp": payload_json["event"]["timestamp"],
    }
    for each, detail in payload_json["packagingData"]["primary"]["components"].items():
        each_record = common_data.copy()
        each_record.update(
            {
                "packaging_level": "primary",
                "component_type": each,
                "Colour": detail[0]["Colour"],
                "Depth (mm)": detail[0]["Depth(mm)"],
                "Height (mm)": detail[0]["Height(mm)"],
                "Width (mm)": detail[0]["Width(mm)"],
                "material_type": "Plastic",
                "Detectable": detail[0]["material"]["Plastic"]["Detectable"],
                "Flexible or Rigid": detail[0]["material"]["Plastic"][
                    "FlexibleorRigid"
                ],
            }
        )
        result_json.append(each_record)
    return result_json


if __name__ == "__main__":
    with open("input.json", "r") as fh:
        data_dic = json.load(fh)

    pp(transformation(data_dic))
