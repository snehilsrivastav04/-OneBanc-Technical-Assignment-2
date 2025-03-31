def levenshtein_distance(s1, s2):
    
    m = len(s1)
    n = len(s2)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,     # Deletion
                               matrix[i][j - 1] + 1,     # Insertion
                               matrix[i - 1][j - 1] + cost) # Substitution

    return matrix[m][n], matrix

def print_matrix(matrix, s1, s2):
  
    print("  ", end="  ")
    for char in s2:
        print(char, end=" ")
    print()
    print("-" * (4 + len(s2) * 2))
    for i in range(len(matrix)):
        if i == 0:
            print(" ", end="| ")
        else:
            print(s1[i - 1], end="| ")
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()

if __name__ == "__main__":
    string_pairs = [
        ("Levenshtein", "Lavenstaein"),
        ("TryHackMe", "TriHackingMe"),
        ("Optimization", "Progressive"),
        ("This is easy", "This is easy"),
    ]

    for s1, s2 in string_pairs:
        distance, matrix = levenshtein_distance(s1, s2)
        print(f"Distance between '{s1}' and '{s2}': {distance}")
        print("Edit Distance Matrix:")
        print_matrix(matrix, s1, s2)
        print("\n" + "" * 40 + "\n")