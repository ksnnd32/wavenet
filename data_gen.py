import sys
import mfcc
import glob
import os

audio_dir = sys.argv[1]
feature_dir = sys.argv[2]

audio_files = glob.glob('{}/*.mp3'.format(audio_dir))
print('found {} samples in {}'.format(len(audio_files), audio_dir))

for file in audio_files:
    sample_name = file.split('\\')[-1].split('.')[0]
    if os.path.isfile('{}/{}.csv'.format(feature_dir, sample_name)):
        print('feature exist for {}'.format(sample_name))
        continue
    mfcc_feature = mfcc.get_mfcc(file)
    
    fea_file_name = '{}/{}.csv'.format(feature_dir, sample_name)
    print('writing feature to [ {} ]'.format(fea_file_name))
    with open(fea_file_name, 'w') as f:
        for row in mfcc_feature:
            for col in row:
                f.write('{},'.format(col))
            f.write('\n')

