from app import create_app, db

def test_teams_endpoint():
    app = create_app()
    client = app.test_client()
    response = client.get('/api/teams')
    assert response.status_code == 200
