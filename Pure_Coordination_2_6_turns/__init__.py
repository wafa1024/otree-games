
from otree.api import *
c = cu

doc = 'A pure coordination game.\n'
class Constants(BaseConstants):
    name_in_url = 'Pure_Coordination_2_6_turns'
    players_per_group = 2
    num_rounds = 6
    betray_payoff = cu(0)
    betrayed_payoff = cu(0)
    both_cooperate_payoff = cu(10)
    both_defect_payoff = cu(10)
    instructions_template = 'Pure_Coordination_2_6_turns/instructions.html'
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
    payoff_matrix = dict(
        Left=dict(
            Left=Constants.both_cooperate_payoff, Right=Constants.betrayed_payoff
        ),
        Right=dict(
            Left=Constants.betray_payoff, Right=Constants.both_defect_payoff
        ),
    )
    player.payoff = payoff_matrix[player.decision][other_player(player).decision]
class Player(BasePlayer):
    decision = models.StringField(choices=[['Left', 'Left'], ['Right', 'Right']], doc='This player s decision', widget=widgets.RadioSelect)
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