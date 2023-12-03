import sqlite3

scoreDB = sqlite3.connect('ScoreDatabase.db')
score_cursor = scoreDB.cursor()

def initialize_score_database():    #call this only to ensure our database is properly set up
    score_cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY,
            wins INTEGER DEFAULT 0,
            draws INTEGER DEFAULT 0
        )
        """)
    scoreDB.commit()

def get_scores():   
    score_cursor.execute('SELECT wins, draws FROM scores LIMIT 1')
    row = score_cursor.fetchone()
    if row is not None:
        return 'Wins : ' + str(row[0]) + ', Draws : ' + str(row[1])
    else:
        return 'Wins : 0 , Draws : 0'

def update_scores(result):
    # Check if the row with id = 1 already exists
    score_cursor.execute('SELECT 1 FROM scores WHERE id = 1')
    existing_row = score_cursor.fetchone()

    if existing_row:
        # Row with id = 1 exists, update the wins or draws count
        if result == 'wins':
            score_cursor.execute('UPDATE scores SET wins = wins + 1 WHERE id = 1')
        elif result == 'draws':
            score_cursor.execute('UPDATE scores SET draws = draws + 1 WHERE id = 1')
    else:
        # Row with id = 1 does not exist, insert a new row
        if result == 'wins':
            score_cursor.execute('INSERT INTO scores (id, wins) VALUES (1, 1)')
        elif result == 'draws':
            score_cursor.execute('INSERT INTO scores (id, draws) VALUES (1, 1)')

    scoreDB.commit()
      
def reset_scores():
    score_cursor.execute('UPDATE scores SET wins = 0, draws = 0 WHERE id = 1')
    scoreDB.commit()

def close_score_database_connection():
    scoreDB.close()

if __name__ == '__main__':
    #incase this script is run as the main, it resets the scores
    initialize_score_database()
    reset_scores()