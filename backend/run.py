from app import create_app, db
from app.models import Area, Team, Player, Match

app = create_app()

with app.app_context():
    db.create_all()  # Auto creates DB tables
    if not Area.query.first():
        area = Area(name="London")
        team1 = Team(name="Arsenal", area=area)
        team2 = Team(name="Chelsea", area=area)
        player1 = Player(name="Saka", team=team1)
        player2 = Player(name="Sterling", team=team2)
        match = Match(date="2025-04-08", home_team_id=team1.id, away_team_id=team2.id, area=area)
        db.session.add_all([area, team1, team2, player1, player2, match])
        db.session.commit()

if __name__ == "__main__":
    app.run(host="localhost", port=5002)
    
