
from otree.api import *
c = cu

doc = 'A public goods game\n'
class Constants(BaseConstants):
    name_in_url = 'Public_Goods_Game'
    players_per_group = None
    num_rounds = 5
    multiplier = 2
    endowment = 10
    instructions_template = 'Public_Goods_Game/instructions.html'
def creating_session(subsession):
    session = subsession.session
    subsession.group_randomly()
class Subsession(BaseSubsession):
    pass
def set_payoffs(group):
    session = group.session
    
    players = group.get_players()
    
    contributions = [p.contribution for p in players]
    
    group.total_contribution = sum(contributions)
    
    group.individual_share = group.total_contribution * Constants.multiplier / session.num_participants
    
    for p in group.get_players():
        set_payoff(p)
class Group(BaseGroup):
    individual_share = models.CurrencyField()
    total_contribution = models.CurrencyField()
def set_payoff(player):
    group = player.group
    player.payoff = Constants.endowment - player.contribution + group.individual_share
class Player(BasePlayer):
    contribution = models.IntegerField(max=Constants.endowment, min=0)
class Introduction(Page):
    form_model = 'player'
    timeout_seconds = 100
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player):
        maximum_score = Constants.multiplier * Constants.endowment
        
        return dict(
            maximum_score = maximum_score
        )
class Decision(Page):
    form_model = 'player'
    form_fields = ['contribution']
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
class Results(Page):
    form_model = 'player'
page_sequence = [Introduction, Decision, ResultsWaitPage, Results]