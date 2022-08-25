output_address="/media/amir_shirian/Amir/Datasets/Ego4D"
if [ ! -d $output_address"/data"  ];then
	mkdir $output_address"/data"
fi
if [ ! -d $output_address"/data/wave"  ];then
	mkdir $output_address"/data/wave"
fi

for f in `ls data/videos/`
do
    echo ${f%.*}
    ffmpeg -y -i data/videos/${f} -qscale:a 0 -ac 1 -vn -threads 6 -ar 16000 $output_address/data/wave/${f%.*}.wav -loglevel panic
done

