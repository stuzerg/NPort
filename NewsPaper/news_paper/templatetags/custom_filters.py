from django import template

register = template.Library()


@register.filter()
def censored(checking, swear='омикрон'):
    asteriks_len = len(swear)
    swear = swear.lower()
    result = checking
    # на всякий случай убираем чувствительность к регистру,
    # поэтому много строк(((

    curr = 0
    if isinstance(checking, str):
        ch_low = checking.lower()

        while True:
            curr = ch_low.find(swear, curr)
            checking = checking.replace(checking[curr:curr+asteriks_len], checking[curr]+'*'*(asteriks_len-1))

            if curr == -1:

                break
            curr += asteriks_len
            result = checking
            # print(checking, curr)
    else: print('формат данных отвергает цензуру!')

    return result
