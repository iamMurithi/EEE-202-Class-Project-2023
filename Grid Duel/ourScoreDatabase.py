import sqlite3

scoreDB = sqlite3.connect('ScoreDatabase.db')
score_cursor = scoreDB.cursor()

def initialize_score_database():    #call this only to ensure our database is properly set up
    score_cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY,
            wins INTEGER DEFAULT 0,
            draws INTEGER DEFAULT 0,
        )
    ''')
    scoreDB.commit()

def get_scores():   #this wil display scores in grid duel options, 'scores'
    score_cursor.execute('SELECT * FROM scores LIMIT 1')
    row = score_cursor.fetchone()
    if row is not None:
        return {'wins': row[1], 'draws': row[2]}
    else:
        return {'wins': 0, 'draws': 0}

def update_scores(result):  #this will update our database with the wins/draws every time grid duel is ran.
    if result in ["win", "draw"]:
        score_cursor.execute('''
            UPDATE scores SET {} = {} + 1 WHERE id = 1
        '''.format(result , result))
        scoreDB.commit()

def close_score_database_connection():
    scoreDB.close()
