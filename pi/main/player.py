import vlc

global a

def change_volume(val, a):
    #Popen(['amixer', 'set', 'Master', 'unmute'])
    #amixer -D bluealsa sset "UE BOOM 2 - A2DP" 50%
    a.get_media_player().audio_set_volume(val)
    #p.audio_set_volume(val)
    #Popen(['amixer','-D','bluealsa', 'sset', '"UE BOOM 2 - A2DP"', '{}%'.format(val)],stdout=open(os.devnull, 'wb'))	


def play_station(s, a_old, p=Player, media_list=media_list):
	a=p.media_list_player_new() #['station_name_voices/{}.wav'.format(s),
	a.set_media_list(media_list[s])
	if a_old is not None:
		a_old.stop()
	a.play()
	return a 
