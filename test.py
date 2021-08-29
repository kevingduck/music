import random

# Convert chess games to music
"""
Beats and sleep time fractions
Beat Fraction 	Sleep Time
Whole -	1
Half -	0.5
Quarter -	0.25
Eighth -	0.125
Sixteenth -	0.0625
Thirty-second -	0.03125
Sixty-fourth -	0.015625
"""

"""
Demo PGN game

1.e4 e5 2.Bc4 f5 3.exf5 Nf6 4.Nc3 d5 5.Nxd5 Bc5 6.Nxf6+ Qxf6 7.d3 Bxf5 8.Nf3 Bg4
9.Bd5 c6 10.Be4 Nd7 11.O-O h6 12.c3 O-O-O 13.b4 Bb6 14.a4 a6 15.Qb3 Bxf3
16.Bxf3 g5 17.Be3 g4 18.Bxg4 Bc7 19.Bf3 Rhg8 20.Be4 Rg4 21.f3 Rg7 22.b5 axb5
23.axb5 Nb6 24.bxc6 Rdg8 25.Rf2 Qd8 26.Ra8+ Bb8 27.Bxb6 Rxg2+ 28.Rxg2 Rxg2+
29.Kxg2 Qg5+ 30.Kh1 Qc1+ 31.Bg1  1-0
"""

"""
Pieces and corresponding notes

King (K) - h h
Queen (Q) -  s s s s s s s s s s s s s s s s 
Rook (R) - e e e e e e e e 
Bishop (B) - t t t t t t  
Knight (N) - q e e q e e 
Pawn - q q q q 


"""
note_times = {
    'w': 1,
    'h': 0.5,
    'tr': 0.33,
    'q': 0.25,
    'e': 0.125,
    's': 0.0625,
    't': 0.03125,
    'sf': 0.015625
}

piece_time = {
  'k': str(note_times['h']) + ' ' + str(note_times['h']),
  'q': str(note_times['s']) + ' ' + str(note_times['s']) + ' ' +  str(note_times['s']) + ' ' + str(note_times['s']) +' ' +  str(note_times['q']) +' ' +  str(note_times['q']) +' ' +  str(note_times['q']),
  'r': str(note_times['e']) + ' ' + str(note_times['e']) + ' ' +  str(note_times['e']) + ' ' + str(note_times['e']) +' ' +  str(note_times['e']) +' ' +  str(note_times['e']) +' ' +  str(note_times['e']) +' ' +  str(note_times['e']),
  'b': str(note_times['tr']) + ' ' +  str(note_times['tr'])   + ' ' +  str(note_times['tr'])   + ' ' +  str(note_times['tr'])   + ' ' +  str(note_times['tr'])   + ' ' +  str(note_times['tr']),
  'n': str(note_times['q']) + ' ' +  str(note_times['e'])   + ' ' +  str(note_times['e'])   + ' ' +  str(note_times['q'])   + ' ' +  str(note_times['e'])   + ' ' +  str(note_times['e']),
  'p': str(note_times['q']) + ' ' +  str(note_times['q'])   + ' ' +  str(note_times['q'])   + ' ' +  str(note_times['q']),
  '(Castle)': str(note_times['w']),
} 


game = """
1.e4 e5 2.Bc4 f5 3.exf5 Nf6 4.Nc3 d5 5.Nxd5 Bc5 6.Nxf6+ Qxf6 7.d3 Bxf5 8.Nf3 Bg4 9.Bd5 c6 10.Be4 Nd7 11.O-O h6 12.c3 O-O-O 13.b4 Bb6 14.a4 a6 15.Qb3 Bxf3 16.Bxf3 g5 17.Be3 g4 18.Bxg4 Bc7 19.Bf3 Rhg8 20.Be4 Rg4 21.f3 Rg7 22.b5 axb5 23.axb5 Nb6 24.bxc6 Rdg8 25.Rf2 Qd8 26.Ra8+ Bb8 27.Bxb6 Rxg2+ 28.Rxg2 Rxg2+  29.Kxg2 Qg5+ 30.Kh1 Qc1+ 31.Bg1  1-0
"""

# Compose song from pieces moving
song = []

def add_note(note):
    song.append(note)


# Turn list
def get_turns_from_game(game):    
    i = 1
    for turn in game.split('.')[1:]:
        # print(f'{i}) {turn[:-2]}')

        notes = get_notes_from_turn(turn)
        print(f'{notes} \n')
        
        i += 1
        
        # # take opponent's piece
        # if 'x' in turn.split(' ')[0]:
        #     print('White attacks! \n')
        #     if (is_in_check(turn).split(' ')[0]):
        #         print('Black is in check! \n')
        
        # if 'x' in turn.split(' ')[1]:
        #     print('Black attacks! \n')
        #     if is_in_check(turn).split(' ')[1]:
        #         print('White is in check! \n')
            
        # # win via checkmate or resignation
        # if '1' in turn.split(' ')[1]:
        #     print('White has won! \n')
        # if '1' in turn.split(' ')[0]:
        #     print('Black won! \n')

# determine if player is in check
def is_in_check(turn):
    if '+' in turn.split(' ')[1]:
        print('White is in check! \n')
    if '+' in turn.split(' ')[0]:
        print('Black is in check! \n')

# convert each turn into musical notes from corresponding piece
def get_notes_from_turn(turn):
    notes = []
    try:
        for piece in turn.split(' ')[:2]:
            if piece[0] not in ['K', 'Q', 'R', 'B', 'N', 'O']:
                notes.append('p')
            elif piece[0] == 'K':
                notes.append('k')
            elif piece[0] == 'Q':
                notes.append('q')
            elif piece[0] == 'R':
                notes.append('r')
            elif piece[0] == 'B':
                notes.append('b')
            elif piece[0] == 'N':
                notes.append('n')
            elif piece[0] == 'O':
                notes.append('(Castle)')
            else:
                print('Error!' )
        add_note(notes[0] + ' ' + notes[1])
    
    except:
        print(f'Final move: {turn}')

    return notes

# Convert notes to song
def convert_to_music(song):
    music = []
    for piece in song:
        print(piece)
        for p in piece.split(' '):
            music.append(piece_time[p])
    
    for note in music:
        print(note)
    return music

# generate random letter from a to g
def random_letter():
    return random.choice(('a','b','c','d','e','f','g'))

def main():
    get_turns_from_game(game)
    convert_to_music(song)
    

if __name__ == '__main__':
    main()


