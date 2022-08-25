import subprocess, os, json
import pandas as pd
from tqdm import tqdm

if __name__ == '__main__':
    if 'scripts' in os.getcwd():
        os.chdir('..')

os.makedirs('data/tmp', exist_ok=True)
os.makedirs('data/videos', exist_ok=True)

with open('data/json/av_train.json', 'r') as f:
    ori_annot_train = json.load(f)

with open('data/json/av_val.json', 'r') as f:
    ori_annot_val = json.load(f)

with open('data/csv/manifest.csv', 'r') as f:
    manifest = pd.read_csv(f)

print("Downloading val videos...")
download_pbar = tqdm(ori_annot_val['videos'], total=len(ori_annot_val['videos']))
for video in download_pbar:
    video_uid = video['video_uid']

    canonical_path = manifest[manifest['parent_video_uid']==video_uid]['s3_path'].iloc[0]
    cmd = f'aws s3 cp {canonical_path} data/tmp/ --quiet'

    # check if we already have the video in tmp folder
    file_name = canonical_path.split('/')[-1]
    if not os.path.exists(f'data/tmp/{file_name}'):
        download_pbar.set_postfix({'downloading': video_uid})
        subprocess.run(cmd, shell=True)

    chunking_pbar = tqdm(video['clips'], total=len(video['clips']), leave=False)

    for clip in chunking_pbar:
        clip_uid = clip['clip_uid']

        # skip if we already have the video
        if os.path.exists(f'data/videos/{clip_uid}.mp4'):
            continue

        chunking_pbar.set_postfix({'chunking': clip_uid})
        start_sec = clip['video_start_sec']
        end_sec = clip['video_end_sec']
        cmd = f'ffmpeg -y -i data/tmp/{file_name} -ss {start_sec} -to {end_sec} -c:a copy -vcodec libx264 -keyint_min 2 -g 1  -y data/videos/{clip_uid}.mp4 -loglevel quiet'
        subprocess.call(cmd, shell=True)
    os.remove(f'data/tmp/{file_name}')

print("Downloading train videos...")
download_pbar = tqdm(ori_annot_train['videos'], total=len(ori_annot_train['videos']))
for video in download_pbar:
    video_uid = video['video_uid']
    canonical_path = manifest[manifest['parent_video_uid']==video_uid]['s3_path'].iloc[0]
    cmd = f'aws s3 cp {canonical_path} data/tmp/ --quiet'

    # check if we already have the video in tmp folder
    file_name = canonical_path.split('/')[-1]
    if not os.path.exists(f'data/tmp/{file_name}'):
        download_pbar.set_postfix({'downloading': video_uid})
        subprocess.run(cmd, shell=True)

    chunking_pbar = tqdm(video['clips'], total=len(video['clips']), leave=False)

    for clip in chunking_pbar:
        clip_uid = clip['clip_uid']

        # skip if we already have the video
        if os.path.exists(f'data/videos/{clip_uid}.mp4'):
            continue

        chunking_pbar.set_postfix({'chunking': clip_uid})
        start_sec = clip['video_start_sec']
        end_sec = clip['video_end_sec']
        cmd = f'ffmpeg -y -i data/tmp/{file_name} -ss {start_sec} -to {end_sec} -c:a copy -vcodec libx264 -keyint_min 2 -g 1  -y data/videos/{clip_uid}.mp4 -loglevel quiet'
        subprocess.call(cmd, shell=True)
    os.remove(f'data/tmp/{file_name}')

print('finish')

