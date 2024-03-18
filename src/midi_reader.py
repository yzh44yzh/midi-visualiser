import mido

class NoteEvent():

    def __init__(self, note, velocity, duration):
        self.note = note
        self.velocity = velocity
        self.duration = duration

    def __repr__(self):
        return f'NoteEvent({self.note}, {self.velocity}, {self.duration})'        


class MidiFileParser():

    def __init__(self, filepath):
        print(filepath)
        self.mf = mido.MidiFile(filepath, type=1)
        print(f'ticks_per_beat: {self.mf.ticks_per_beat}, length: {self.mf.length}')
        self.tempo = self.get_tempo()

    def show_time_signature(self, msg):
        print(f'{msg.numerator}/{msg.denominator}, clocks_per_click:{msg.clocks_per_click}')

    def show_tempo(self, msg):
        print(f'tempo:{msg.tempo} bpm:{mido.tempo2bpm(msg.tempo)}')

    def get_tempo(self):
        for track in self.mf.tracks:
            for msg in track:
                if msg.type == 'time_signature':
                    self.show_time_signature(msg)
                elif msg.type == 'set_tempo':
                    self.show_tempo(msg)
                    return msg.tempo

    def show_notes(self, track_num):
        track = self.mf.tracks[track_num]
        print(f'Track {track.name}')
        for msg in track:
            if msg.type == 'note_on':
                print(msg)

    def get_events(self, track_num=0):
        track = self.mf.tracks[track_num]
        events = []
        curr_note = None

        for msg in track:
            if msg.type == 'note_on':
                if msg.velocity > 0:
                    if curr_note:
                        # ignore accords
                        continue
                    else:
                        curr_note = NoteEvent(msg.note, msg.velocity, None)
                elif msg.velocity == 0:
                    # Actually it should be 'note_off', but MuseScore generates 'note_on' with zero velocity
                    if curr_note:
                        curr_note.duration = mido.tick2second(msg.time, self.mf.ticks_per_beat, self.tempo)
                        events.append(curr_note)
                        curr_note = None
                    elif msg.time != 0:
                        raise Exception(f'unexpected msg {msg}')
                    else:
                        # ignore accords
                        pass
                else: 
                    raise Exception(f'unexpected msg {msg}')

        return events

# To run it on Windows use
# python -X utf8 midi_reader.py

if __name__ == '__main__':
    mfp = MidiFileParser('../midi/Cold_Forest_2.mid')
    events = mfp.get_events(0)
    print(events)
    
