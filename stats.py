class Stats(object):
    """Keep track of game statistics"""

    def __init__(self):
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
        if self.pos[1] + self.pos[2] == 0:
            team1_pos = 0.5
        else:
            team1_pos = round(self.pos[1]/(self.pos[1]+self.pos[2]),2)
        return team1_pos, 1-team1_pos

    def get_pass_acc(self):
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
        if self.shot_acc[1]['succ'] + self.shot_acc[1]['fail'] == 0:
            team1_shot = 0
        else:
            team1_shot = round(self.shot_acc[1]['succ']/(self.shot_acc[1]['succ']+self.shot_acc[1]['fail']),2)

        if self.shot_acc[2]['succ'] + self.shot_acc[2]['fail'] == 0:
            team2_shot = 0
        else:
            team2_shot = round(self.shot_acc[2]['succ']/(self.shot_acc[2]['succ']+self.shot_acc[2]['fail']),2)

        return team1_shot, team2_shot
