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
<img width="1392" height="465" alt="image" src="https://github.com/user-attachments/assets/3ee4fac9-5e39-45f7-8291-d283389bdb7c" />
If we split the input track into segments with linear fades on either end and play these segments so that each starting fade overlaps with each ending fade, then the perceived loudness will remain unchanged despite individual volume fluctuation. 
If we want to stop a track dynamically, all we have to do is stop the later segment from playing to reveal the hidden fade-out of the current segment.

A limitation of this method is the inability to fade audio precisely. Instead, we will have to wait for the hold duration to finish before getting to the ending fade duration. However, this is incredibly useful in creating natural fade-outs and seamless transitions between different tracks.
<img width="1419" height="576" alt="image" src="https://github.com/user-attachments/assets/3fc47925-6a43-4623-b9fb-326f0f50d03e" />

### How to use script
* main.py is a Python script that can be run however you choose. I personally use PyCharm.
* Make sure to install the pydub package.
* **Inputs**: .mp3 file
* **Outputs**: Split .ogg files, Minecraft's audio.json for sound declaration in resource pack, and a .mcfunction file to control these sounds in-game via datapack.

### Resource pack setup
* After splitting a track, place the generated audio.json here: "<resource_pack_name>/assets/minecraft/audio.json"
* To format the audio.json correctly, open the .json and replace the first closed brace and comma with an open brace.
* <img width="290" height="104" alt="image" src="https://github.com/user-attachments/assets/ba10fbda-d6eb-41ab-8117-2720260518db" />
* Finally, add 2 closing braces at the end.
* <img width="138" height="119" alt="image" src="https://github.com/user-attachments/assets/0a88c05e-e8a5-4e3e-9120-c7bc46d790eb" />
* Create the directory, "<resource_pack_name>/assets/minecraft/sounds/<track_type>/<track_name>" and place the rendered audio segments here. (i.e., track_name_1, _2, etc.)

### Datapack setup
* Once you clone the repository, there is a folder titled *Example_datapack*. In this folder, you will find a blank setup of what we need to control these audio segments.
