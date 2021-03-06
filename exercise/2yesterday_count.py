'''
yesterday.txt 파일을 읽어서
YESTERDAY 라는 단어가 몇번 나왔는지 yesterday_lyric.upper().count('YESTERDAY')
Yesterday 라는 단어가 몇번 나왔는지  yesterday_lyric.count('Yesterday')
yesterday 라는 단어가 몇번 나왔는지  yesterday_lyric.count('yesterday')
'''
# mode - r(read), w(write), a(append), rb(read binary), wb(write binary)
# f = open('yesterday.txt', 'r')
# yesterday_lyric = f.read()
# f.close()

with open('yesterday.txt') as file:
    lyric = ''
    while 1:
        line = file.readline()
        if not line:
            break
        lyric = lyric + line.strip() + '\n'

print(lyric)
print('-----')

with open('yesterday.txt', 'r') as f:
    yesterday_lyric = f.read()
    print(yesterday_lyric)

print('Number of a word \'YESTERDAY\' ', yesterday_lyric.upper().count('YESTERDAY'))
print('Number of a word \'Yesterday\' ', yesterday_lyric.count('Yesterday'))
print('Number of a word \'yesterday\' ', yesterday_lyric.count('yesterday'))