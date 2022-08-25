import json
import os
import subprocess

import pandas as pd
from tqdm import tqdm

if __name__ == "__main__":
    if "scripts" in os.getcwd():
        os.chdir("..")

os.makedirs("data/videos", exist_ok=True)

with open("data/json/av_train.json", "r") as f:
    ori_annot_train = json.load(f)

with open("data/json/av_val.json", "r") as f:
    ori_annot_val = json.load(f)

with open("data/csv/manifest.csv", "r") as f:
    manifest = pd.read_csv(f)

print("Downloading val videos...")
video_pbar = tqdm(ori_annot_val["videos"], total=len(ori_annot_val["videos"]))
clip_count = 0
for video in video_pbar:
    video_uid = video["video_uid"]
    video_pbar.set_postfix({"processing": video_uid})

    clip_pbar = tqdm(video["clips"], total=len(video["clips"]), leave=False)
    for clip in clip_pbar:
        clip_uid = clip["clip_uid"]

        clip_count += 1

        canonical_path = manifest[manifest["exported_clip_uid"] == clip_uid]
        assert len(canonical_path) == 1

        # make sure the clip is from the av challenge
        assert canonical_path["benchmarks"].str.contains("AV").any()

        canonical_path = canonical_path["s3_path"].iloc[0]
        cmd = f"aws s3 cp {canonical_path} data/videos/ --quiet"

        # check if we already have the video in tmp folder
        if not os.path.exists(f"data/videos/{clip_uid}.mp4"):
            clip_pbar.set_postfix({"downloading": clip_uid})
            subprocess.run(cmd, shell=True)

print(f"Downloaded {clip_count} clips for val set")

print("Downloading train videos...")
video_pbar = tqdm(ori_annot_train["videos"], total=len(ori_annot_train["videos"]))
clip_count = 0
for video in video_pbar:
    video_uid = video["video_uid"]
    video_pbar.set_postfix({"processing": video_uid})

    clip_pbar = tqdm(video["clips"], total=len(video["clips"]), leave=False)
    for clip in clip_pbar:
        clip_uid = clip["clip_uid"]

        clip_count += 1

        canonical_path = manifest[manifest["exported_clip_uid"] == clip_uid]
        assert len(canonical_path) == 1

        # make sure the clip is from the av challenge
        assert canonical_path["benchmarks"].str.contains("AV").any()

        canonical_path = canonical_path["s3_path"].iloc[0]
        cmd = f"aws s3 cp {canonical_path} data/videos/ --quiet"

        # check if we already have the video in tmp folder
        if not os.path.exists(f"data/videos/{clip_uid}.mp4"):
            clip_pbar.set_postfix({"downloading": clip_uid})
            subprocess.run(cmd, shell=True)

print(f"Downloaded {clip_count} clips for train set")
print("finish")
