# seed.py
from app import create_app, db
from app.models import Area, Team, Player, Match

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Add Area
    london = Area(name="London")
    madrid = Area(name="Madrid")
    db.session.add_all([london, madrid])
    db.session.commit()

    # Add Teams
    arsenal = Team(name="Arsenal", area_id=london.id)
    chelsea = Team(name="Chelsea", area_id=london.id)
    real = Team(name="Real Madrid", area_id=madrid.id)
    db.session.add_all([arsenal, chelsea, real])
    db.session.commit()

    # Add Players
    players = [
        Player(name="Saka", team_id=arsenal.id),
        Player(name="Odegaard", team_id=arsenal.id),
        Player(name="Sterling", team_id=chelsea.id),
        Player(name="Modric", team_id=real.id),
    ]
    db.session.add_all(players)
    db.session.commit()

    # Add Match
    match = Match(
        date="2025-04-08",
        home_team_id=arsenal.id,
        away_team_id=chelsea.id,
        area_id=london.id
    )
    db.session.add(match)
    db.session.commit()

    print("✅ Database seeded successfully!")
