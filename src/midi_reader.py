import mido

# To run it on Windows use
# python -X utf8 midi_reader.py

mid = mido.MidiFile('../midi/Cold_Forest_2.mid', type=1)

for track in mid.tracks:
    print(f'Track {track.name}')
    for msg in track:
        print(msg)
