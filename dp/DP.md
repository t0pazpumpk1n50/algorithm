#### Determine if a string s is a subsquence of another string t


    Let F(i, j) denote whether s[:i+1] is a subsequence of t[:j+1]
    F(i, j) = F(i, j - 1) or 
              F(i - 1, j - 1) and s[i] == t[j]
