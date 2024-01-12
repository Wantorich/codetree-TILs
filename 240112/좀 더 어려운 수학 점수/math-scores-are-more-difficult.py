mathA, engA = map(int, input().split())
mathB, engB = map(int, input().split())

if mathA > mathB :
    print('A')
elif mathA < mathB :
    print('B')
else :
    print('%c' % 'A' if engA >= engB else 'B')