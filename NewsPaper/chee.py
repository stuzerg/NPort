

def censored(checking, swear='редиска'):
    asteriks_len = len(swear)
    swear = swear.lower()

    curr = 0
    if isinstance(checking, str):
        ch_low = checking.lower()

        while True:
            curr = ch_low.find(swear, curr)
            checking = checking.replace(checking[curr:curr+asteriks_len], swear[0]+'*'*(asteriks_len-1))

            if curr == -1: break
            curr += asteriks_len
            print(checking, curr)
    else: print('формат данных отвергает цензуру!')

inp = 'fhrtyert yyKJLKJDFLKGJ LKредискаGHFFрЕдИсКА АПРfhrtyert yyKJLKJDFLKGJ LKредискаGHFFрЕдИсКАfhrtyert yyKJLKJDFLKGJ LKредискаGHFFрЕдИсКА'

censored(inp)
