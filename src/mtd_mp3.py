import eyed3
from eyed3.id3.frames import ImageFrame

from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
from mutagen.id3._frames import USLT

import os

def change_cover(audio, cover_path):
    audio_file = eyed3.load(f'{audio}')

    audio_file.tag.images.set(ImageFrame.FRONT_COVER, open(f'{cover_path}','rb').read(), 'image/jpeg')

    audio_file.tag.save()

    try:
        os.remove(cover_path)
    except OSError as e:
        print(f"Error deleting file '{cover_path}': {e}")


def change_metadata(file_path, author, track_name, lyric):
    # Load the MP3 file
    try:
        audio = EasyID3(file_path)
        
        # Change metadata
        audio['artist'] = author
        audio['title'] = track_name
        audio.save()

        audio = ID3(file_path)
        audio.add(USLT(encoding=3, desc=u'', text=lyric))
        
        audio.save()

        os.remove('lyric.json')
    except FileNotFoundError as fl:
        print(f"Error: {fl}")
