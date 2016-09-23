import numpy
from moviepy.editor import *
from wand.image import Image as wandImage

clips = []

# Length in seconds of every slide
durations = [2, 27, 30, 23, 43, 50, 64, 51, 17, 108, 10, 10]


with wandImage(filename="ML2-VDD.pdf", resolution=300) as img:
    # I think this is a feature, using [0] actualy converts all the sequence
    img.sequence[0].container.save(filename='slide.jpg')
    for i in img.sequence:
        clips.append(ImageClip('slide-%d.jpg' % i.index)
         .set_duration(durations[i.index]).fadein(1).fadeout(1))

audio = AudioFileClip("talk.mp3")

final = concatenate_videoclips(clips).set_audio(audio)
final.write_videofile("movie.mp4", fps=24)
