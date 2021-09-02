def tournamentWinner(competitions, results):
    competitions_length = len(competitions)
	results_length = len(results)
	
	scores = {}
	results_index = 0
	
	for teams in competitions:
		if teams[0] not in scores:
			scores[teams[0]] = 0
		if teams[1] not in scores:
			scores[teams[1]] = 0
		
		if results[results_index] == 0:
			scores[teams[1]] += 3
		elif results[results_index] == 1:
			scores[teams[0]] += 3
			
		results_index += 1
		
	max_scoring_team = None
	max_score = None
	
	for score in scores:
		if max_scoring_team is None:
			max_scoring_team = score
			max_score = scores[score]
		else:
			if max_score < scores[score]:
				max_scoring_team = score
				max_score = scores[score]
    return max_scoring_team
