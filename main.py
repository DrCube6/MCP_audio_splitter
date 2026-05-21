# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pydub import AudioSegment

global track_type
global audio_channel

def ask_for_filename():
    global song
    global filename
    try:
        filename = str(input("Filename (without file extension): "))
        # load song
        song = AudioSegment.from_file(filename + ".mp3", format="mp3")
        print("completing operation...")
    except:
        print("could not find correct filename in directory")
        ask_for_filename()


def is_layer_track():
    global layer_track
    global layers
    layer_track = str(input("Is this a layer track? (y/n): "))
    if layer_track == 'y':
        layers = int(input("How many additional layers on top of base layer? (1-3): "))
        if layers < 1 or layers > 3:
            print("Invalid amount of layers (1-3), try again.")
            is_layer_track()
    elif layer_track == 'n':
        return
    else:
        print("Invalid Input (y/n), try again.")
        is_layer_track()

def track_loop():
    global loop
    loop = str(input("Does the track loop? (y/n): "))
    if loop == 'y':
        return
    elif loop == 'n':
        return
    else:
        print("Invalid Input (y/n), try again.")
        track_loop()


track_type = str(input("Input track type (ambient/music): "))
audio_channel = str(input("Input audio channel (hostile/player): "))
track_loop()
is_layer_track()
print(f"Input base.mp3 file,")
ask_for_filename()
original_filename = filename

fade_duration = 1.0
hold_duration = 1.0

# open files
mcfunctionfile = open(f"{filename}.mcfunction", "+w")
sound_jsonfile = open("sounds.json", "+w")

# var
num = 0
initial = 0
final = (fade_duration * 2 + hold_duration) * 1000

# GET SOUNDS.JSON AND .MCFUNCTION FILES
while final < len(song):
    final = final + (fade_duration + hold_duration) * 1000
    num = num + 1

    block_mcfunction = [f"\n#segment {str(num)}\n"]
    if layer_track == 'y':

        # SAVE LAYERED TRACK TO SOUNDS.JSON
        i = 0
        while i <= layers:
            block_mcfunction += [
                f"execute if score segment {track_type} matches {str(num)} if score layer_{str(i)} {track_type} matches 1 at @a run playsound {track_type}.{filename}.{filename}_{str(num)}_{str(i)} {audio_channel} @a ~ ~ ~ 1\n"]
            block_sound_json = ['\t}, \n',
                                f'\t"{track_type}.{filename}.{filename}_{str(num)}_{str(i)}": ' + ' {\n',
                                '\t\t"sounds": [\n'
                                f'\t\t\t"{track_type}/{filename}/{filename}_{str(num)}_{str(i)}"\n'
                                '\t\t]\n'
                                ]
            sound_jsonfile.writelines(block_sound_json)
            i += 1
    else:

        block_mcfunction += [
            f"execute if score segment {track_type} matches {str(num)} at @a run playsound {track_type}.{filename}.{filename}_{str(num)} {audio_channel} @a ~ ~ ~ 1\n"]

        # SAVE NON-LAYERED TRACK TO SOUNDS.JSON
        block_sound_json = ['\t}, \n',
                            f'\t"{track_type}.{filename}.{filename}_{str(num)}": ' + ' {\n',
                            '\t\t"sounds": [\n'
                            f'\t\t\t"{track_type}/{filename}/{filename}_{str(num)}"\n'
                            '\t\t]\n'
                            ]
        sound_jsonfile.writelines(block_sound_json)

    # WRITE RETURN BLOCK TO .MCFUNCTION FILE
    block_mcfunction += [
        f"execute if score segment {track_type} matches {str(num)} run scoreboard players set timer {track_type} {int((fade_duration + hold_duration) * 20)}\n",
        f"execute if score segment {track_type} matches {str(num)} run return 0\n"]
    mcfunctionfile.writelines(block_mcfunction)

# WRITE LOOP BLOCK TO .MCFUNCTION FILE
if loop == 'y':
    mcfunctionfile.writelines([
        f"\n#loop\n",
        f"scoreboard players set segment {track_type} 0\n",
        f"scoreboard players set timer {track_type} 0\n",
    ])
else:
    mcfunctionfile.writelines([
        f"\n#loop\n",
        f"scoreboard players set track {track_type} 0\n",
        f"scoreboard players set timer {track_type} 0\n",
        f"scoreboard players set segment {track_type} 1\n",
    ])

if layer_track == 'y':
    i = 0
    while i <= layers:
        if i != 0:
            print(f"Input layer_{str(i)}.mp3 file,")
            ask_for_filename()

        # var
        num = 0
        initial = 0
        final = (fade_duration * 2 + hold_duration) * 1000

        # SPLIT LAYERED TRACK
        while final < len(song):
            # cut and fade
            clip = song[initial:final]
            clip = clip.fade_in(int(fade_duration * 1000)).fade_out(int(fade_duration * 1000))

            # increment
            initial = initial + (fade_duration + hold_duration) * 1000
            final = final + (fade_duration + hold_duration) * 1000
            num = num + 1

            # export clip
            clip.export(original_filename + "_" + str(num) + "_" + str(i) + ".ogg", format="ogg")
            print(f"Exporting {original_filename}_{str(num)}_{str(i)}")

        i += 1
else:
    # SPLIT NON-LAYER TRACK
    num = 0
    initial = 0
    final = (fade_duration * 2 + hold_duration) * 1000
    while final < len(song):
        # cut and fade
        clip = song[initial:final]
        clip = clip.fade_in(int(fade_duration * 1000)).fade_out(int(fade_duration * 1000))

        # increment
        initial = initial + (fade_duration + hold_duration) * 1000
        final = final + (fade_duration + hold_duration) * 1000
        num = num + 1

        # export clip
        clip.export(original_filename + "_" + str(num) + ".ogg", format="ogg")
        print(f"Exporting {original_filename}_{str(num)}")
# end
print("done!")
