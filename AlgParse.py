import re

ALG_PATTERN = r"((\s*([xyzUuLlFfRrBbDdMES]['2]?\s+)+([xyzUuLlFfRrBbDdMES]['2]?\s*)*)|([xyzUuLlFfRrBbDdMES]['2]?))"
COMM_PATTERN = r"\[\s*" + ALG_PATTERN + r",\s*" + ALG_PATTERN + r"\]"
CONJ_PATTERN = r"\[\s*" + ALG_PATTERN + r":\s*" + ALG_PATTERN + r"\]"

def simplify(compound_alg) -> str:
    """Expands an algorithm recursively until it is a simple sequence"""
    output = compound_alg
    if is_simple_sequence(compound_alg):
        return compound_alg.strip()
    
    # Expand innermost commutators
    com_found = re.search(COMM_PATTERN,output)
    if com_found is not None:
        comm = com_found.group()
        output = output.replace(comm,expand_commutator(comm))
    # Expand innermost conjugates
    conj_found = re.search(CONJ_PATTERN,output)
    if conj_found is not None:
        conj = conj_found.group()
        output = output.replace(conj,expand_conjugate(conj))
    
    return simplify(output)


def is_simple_sequence(alg):
    """Returns true if alg is a simple sequence (e.g. "R U R' U')"""
    return re.fullmatch(ALG_PATTERN,alg) is not None

def invert_sequence(alg) -> str:
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

def expand_commutator(commutator) -> str:
    """Takes a string in commutator notation and expands it to a simple sequence
        ex. "[D, R U R']" -> "D R U R' D' R U' R"
    """
    A,B = commutator.replace("[","").replace("]","").split(',')
    expanded = f"{A.strip()} {B.strip()} {invert_sequence(A.strip())} {invert_sequence(B.strip())}"
    return expanded

def expand_conjugate(conjugate) -> str:
    """Takes a string in conjugate notation and expands it to a simple sequence
        ex. "[R' U': R' F R F']" -> "R' U' R' F R F' U R"
    """
    A,B = conjugate.replace("[","").replace("]","").split(':')
    expanded = f"{A.strip()} {B.strip()} {invert_sequence(A.strip())}"
    return expanded