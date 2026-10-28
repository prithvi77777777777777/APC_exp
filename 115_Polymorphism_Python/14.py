class Media:
    def play(self): print("Playing media")
class Audio(Media):
    def play(self): print("Playing audio")
class Video(Media):
    def play(self): print("Playing video")
class Podcast(Media):
    def play(self): print("Playing podcast")
for m in [Audio(), Video(), Podcast()]: m.play()
