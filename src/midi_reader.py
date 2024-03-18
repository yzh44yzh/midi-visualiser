import mido

class NoteEvent():

    def __init__(self, note, velocity, duration):
        self.note = note
        self.velocity = velocity
        self.duration = duration
        self.time = None

    def __repr__(self):
        return f'NoteEvent({self.note}, {self.velocity}, {self.duration})'


class MidiFileParser():

    def __init__(self, filepath, bpm):
        print(filepath)
        self.mf = mido.MidiFile(filepath, type=1)
        self.tempo = mido.bpm2tempo(bpm)
        print(f'ticks_per_beat: {self.mf.ticks_per_beat}, bpm: {bpm}, tempo: {self.tempo}, length: {self.mf.length}')

    def show_time_signature(self, msg):
        print(f'{msg.numerator}/{msg.denominator}, clocks_per_click:{msg.clocks_per_click}')

    def show_all(self):
        for track in self.mf.tracks:
            for msg in track:
                if msg.type == 'note_off':
                    duration = mido.tick2second(msg.time, self.mf.ticks_per_beat, self.tempo)
                    print(msg, duration)
                else:
                    print(msg)

    def get_events(self, track_num=0):
        track = self.mf.tracks[track_num]
        events = []
        curr_note = None

        for msg in track:
            if msg.type == 'note_on':
                if curr_note:
                    # ignore accords
                    continue
                else:
                    curr_note = NoteEvent(msg.note, msg.velocity, None)

            if msg.type == 'note_off':
                if curr_note:
                    curr_note.duration = mido.tick2second(msg.time, self.mf.ticks_per_beat, self.tempo)
                    events.append(curr_note)
                    curr_note = None
                else:
                    # ignore accords
                    pass

        return events

# To run it on Windows use
# python -X utf8 midi_reader.py

if __name__ == '__main__':
    mfp = MidiFileParser('../midi/cold_forest_2_voice_1.mid', 105)
    # print(mfp.show_all())
    events = mfp.get_events(0)
    print(events)
