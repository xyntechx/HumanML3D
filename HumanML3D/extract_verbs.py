import os
import zipfile
from tqdm import tqdm

with zipfile.ZipFile("HumanML3D/texts.zip") as zip_ref:
    zip_ref.extractall("HumanML3D")

labels = {}

for filename in tqdm(os.listdir("HumanML3D/texts")):
    with open(f"HumanML3D/texts/{filename}") as f:
        content = f.read().strip().split("\n")

    verbs = set()

    for line in content:
        tokens = line.split("#")[1].split(" ") # just handling the formatting dictated by each txt file
        for token in tokens:
            if "/VERB" not in token:
                continue
            verbs.add(token.strip("/VERB"))

    label = "-".join(sorted(list(verbs))) # ordering each verb alphabetically ascendingly since order doesn't matter in distinguishing labels (i.e. walk-run == run-walk)

    labels[filename.strip(".txt")] = label

with open("HumanML3D/verbs.txt", "w") as f:
    f.write("\n".join(map(lambda k: f"{k} {labels[k]}", labels)))
    print("FileID to verb mapping saved in HumanML3D/verbs.txt")
