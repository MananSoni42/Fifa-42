"""
Manage game statistics

Currently tracks:

- Possession
- Number of goals scored
- Pass accuracy
- Shot accuracy  
"""

class Stats(object):
    """
    Keep track of game statistics
    """

    def __init__(self):
        """
        Initializes the possession, pass accuracy and shot accuracy
        """
        self.pos = { 1: 0, 2: 0 }
        self.goals = { 1: 0, 2: 0 }
        self.pass_acc = {
            1: {
                'succ': 0,
                'fail': 0
            },
            2: {
                'succ': 0,
                'fail': 0
            },
        }
        self.shot_acc = {
            1: {
                'succ': 0,
                'fail': 0
            },
            2: {
                'succ': 0,
                'fail': 0
            },
        }

    def get_possession(self):
        """
        Return a tuple containing the current possesion (between 0 and 1) for each team

        It is rounded to 2 decimal places and their sum is guaranteed to be 1
        """
        if self.pos[1] + self.pos[2] == 0:
            team1_pos = 0.5
        else:
            team1_pos = round(self.pos[1]/(self.pos[1]+self.pos[2]),2)
        return team1_pos, 1-team1_pos

    def get_pass_acc(self):
        """
        Return a tuple containing the current pass accuracy (between 0 and 1) for each team

        It is rounded to 2 decimal places
        """
        if self.pass_acc[1]['succ'] + self.pass_acc[1]['fail'] == 0:
            team1_pass = 0
        else:
            team1_pass = round(self.pass_acc[1]['succ']/(self.pass_acc[1]['succ']+self.pass_acc[1]['fail']),2)

        if self.pass_acc[2]['succ'] + self.pass_acc[2]['fail'] == 0:
            team2_pass = 0
        else:
            team2_pass = round(self.pass_acc[2]['succ']/(self.pass_acc[2]['succ']+self.pass_acc[2]['fail']),2)

        return team1_pass, team2_pass

    def get_shot_acc(self):
        """
        Return a tuple containing the current shot accuracy (between 0 and 1) for each team

        It is rounded to 2 decimal places
        """
        if self.shot_acc[1]['succ'] + self.shot_acc[1]['fail'] == 0:
            team1_shot = 0
        else:
            team1_shot = round(self.shot_acc[1]['succ']/(self.shot_acc[1]['succ']+self.shot_acc[1]['fail']),2)

        if self.shot_acc[2]['succ'] + self.shot_acc[2]['fail'] == 0:
            team2_shot = 0
        else:
            team2_shot = round(self.shot_acc[2]['succ']/(self.shot_acc[2]['succ']+self.shot_acc[2]['fail']),2)

        return team1_shot, team2_shot
