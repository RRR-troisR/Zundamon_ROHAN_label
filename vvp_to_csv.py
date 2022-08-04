import glob
import json
import os

from typing import Dict

files = glob.glob("./vvproj_data/*.vvproj")

index_content = []

for num in range(92):
    numf = (num) * 50 + 1
    numf = str(numf)
    numg = num * 50 + 50
    numg = str(numg)
    file = os.path.join("./vvproj_data/" + "project" + numf + "-" + numg + ".vvproj")
    print(file)
    content = {}
    with open(file, encoding="utf8") as f:
        content = json.loads(f.read())
    audio_items: Dict[str, Dict] = content["audioItems"]
    for audio_key in audio_items.keys():
        phonemes = []
        accents = []
        audio_item = audio_items[audio_key]
        accent_phrases = audio_item["query"]["accentPhrases"]
        text = audio_item["text"]
        name = text.split(":")[0]
        if text == "":
            pass
        else:
            for accent_phrase in accent_phrases:
                accent = []
                for i, mora in enumerate(accent_phrase["moras"]):
                    if i + 1 == accent_phrase["accent"] and len(accent_phrase["moras"]) != accent_phrase["accent"]:
                        if mora.get("consonant") is not None:
                            accent.append("_")
                            phonemes.append(mora["consonant"])
                        accent.append("]")
                        phonemes.append(mora["vowel"])
                    else:
                        if mora.get("consonant") is not None:
                            accent.append("_")
                            phonemes.append(mora["consonant"])
                        if i == 0:
                            accent.append("[")
                        else:
                            accent.append("_")
                        phonemes.append(mora["vowel"])
                if accent_phrase.get("pauseMora") is not None:
                    accent.append("_")
                    phonemes.append(accent_phrase["pauseMora"]["vowel"])
                accent[-1] = "#"
                accents += accent
            if text[-1] == "？":
                accents[-1] = "?"
            else:
                accents[-1] = "#"

            index_content.append(name + "," + " ".join(phonemes) + "\n" + name + "," + " ".join(accents))

with open("./csv_data/phoneme_and_accent.csv", mode="w") as f:
    f.write("\n".join(index_content))
