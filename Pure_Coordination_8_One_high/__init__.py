
from otree.api import *
c = cu

doc = 'A pure coordination game.\n'
class Constants(BaseConstants):
    name_in_url = 'Pure_Coordination_8_One_high'
    players_per_group = 2
    num_rounds = 1
    match_high_payoff = 10
    match_low_payoff = 5
    no_match_payoff = 0
    instructions_template = 'Pure_Coordination_8_One_high/instructions.html'
def creating_session(subsession):
    session = subsession.session
    subsession.group_randomly()
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
    if player.decision == other_player(player).decision:
        if player.decision == "F":
            player.payoff = Constants.match_high_payoff
        else:
            player.payoff = Constants.match_low_payoff
    else:
        player.payoff = Constants.no_match_payoff
    
class Player(BasePlayer):
    decision = models.StringField(choices=[['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D'], ['E', 'E'], ['F', 'F'], ['G', 'G'], ['H', 'H']], doc='This player s decision', widget=widgets.RadioSelect)
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