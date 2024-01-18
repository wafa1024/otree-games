
from otree.api import *
c = cu

doc = 'A pure coordination game.\n'
class Constants(BaseConstants):
    name_in_url = 'Coord_map_into'
    players_per_group = None
    num_rounds = 1
    instructions_template = 'Coord_map_into/instructions.html'
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
        if player.decision == "D":
            player.payoff = Constants.match_low_payoff
        else:
            player.payoff = Constants.match_high_payoff
    else:
        player.payoff = Constants.no_match_payoff
    
class Player(BasePlayer):
    decision = models.StringField(choices=[['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D'], ['E', 'E'], ['F', 'F'], ['G', 'G'], ['H', 'H']], doc='This player s decision', widget=widgets.RadioSelect)
class Introduction(Page):
    form_model = 'player'
    timeout_seconds = 100
page_sequence = [Introduction]