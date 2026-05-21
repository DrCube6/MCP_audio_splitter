# MCP Audio Splitter
Minecraft Playsound Audio Splitter is a tool designed to avoid the limitations of Minecraft's playsound command. It allows for dynamic fading and seamless transitions between long audio tracks directly in the game. This is useful for creating dynamic ambient and music tracks. 

### Supports
* Custom fade and hold durations of split tracks.
* Custom resource pack directory for audio.json sound declaration.
* Custom Minecraft Audio Channel (master, player, etc.)
* Up to 3 additional layers for multi-layered tracks
* Looping tracks

### Requirements
* Python
* Pydub
* Datapack
* Resource pack

### Theory
To bypass Minecraft's playsound fading limitation and add dynamic audio tracks to our maps, we need to render audio segments with fades already present. Below is a diagram of what this tool does.
<img width="1005" height="369" alt="MCP_01" src="https://github.com/user-attachments/assets/73c26bb8-e8c5-442f-8090-af021c2b625d" />


If we split the input track into segments with linear fades on either end and play these segments so that each starting fade overlaps with each ending fade, then the perceived loudness will remain unchanged despite individual volume fluctuation. 
If we want to stop a track dynamically, all we have to do is stop the later segment from playing to reveal the hidden fade-out of the current segment.

A limitation of this method is the inability to fade audio precisely. Instead, we will have to wait for the hold duration to finish before getting to the ending fade duration. However, this is incredibly useful in creating natural fade-outs and seamless transitions between different tracks.
<img width="1028" height="440" alt="MCP_02" src="https://github.com/user-attachments/assets/c0437bca-1ac5-4a94-96cf-f6383db46bb8" />


### How to use script
* main.py is a Python script that can be run however you choose. I personally use PyCharm.
* Make sure to install the pydub package.
* **Inputs**: .mp3 file
* **Outputs**: Split .ogg files, Minecraft's audio.json for sound declaration in resource pack, and a .mcfunction file to control these sounds in-game via datapack.

### Resource pack setup
* After splitting a track, place the generated audio.json here: "<resource_pack_name>/assets/minecraft/audio.json"
* To format the audio.json correctly, open the .json and replace the first closed brace and comma with an open brace.
* <img width="301" height="117" alt="image" src="https://github.com/user-attachments/assets/6e968237-fc24-4cef-802b-8cfcc287676e" />


* Finally, add 2 closing braces at the end.
* <img width="107" height="106" alt="image" src="https://github.com/user-attachments/assets/263ed3fa-df07-4760-acb4-0e36206973c1" />


* Create the directory, "<resource_pack_name>/assets/minecraft/sounds/<track_type>/<track_name>" and place the rendered audio segments here. (i.e., track_name_1, _2, etc.)

### Datapack setup
* Once you clone the repository, there is a folder titled *example_datapack*. In this folder, you will find a blank setup of what we need to control these audio segments.
* Go to "example_datapack/data/gd/function/music" and place the generated .mcfunction file from the Python script.
* Make sure the music folder, in this case, is renamed to the <track_type> that you chose during the generation phase. Whether that be music, ambient, or any other category you might want to add.
* Finally, go to the "example_datapack/data/gd/function/loaders/music.mcfunction" file and change or add the generated .mcfunction file's path to this list. For example, "execute if score timer music matches 0 if score track music matches 2 run function gd:music/my_new_track_02"
* To start a track, explore the start_my_new_track.mcfunction file. Make sure, if you added a new track, (i.e. my_new_track_02) and changed the "track music" scoreboard to 2, you need to make sure to also set "track music" to 2 in the start function to target the right track (i.e., scoreboard players set track music 1, 2, 3...)
* To stop a track, use the stop_my_new_track.mcfunction file or use "scoreboard players set track music 0"

### Multi-layered tracks
This feature is incredibly useful if you want to toggle multiple instruments on or off while a song is playing. 
<img width="1095" height="686" alt="MCP_05" src="https://github.com/user-attachments/assets/2a5d3f8c-7758-4be8-b3df-5c38bb767933" />


This feature supports a maximum of 4 individual layers. First, render the song with your instruments separated into individual .mp3 files. Put all .mp3 files into the Python script's home directory. 
* Once you run the main.py script, select "layered track", select the number of additional layers on top of the first layer (0-2), and you will be prompted to input the file names of your previously separated .mp3 files.
* The script will handle the splitting of all layers, the audio.json, and the .mcfunction file.
* Follow the steps mentioned above to set up the datapack and resource pack properly.
* Once this is complete, you can control the layers through these commands:
* **On**: "scoreboard players set layer_0 music 1"
* **Off**: "scoreboard players set layer_0 music 0"
* Available layers: "layer_0", "layer_1", ... "layer_2"
