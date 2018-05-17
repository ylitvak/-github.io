'''
Use this to clean up the transcript files into one long paragraph per section
Copy it into kbai-ebook/tex/transcripts/transcripts_raw/ and then change the 
<folder> variable below to reflect the folder you want to generate transcripts 
for.

- May need to play with folder paths (i.e. '/' symbols) if not using windows; linux
	uses a slightly different scheme which I haven't tested this script with
'''

from glob import glob
import os 

folder = '10 - Incremental Concept Learning'
if not os.path.exists(folder + '/clean/'): os.mkdir(folder + '/clean/')

for filename in glob(folder + '/*.srt'):
	with open(filename) as f:
		lines = f.readlines()
		text = []
		for line in lines:
			if line.strip() and len(line.strip()) > 3 and '-->' not in line:
				text.append(line.replace('>>','').strip())

		transcript = ' '.join(text).replace('  ', ' ')
		with open(folder + '/clean/' + filename.split('\\')[-1], 'w+') as f2:
			f2.write(transcript)
