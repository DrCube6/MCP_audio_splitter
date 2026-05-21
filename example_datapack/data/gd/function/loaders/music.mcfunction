#get track info
#add new tracks here! For example: "execute if score timer music matches 0 if score track music matches 2 run function gd:music/my_new_track_02"
execute if score timer music matches 0 if score track music matches 1 run function gd:music/my_new_track


#countdown
execute unless score pause music matches 1 if score timer music matches 1.. run scoreboard players remove timer music 1

#increment music segment and repeat
execute if score timer music matches 0 run scoreboard players add segment music 1