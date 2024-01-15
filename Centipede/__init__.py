
from otree.api import *
c = cu

doc = '\nThis is the centipede game. Two players take turns deciding whether to continue or accept the payoff.\n'
class Constants(BaseConstants):
    name_in_url = 'Centipede'
    players_per_group = 2
    num_rounds = 6
    p1_payoff_1 = 1
    p1_payoff_2 = 0
    p1_payoff_3 = 3
    p1_payoff_4 = 2
    p1_payoff_5 = 4
    p1_payoff_6 = 3
    p2_payoff_1 = 0
    p2_payoff_2 = 2
    p2_payoff_3 = 1
    p2_payoff_4 = 4
    p2_payoff_5 = 3
    p2_payoff_6 = 5
    instructions_template = 'Centipede/instructions.html'
def creating_session(subsession):
    session = subsession.session
    subsession.group_randomly()
class Subsession(BaseSubsession):
    pass
def set_payoffs(group):
    for p in group.get_players():
        set_payoff(p)
class Group(BaseGroup):
    p1_choice_1 = models.StringField(choices=[['Continue', 'Continue'], ['Stop', 'Stop']], initial='Stop')
    p2_choice_2 = models.StringField(choices=[['Continue', 'Continue'], ['Stop', 'Stop']], initial='Stop')
    p1_choice_3 = models.StringField(choices=[['Continue', 'Continue'], ['Stop', 'Stop']], initial='Stop')
    p2_choice_4 = models.StringField(choices=[['Continue', 'Continue'], ['Stop', 'Stop']], initial='Stop')
    p1_choice_5 = models.StringField(choices=[['Continue', 'Continue'], ['Stop', 'Stop']], initial='Stop')
def other_player(player):
    group = player.group
    return player.get_others_in_group()[0]
def set_payoff(player):
    group = player.group
    if player.id_in_group == 1:
        if group.p1_choice_1 == "Stop":
            player.payoff = Constants.p1_payoff_1
        elif group.p2_choice_2 == "Stop":
            player.payoff = Constants.p1_payoff_2
        elif group.p1_choice_3 == "Stop":
            player.payoff = Constants.p1_payoff_3
        elif group.p2_choice_4 == "Stop":
            player.payoff = Constants.p1_payoff_4
        elif group.p1_choice_5 == "Stop":
            player.payoff = Constants.p1_payoff_5
        else:
            player.payoff = Constants.p1_payoff_6
    else:
        if group.p1_choice_1 == "Stop":
            player.payoff = Constants.p2_payoff_1
        elif group.p2_choice_2 == "Stop":
            player.payoff = Constants.p2_payoff_2
        elif group.p1_choice_3 == "Stop":
            player.payoff = Constants.p2_payoff_3
        elif group.p2_choice_4 == "Stop":
            player.payoff = Constants.p2_payoff_4
        elif group.p1_choice_5 == "Stop":
            player.payoff = Constants.p2_payoff_5
        else:
            player.payoff = Constants.p2_payoff_6    
class Player(BasePlayer):
    pass
class Introduction(Page):
    form_model = 'player'
    timeout_seconds = 100
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
class Player1_Choice_1(Page):
    form_model = 'group'
    form_fields = ['p1_choice_1']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 1
class WaitForP1C1(WaitPage):
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 2
class Player2_Choice_2(Page):
    form_model = 'group'
    form_fields = ['p2_choice_2']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 2 and group.p1_choice_1 == "Continue"
class WaitForP2C2(WaitPage):
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 1 and group.p1_choice_1 == "Continue"
class Player1_Choice_3(Page):
    form_model = 'group'
    form_fields = ['p1_choice_3']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 1 and group.p2_choice_2 == "Continue"
class WaitForP1C3(WaitPage):
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 2 and group.p2_choice_2 == "Continue"
class Player2_Choice_4(Page):
    form_model = 'group'
    form_fields = ['p2_choice_4']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 2 and group.p1_choice_3 == "Continue"
class WaitForP2C4(WaitPage):
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 1 and group.p1_choice_3 == "Continue"
class Player1_Choice_5(Page):
    form_model = 'group'
    form_fields = ['p1_choice_5']
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 1 and group.p2_choice_4 == "Continue"
class WaitForP1C5(WaitPage):
    @staticmethod
    def is_displayed(player):
        group = player.group
        return player.id_in_group == 2 and group.p2_choice_4 == "Continue"
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Results(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player):
        group = player.group
        if group.p1_choice_1 == "Stop":
            ender = 1
            end_round = 1
            end_decision = "Stop"
        elif group.p2_choice_2 == "Stop":
            ender = 2
            end_round = 2
            end_decision = "Stop"
        elif group.p1_choice_3 == "Stop":
            ender = 1
            end_round = 3
            end_decision = "Stop"
        elif group.p2_choice_4 == "Stop":
            ender = 2
            end_round = 4
            end_decision = "Stop"
        elif group.p1_choice_5 == "Stop":
            ender= 1
            end_round = 5
            end_decision = "Stop"
        else:
            ender = 1
            end_round = 5
            end_decision = "Continue"
        
        
        return dict(
            ender=ender,
            end_round = end_round,
            end_decision = end_decision,
        )
page_sequence = [Introduction, Player1_Choice_1, WaitForP1C1, Player2_Choice_2, WaitForP2C2, Player1_Choice_3, WaitForP1C3, Player2_Choice_4, WaitForP2C4, Player1_Choice_5, WaitForP1C5, ResultsWaitPage, Results]