#get track info
#add new tracks here! For example: "execute if score timer ambient matches 0 if score track ambient matches 2 run function gd:ambient/my_new_track_02"
execute if score timer ambient matches 0 if score track ambient matches 1 run function gd:ambient/my_new_ambient_track


#countdown
execute unless score pause ambient matches 1 if score timer ambient matches 1.. run scoreboard players remove timer ambient 1

#increment ambient segment and repeat
execute if score timer ambient matches 0 run scoreboard players add segment ambient 1