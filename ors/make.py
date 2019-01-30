import os
import sys
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))

file_mp3_1 =  current_dir + '\\1.mp3'
file_mp3_2 =  current_dir + '\\2.mp3'
file_ffmpeg = current_dir + '\\bin\\ffmpeg.exe'
file_fr =     current_dir + '\\bin\\fr.exe'

file_wav_1 = '\\1.wav'
file_wav_2 = '\\2.wav'

p1 = os.path.isfile(file_mp3_1)
p2 = os.path.isfile(file_mp3_2)
p3 = os.path.isfile(file_ffmpeg)
p4 = os.path.isfile(file_fr)

if not p1 or not p2 or not p3 or not p4:
   print('no files')
   sys.exit()

def make_ffmpeg_arg(name):   
   args = current_dir + '\\bin\\ffmpeg -v 0 -i "' + \
          current_dir + '\\{}.mp3" -f wav -ar 8000 -ac 1 -acodec pcm_u8 - > "'.format(name) + \
          current_dir + '\\{}.wav"'.format(name)
   return args

print(make_ffmpeg_arg('1'))

s1 = subprocess.call(make_ffmpeg_arg('1'), shell=True)
print('sub1:', s1)
s2 = subprocess.call(make_ffmpeg_arg('2'), shell=True)
print('sub1:', s2)

p1 = os.path.isfile('./'+file_wav_1)
p2 = os.path.isfile('./'+file_wav_2)

if not p1 or not p2:
   sys.exit()


args = current_dir + '\\bin\\fr "' + current_dir + '\\1.wav" "' + current_dir + '\\2.wav" ' + current_dir + '\\result\\result.wav'

subprocess.call(args)

# Clear garbage
delete = []
delete.append(current_dir + '\\1.wav')
delete.append(current_dir + '\\2.wav')
delete.append(current_dir + '\\t.txt')

ctrl = input("Delete source files? y/n\n")
if ctrl == 'y':
   delete.append(current_dir + '\\1.mp3')
   delete.append(current_dir + '\\2.mp3')
   
for item in delete:
   os.remove(item)