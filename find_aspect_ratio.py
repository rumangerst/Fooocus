from PIL import Image
import sys

aspect_ratio_dict = {
    "704×1408 ∣ 1:2": 1.0 / 2.0,
    "768×1280 ∣ 3:5": 3.0 / 5.0,
    "896×1152 ∣ 7:9": 7.0 / 9.0,
    "960×1024 ∣ 15:16": 15.0 / 16.0,
    "1088×960 ∣ 17:15": 17.0 / 15.0,
    "1152×832 ∣ 18:13": 18.0 / 13.0,
    "1344×768 ∣ 7:4": 7.0 / 4.0,
    "1472×704 ∣ 23:11": 23.0 / 11.0,
    "1664×576 ∣ 26:9": 26.0 / 9.0,
    "704×1344 ∣ 11:21": 11.0 / 21.0,
    "832×1216 ∣ 13:19": 13.0 / 19.0,
    "896×1088 ∣ 14:17": 14.0 / 17.0,
    "1024×1024 ∣ 1:1": 1,
    "1088×896 ∣ 17:14": 17.0 / 14.0,
    "1216×832 ∣ 19:13": 19.0 / 13.0,
    "1344×704 ∣ 21:11": 21.0 / 11.0,
    "1536×640 ∣ 12:5": 12.0 / 5.0,
    "1728×576 ∣ 3:1": 3.0 / 1.0,
    "768×1344 ∣ 4:7": 4.0 / 7.0,
    "832×1152 ∣ 13:18": 13.0 / 18.0,
    "960×1088 ∣ 15:17": 15.0 / 17.0,
    "1024×960 ∣ 16:15": 16.0 / 15.0,
    "1152×896 ∣ 9:7": 9.0 / 7.0,
    "1280×768 ∣ 5:3": 5.0 / 3.0,
    "1408×704 ∣ 2:1": 2.0 / 1.0,
    "1600×640 ∣ 5:2": 5.0 / 2.0
}

with Image.open(sys.argv[1]) as im:
    width, height = im.size
    print("Image size is " + str(width) + "x" + str(height))
    target_ratio = width / height

    closest_name = None
    min_difference = float('inf')

    for name, ratio in aspect_ratio_dict.items():
        difference = abs(target_ratio - ratio)
        if difference < min_difference:
            min_difference = difference
            closest_name = name

    print("SELECT: " + closest_name)