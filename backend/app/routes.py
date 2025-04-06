from flask import Blueprint, jsonify, request
from app.database import db
from app.models import Match, Team, Player, Area
from app.schemas import MatchSchema, TeamSchema, PlayerSchema, AreaSchema

api_bp = Blueprint('api', __name__)

match_schema = MatchSchema(many=True)
team_schema = TeamSchema(many=True)
player_schema = PlayerSchema(many=True)
area_schema = AreaSchema(many=True)

@api_bp.route('/matches')
def get_matches():
    area = request.args.get('area')
    team_id = request.args.get('team_id')
    query = Match.query
    if area:
        query = query.join(Area).filter(Area.name == area)
    if team_id:
        query = query.filter((Match.home_team_id == team_id) | (Match.away_team_id == team_id))
    return jsonify(match_schema.dump(query.all()))

@api_bp.route('/teams')
def get_teams():
    return jsonify(team_schema.dump(Team.query.all()))

@api_bp.route('/players')
def get_players():
    team_id = request.args.get('team_id')
    query = Player.query
    if team_id:
        query = query.filter_by(team_id=team_id)
    return jsonify(player_schema.dump(query.all()))

@api_bp.route('/areas')
def get_areas():
    return jsonify(area_schema.dump(Area.query.all()))
