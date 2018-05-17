'''
Creates all files, copying transcripts and section headers into the appropriate format
Don't need to move from the creation templates folder; just adjust the two variables below and run

To do after running:
- Section 1 still needs sphere / quotes
- copy slides / etc. into _static
- exercises / readings / etc..
'''
# Two variables which need to be set *exactly*:
folder = '26 - Wrap-Up' # Can find this in kbai-ebook/tex/transcripts/transcripts_raw/ if unsure
path_to_ebook = '../../../kbai-ebook-master/tex/'
# --------------------------------


from glob import glob
import os 

assert(os.path.exists('../_sources/')), 'Can\'t find _sources folder; is the script still in creation templates?'

chapter_num   = folder.split(' - ')[0]
chapter_title = folder.split(' - ')[1] 
path_to_transcripts = path_to_ebook + 'transcripts/transcripts_raw/' + folder
path_to_videos = path_to_ebook + 'videos/%s*.txt' % chapter_num
transcripts = glob(path_to_transcripts + '/*.srt')
path_to_transcripts += '/clean/'
path_to_chapter = '../_sources/Ch%s'%chapter_num

# Create cleaned transcripts
if not os.path.exists(path_to_transcripts): 
	os.mkdir(path_to_transcripts)
num_sections = len(list(transcripts))
for filename in transcripts:
	with open(filename) as f:
		lines = f.readlines()
		text = []
		for line in lines:
			if line.strip() and len(line.strip()) > 3 and '-->' not in line:
				text.append(line.replace('>>','').strip())

		transcript = ' '.join(text).replace('  ', ' ')
		with open(path_to_transcripts + filename.split('\\')[-1], 'w+') as f2:
			f2.write(transcript)


# Create SectionXX files
if not os.path.exists(path_to_chapter):
	os.mkdir(path_to_chapter)

videos = open(list(glob(path_to_videos))[0]).readlines()
videos = {i:v.split('watch?v=')[1].split('&')[0] for i,v in enumerate(videos)}

for transcript in glob(path_to_transcripts + '*.srt'):
	sect_num  = transcript.split(' - ')[-2][-2:]
	sect_name = transcript.split(' - ')[-1].replace('.srt','')
	vid_path  = videos[int(sect_num)-1]
	if 'final quiz' in sect_name.lower(): continue
	with open(path_to_chapter + '/Section%s.rst'%sect_num, 'w+') as f:
		title = 'Section %s: %s' % (sect_num, sect_name)
		f.write(title + '\n')
		f.write(''.join([':']*len(title)) + '\n')
		f.write('\n')
		f.write('.. youtube:: %s\n'%vid_path)
		f.write('        :height: 315\n')
		f.write('        :width: 560\n')
		f.write('        :align: left\n')
		f.write('\n')
		f.write(open(transcript).read() + '\n')
		f.write('\n')

# Create toc file
with open('../_sources/CH%s_%s.rst' % (chapter_num, chapter_title.replace(' ', '')), 'w+') as f:
	f.write(chapter_title + '\n')
	f.write(''.join(['-']*len(chapter_title)) + '\n')
	f.write('\n')
	f.write('.. toctree::\n')
	f.write('        :caption: Index\n')
	f.write('        :maxdepth: 2\n')
	f.write('        :glob:\n')
	f.write('\n\n')
	f.write('        Ch%s/*'%chapter_num)

# Add to Index
lines = open('../_sources/index.rst', 'r').readlines() 
for i,line in enumerate(lines):
	if 'CH' in line and '.rst' in line:
		idx = i
		ch_num = int(line.strip().split('_')[0].strip('CH'))
		if ch_num == int(chapter_num):
			assert(0), 'Chapter already in index; script is finished' 
		elif ch_num > int(chapter_num):
			idx = i - 1
			break
idx += 1
lines = lines[:idx] + ['        CH%s_%s.rst\n'%(chapter_num, chapter_title.replace(' ',''))] + lines[idx:]

with open('../_sources/index.rst', 'w+') as f:
	for line in lines:
		f.write(line)
