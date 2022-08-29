# Ego4d Social Benchmark (TTM)
This repository contains the codebase for Ego4d social benchmark -- *Talking-to-me* baseline models. 

Switch to [*Looking-at-me*](https://github.com/EGO4D/social-interactions/tree/lam).

***

### Note from the author
This repository is a fork of the original repository and trying to fix the original bugs.
You can download file in the below to be able to reproduce the results:

Download _av_train.json_ and _av_val.json_: 
```
ego4d --output_directory="~/ego4d_data" --datasets annotations
```

Download _manifest.csv_ (don't need to download the whole dataset, only the manifest):
```
ego4d --output_directory="~/ego4d_data" --metadata --datasets clips
```

[//]: # ([_manifest.csv_]&#40;https://drive.google.com/file/d/1skwx4fjwykfxmYhUHYk4-9BXWLNWiqSw/view?usp=sharing&#41;\)
[//]: # ([_av_train.json_]&#40;https://drive.google.com/file/d/1YwZjGfSnCyim95CdF3Q1HoyUqpSz-KPr/view?usp=sharing&#41;\)
[//]: # ([_av_val.json_]&#40;https://drive.google.com/file/d/1xR9n36mqmXzw3GpMyQYjPibYp5-vQ_oX/view?usp=sharing&#41;)

### Dependencies

Start from building the environment
```
sudo apt-get install ffmpeg
pip install -r requirements.txt
```

***
### Data preparation

Skip the following steps if you already get the data following the instructions in *Looking-at-me*.

Download data manifest (`manifest.csv`) and annotations (`av_{train/val}.json`) for audio-visual diarization benchmark following the Ego4D download [instructions](https://github.com/facebookresearch/Ego4d/blob/main/ego4d/cli/README.md).

Note: the default folder to save videos and annotations is ```./data```, please create symbolic links in ```./data``` if you save them in another directory. The structure should be like this:

data/
* csv/
  * manifest.csv
* json/
  * av_train.json
  * av_val.json
* split/
  * test.list
  * train.list
  * val.list
  * full.list
* videos/
  * 00407bd8-37b4-421b-9c41-58bb8f141716.mp4
  * 007beb60-cbab-4c9e-ace4-f5f1ba73fccf.mp4
  * ...
  
Run the following script to download videos and generate clips:
```
python scripts/download_clips.py
```

Run the following scripts to preprocess the videos and annotations:

```
bash scripts/extract_frame.sh
bash scripts/extract_wave.sh
python scripts/preprocessing.py
```
**Note**. Make sure to set the correct _output_address_ in the _'extract_frame.sh'_ and _'extract_wave.sh'_ scripts.
Accordingly, you must add this address to the '_common/config.py_' file.

### 2. Train

### Updates 11 Jun 2022
The training dataset in this codebased is based on the original instead of the released cropped dataset, please modify it accordingly if you want to train the model again.

Run the following script to start training:
```
python run.py
```
Specify the arguments listed in [common/config.py](./common/config.py) if you want to customize the training.

Note: this codebase does **not** support multi-GPU mode.

### 3. Inference
Download the [checkpoints](https://drive.google.com/drive/folders/1MGrhm3J1dKoWPSL3RvC3qb3QeiIqe9vi?usp=sharing).

Run the following script for inference:
```
python run.py --eval --checkpoint ${checkpoint_path} --exp_path ${eval_output_dir}
```

Our model trained from scratch on Ego4d yields `mAP:52.85% ACC:60.24%` on validation set. 

### 4. Test
Download the test dataset with the CLI (--datasets social_test) or just directly on S3 (s3://ego4d-consortium-sharing/public/v1/social_test/).

The default folder to save test dataset is ```./data```. The test dataset structure and the meaning of the file name are shown below:

data/
* final_test_data/
  * segment_id/
    * audio/
      * aud.wav
    * face/
      * frame_id.jpg
      * ...
  * segment_id/
    * audio/
      * aud.wav
    * face/
      * frame_id.jpg
      * ...

Our baseline yields `mAP:53.88% ACC:54.33%` on test set.

The output file is "pred.csv". You have to convert it to the right format shown on the [EvalAI Submission Guidelines](https://eval.ai/web/challenges/challenge-page/1625/submission) and submit it.

### Citation

Please cite the following paper if our code is helpful to your research.
```
@article{grauman2021ego4d,
  title={Ego4d: Around the world in 3,000 hours of egocentric video},
  author={Grauman, Kristen and Westbury, Andrew and Byrne, Eugene and Chavis, Zachary and Furnari, Antonino and Girdhar, Rohit and Hamburger, Jackson and Jiang, Hao and Liu, Miao and Liu, Xingyu and others},
  journal={arXiv preprint arXiv:2110.07058},
  year={2021}
}
```
