# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0 # index for txt[]
    print("============= Finding Index ==============")
    while i < N:
        # print("\t".join(str(a) for a in lps[:i]))
        print("-------\t"*(N+1))
        print("Key:\t","\t".join(str(a) for a in lps), sep = "")
        print("\t"*(j+1), "(j)")
        print("Pat:\t","\t".join(list(pat)), sep = "")
        print("Str:\t","\t".join(list(txt)), sep = "")
        print("\t"*(i+1), "(i)")
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            print("Found pattern at index "+ str(i-j))
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    print("==========================================")
  
def computeLPSArray(pat, M, lps):
    print("============= Computing LPS ==============")
    len = 0 # length of the previous longest prefix suffix
  
    lps[0]=0 # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        print("\t".join(str(a) for a in lps[:i]))
        print("-------\t"*M)
        print("\t".join(list(pat)))
        print("\t"*(len), "(j)", "\t"*(i - len), "(i)", sep = "")
        if pat[i]== pat[len]:
            print("Match found")    
            len += 1
            lps[i] = len
            i += 1
        else:
            print("Match not found")
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
        print()
    print("\t".join(str(a) for a in lps))
    print("==========================================")

s = input('enter string text: ')
p = input('enter pattern to be matched: ')
KMPSearch(p, s)