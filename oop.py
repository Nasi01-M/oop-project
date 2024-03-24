def calculate_score(participant):
    """Calculate the score for a participant based on their consumed items."""
    # Each chicken wing is worth 5 points, each hamburger is worth 3 points, and each hot dog is worth 2 points
    return participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2

def create_scoreboard(participants):
    """Create a scoreboard for the given participants."""
    scoreboard = []
    # Calculate score for each participant and store it along with their name
    for participant in participants:
        score = calculate_score(participant)
        scoreboard.append({'name': participant['name'], 'score': score})
    
    # Sort the scoreboard by score (in descending order) and then alphabetically by name
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    
    return scoreboard

# Example usage:
participants = [
  {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
  {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

# Generate and display the scoreboard
scoreboard = create_scoreboard(participants)
print(scoreboard)
