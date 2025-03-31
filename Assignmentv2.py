def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
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
                               matrix[i - 1][j - 1] + cost)  # Substitution

    return matrix[m][n]


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")


distance = levenshtein_distance(str1, str2)
print(f"\nLevenshtein Distance between '{str1}' and '{str2}': {distance}")
