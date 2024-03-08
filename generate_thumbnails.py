import csv
import shutil
import os

# generate (for the moment, dummy) thumbnails for each text: 

thumbnail = "dummy_thumbnail.jpg"
tsv_fp = "../kitab_metadata_for_DLME/kitab_metadata_for_DLME_latest_release.tsv"
thumbnail_folder = "thumbnails"
with open(tsv_fp, mode="r", encoding="utf-8") as file:
    data = csv.DictReader(file, delimiter="\t")
    for row in data:
        fn = row["one2all_vis_url"].split("=")[-1]
        outfp = os.path.join(thumbnail_folder, fn + ".jpg")
        shutil.copyfile(thumbnail, outfp)
