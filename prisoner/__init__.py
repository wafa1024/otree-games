
from otree.api import *
c = cu

doc = '\nThis is a one-shot "Prisoner\'s Dilemma". Two players are asked separately\nwhether they want to cooperate or defect. Their choices directly determine the\npayoffs.\n'
class Constants(BaseConstants):
    name_in_url = 'prisoner'
    players_per_group = 2
    num_rounds = 1
    betray_payoff = cu(300)
    betrayed_payoff = cu(0)
    both_cooperate_payoff = cu(200)
    both_defect_payoff = cu(100)
    instructions_template = 'prisoner/instructions.html'
class Subsession(BaseSubsession):
    pass
def set_payoffs(group):
    for p in group.get_players():
        set_payoff(p)
class Group(BaseGroup):
    pass
def other_player(player):
    group = player.group
    return player.get_others_in_group()[0]
def set_payoff(player):
    payoff_matrix = dict(
        Cooperate=dict(
            Swerve=Constants.both_cooperate_payoff, Continue=Constants.betrayed_payoff
        ),
        Defect=dict(
            Swerve=Constants.betray_payoff, Continue=Constants.both_defect_payoff
        ),
    )
    player.payoff = payoff_matrix[player.decision][other_player(player).decision]
class Player(BasePlayer):
    decision = models.StringField(choices=[['Cooperate', 'Cooperate'], ['Defect', 'Defect']], doc='This player s decision', widget=widgets.RadioSelect)
class Introduction(Page):
    form_model = 'player'
    timeout_seconds = 100
class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Results(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player):
        me = player
        opponent = other_player(me)
        return dict(
            my_decision=me.decision,
            opponent_decision=opponent.decision,
            same_choice=me.decision == opponent.decision,
        )
page_sequence = [Introduction, Decision, ResultsWaitPage, Results]