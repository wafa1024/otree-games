
from otree.api import *
c = cu

doc = 'A pure coordination game.\n'
class Constants(BaseConstants):
    name_in_url = 'Coord_map_3_no_chat'
    players_per_group = None
    num_rounds = 1
    match_each_player_payoff = 1
    start_payoff = 0
    instructions_template = 'Coord_map_3_no_chat/instructions.html'
def creating_session(subsession):
    session = subsession.session
    subsession.group_randomly()
class Subsession(BaseSubsession):
    pass
def set_payoffs(group):
    players = group.get_players()
    
    A1_total = -1
    A2_total = -1
    A3_total = -1
    A4_total = -1
    B1_total = -1
    B2_total = -1
    B3_total = -1
    B4_total = -1
    C1_total = -1
    C2_total = -1
    C3_total = -1
    C4_total = -1
    
    for p in players:
        if p.decision == "A1":
            A1_total = A1_total + 1
        elif p.decision == "A2":
            A2_total = A2_total + 1
        elif p.decision == "A3":
            A3_total = A3_total + 1    
        elif p.decision == "A4":
            A4_total = A4_total + 1
        elif p.decision == "B1":
            B1_total = B1_total + 1        
        elif p.decision == "B2":
            B2_total = B2_total + 1        
        elif p.decision == "B3":
            B3_total = B3_total + 1        
        elif p.decision == "B4":
            B4_total = B4_total + 1        
        elif p.decision == "C1":
            C1_total = C1_total + 1        
        elif p.decision == "C2":
            C2_total = C2_total + 1
        elif p.decision == "C3":
            C3_total = C3_total + 1
        else:
            C4_total = C4_total + 1
    
    for player in players:
        if player.decision == "A1":
            player.payoff = Constants.start_payoff + A1_total * Constants.match_each_player_payoff
        elif player.decision == "A2":
            player.payoff = Constants.start_payoff + A2_total * Constants.match_each_player_payoff
        elif player.decision == "A3":
            player.payoff = Constants.start_payoff + A3_total * Constants.match_each_player_payoff
        elif player.decision == "A4":
            player.payoff = Constants.start_payoff + A4_total * Constants.match_each_player_payoff
        elif player.decision == "B1":
            player.payoff = Constants.start_payoff + B1_total * Constants.match_each_player_payoff
        elif player.decision == "B2":
            player.payoff = Constants.start_payoff + B2_total * Constants.match_each_player_payoff
        elif player.decision == "B3":
            player.payoff = Constants.start_payoff + B3_total * Constants.match_each_player_payoff
        elif player.decision == "B4":
            player.payoff = Constants.start_payoff + B4_total * Constants.match_each_player_payoff
        elif player.decision == "C1":
            player.payoff = Constants.start_payoff + C1_total * Constants.match_each_player_payoff
        elif player.decision == "C2":
            player.payoff = Constants.start_payoff + C2_total * Constants.match_each_player_payoff
        elif player.decision == "C3":
            player.payoff = Constants.start_payoff + C3_total * Constants.match_each_player_payoff
        else:
            player.payoff = Constants.start_payoff + C4_total * Constants.match_each_player_payoff
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    decision = models.StringField(choices=[['A1', 'A1'], ['A2', 'A2'], ['A3', 'A3'], ['A4', 'A4'], ['B1', 'B1'], ['B2', 'B2'], ['B3', 'B3'], ['B4', 'B4'], ['C1', 'C1'], ['C2', 'C2'], ['C3', 'C3'], ['C4', 'C4']], doc='This player s decision', widget=widgets.RadioSelect)
class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Results(Page):
    form_model = 'player'
page_sequence = [Decision, ResultsWaitPage, Results]