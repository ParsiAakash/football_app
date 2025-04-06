from app.models import Team, Player, Match, Area
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team
        include_fk = True

class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        include_fk = True

class MatchSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Match
        include_fk = True

class AreaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Area
