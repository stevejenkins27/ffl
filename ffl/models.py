from ffl import db

playerPosition = db.Table('nfl_player_position',
        db.Column('player_id', db.Integer, db.ForeignKey('nfl_player.id')),
        db.Column('posiiton_id', db.Integer, db.ForeignKey('position.id')))

class NflPlayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    espn_id = db.Column(db.Integer)
    name = db.Column(db.String(64))
    team_id = db.Column(db.Integer, db.ForeignKey('nfl_team.id'))
    projected_points = db.Column(db.Float)
    team = db.relationship('NflTeam', backref='players')
    positions =  db.relationship('Position', secondary=playerPosition,
            backref='players')

    def __init__(self, id, name, team, positions, points):
        self.espn_id = id
        self.name = name
        self.team = team
        self.positions = positions
        self.projected_points = points

class NflGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_team_id = db.Column(db.Integer, db.ForeignKey('nfl_team.id'))
    away_team_id = db.Column(db.Integer, db.ForeignKey('nfl_team.id'))
    season_week = db.Column(db.Integer)
    home_team = db.relationship('NflTeam', backref='home_games',
            foreign_keys=[home_team_id])
    away_team = db.relationship('NflTeam', backref='away_games',
            foreign_keys=[away_team_id])

    def __init__(self, homeTeam, awayTeam, seasonWeek):
        self.home_team = homeTeam
        self.away_team = awayTeam
        self.season_week = seasonWeek

class NflTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    espn_code = db.Column(db.String(32))
    espn_id = db.Column(db.Integer)
    bye_week = db.Column(db.Integer)
    projected_defense_points = db.Column(db.Float)

    def __init__(self, id, code, name):
        self.espn_id = id
        self.espn_code = code
        self.name = name

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    espn_code = db.Column(db.String(8))
    name = db.Column(db.String(32))
    order = db.Column(db.Integer)

class UserEmail(db.Model):
    email = db.Column(db.String(128), primary_key=True)
