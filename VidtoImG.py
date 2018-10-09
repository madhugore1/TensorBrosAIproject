import subprocess as sp
count = 1
count1 = 1
for i in range(4):
	cmd='ffmpeg -i ' + dancetest+ '.mp4 -r 1 -s 224x224 -f image2 '+str(count)+str(count1)+'%d.jpeg'
	sp.call(cmd,shell=True)
	count1+=1
