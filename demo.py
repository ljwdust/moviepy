from moviepy.editor import *
import time


video = VideoFileClip("0.mp4", target_resolution=(1080, 1920)).subclip(0,10)

# Make the text. Many more options are available.
txt_clip = ( TextClip("My Holidays 2013", fontsize=70, color='white')
                     .set_position('center')
                     .set_duration(10)
           )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
tic = time.time()
result.write_videofile("myHolidays_edited.mp4", 
                     #   codec='h264_nvenc', 
                       fps=25
                    ) # Many options...

print(f"Time: {time.time() - tic:.3f}")
