#
# Description: Password decoding process with many functions
# Create: 2024-08-20
#

import re
from password_processing import morse_decode_dict, phone_nine_box_decode_list, keyboard_to_letters_decode_list


# 判断str是否为摩斯密码组成
def is_morse_code(s: str) -> bool:
    # 检查字符串是否只包含点和横线
    morse_code_pattern = r'^([.-]+(\s|\/|$))*$'
    if not re.match(morse_code_pattern, s):
        print('this str is not morse code !')
        return False
    # 检查是否有多余的分隔符或不符合摩斯密码格式的字符
    # 摩斯密码的字母之间通常用空格分隔，单词之间用斜杠或更大空格分隔
    # 这里允许使用空格或斜杠作为分隔符
    parts = re.split(r'[ /]+', s.strip())
    for part in parts:
        # 检查每个部分是否为单个摩斯密码字符或由空格分隔的字符序列
        if not re.match(r'^[.-]*$', part):
            print('this str is not morse code !')
            return False
    return True


def morse_code_to_str(morse: str):
    if not is_morse_code(morse):
        return []
    morse_list = re.split(r'[ /]+', morse.strip())
    res_list = []
    for each_code in morse_list:
        if not each_code:
            continue
        res_list.append(morse_decode_dict[each_code])
    return res_list


# 手机九宫格键盘规则
def is_nine_box_rule(codes: list) -> bool:
    for code in codes:
        if len(code) != 2:
            return False
        a, b = code[0], code[1]
        if a < '1' or b < '1' or b > '4':
            return False
    return True


# 手机九宫格键盘数字转字母
def phone_nine_box_transform(codes: list):
    if not len(codes):
        return []
    if not is_nine_box_rule(codes):
        return []
    res_list = []
    for code in codes:
        a, b = int(code[0]), int(code[1])
        res_list.append(phone_nine_box_decode_list[a][b - 1])
    return res_list


# 键盘字母转顺序字母 QWE加密法
def keyboard_to_letters(str_list: list):
    res_list = []
    for item in str_list:
        res_list.append(keyboard_to_letters_decode_list[item])
    return res_list


# 珊栏密码 Rail-fence Cipher
def rail_fence_cipher_transform(codes: list, count):
    res_list = [[] for _ in range(count)]
    max_len = len(codes) / count + len(codes) % count
    idx, num = 0, 0
    for code in codes:
        if idx >= max_len - 1:
            idx = 0
            num += 1
        res_list[num].append(code)
        idx += 1

    res_str = str()
    for i in range(len(res_list[0])):
        for j in range(count):
            if i >= len(res_list[j]):
                continue
            res_str += (res_list[j][i])
    return res_str
