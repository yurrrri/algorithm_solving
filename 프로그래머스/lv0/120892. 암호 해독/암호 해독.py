def solution(cipher, code):
    # return ''.join(list(e for i, e in enumerate(cipher) if (i+1)%code == 0))
    return cipher[code-1::code]