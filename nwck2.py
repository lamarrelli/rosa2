def nwck(a, b, c):
    bi = a.find(b)
    ci = a.find(c)
    L = [i for i in a[min(bi, ci):max(bi, ci)] if i in [')','(',',']]
    k = ''
    for i in L:
        k += i
    while '(,)' in k:
        k = k.replace('(,)','')
    if k.count('(') == len(k):
        return len(k)
    elif k.count(')') == len(k):
        return len(k)
    elif k.count(',') == len(k):
        return 2
    else:
        return k.count(')') + k.count('(') + 2

if __name__ == '__main__':
    with open('rosalind_nwck (2).txt', 'r') as f:
        tree = [line.strip().replace(';','') for line in f.readlines() if len(line.strip()) > 0]
    for i in range(0, len(tree), 2):
        a= tree[i]
        b, c = tree[i+1].split(' ')
        print(nwck(a, b, c), end=" ")
