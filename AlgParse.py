def invert_sequence(alg):
    """Returns the inverse of a basic move sequence (Not for commutators)
    
    Args:
        alg: String representing a sequence of moves
        
    Returns:
        Inverted algorithm as string
    """

    moves = alg.split()
    inverted_moves = []

    for move in reversed(moves):
        if move.endswith("'"):
            inverted_moves.append(move[:-1]) # Remove prime
        elif move.endswith("2"):
            inverted_moves.append(move) # Half-turns remain unchanged
        else:
            inverted_moves.append(move + "'") # Invert normal turns by adding a prime

    return " ".join(inverted_moves)