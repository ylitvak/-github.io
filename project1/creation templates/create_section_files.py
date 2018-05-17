# use this to create the SectionXX files in whatever chapter folder you're working in
# copy it into the _sources/ChXX folder, then from a command line run 'python create_section_files.py'
# --- Make sure to change the NUM_SECTIONS to the number of sections you actually need (which 
# 		can be determined via the number of transcripts in the kbai-ebook github)
NUM_SECTIONS = None

for _ in range(1, NUM_SECTIONS):
	with open('Section%02d.rst'%_, 'a+') as f:
		pass