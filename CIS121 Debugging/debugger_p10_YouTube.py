def like_or_dislike(events):
	state = ''
	
	for event in events:
		if event != state:
			state = event
		elif event == state:
			state = 'Nothing'
	return state


print(like_or_dislike(['like','dislike','like']))