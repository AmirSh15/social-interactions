#!/bin/bash
output_address="/media/amir_shirian/Amir/Datasets/Ego4D"
if [ ! -d $output_address"/data"  ];then
	mkdir $output_address"/data"
fi
if [ ! -d $output_address"/data/video_imgs"  ];then
	mkdir $output_address"/data/video_imgs"
fi
for file in `ls data/videos/*`
do
	name=$(basename $file .mp4)
	echo "$name"
	PTHH=$output_address/data/video_imgs/$name
	if [ ! -d "$PTHH"  ];then
		mkdir "$PTHH"
	fi
	ffmpeg -i "$file" -f image2 -vf fps=30 -qscale:v 2 "$PTHH/img_%05d.jpg"
done
