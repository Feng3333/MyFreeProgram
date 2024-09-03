#
# Description: Password encoding process with many functions
# Create: 2024-08-26
#

from .password_encode_dict import morse_encode_dict, keyboard_to_letters_encode_list, phone_nine_box_encode_dict


def generate_final_processed_code(codes: list):
    """
    生成最终的密码结果(字符串形式)
    :param codes: str
    :return: str
    """
    res_str = str()
    for code in codes:
        res_str += code
        res_str += " "
    return res_str


def encode_to_morse_code(letters: str):
    """
    将字符串装换为摩斯密码
    :param letters: str
    :return: morse_code_list: list
    """
    morse_code_list = []
    for s in letters:
        morse_code_list.append(morse_encode_dict[s])
    return morse_code_list


def keyboard_to_letters_encode(str_list: list) -> list:
    """
    # 字母转键盘字母QWE加密法 ABC=QWE
    :param str_list: list
    :return: list
    """
    res_list = []
    for item in str_list:
        res_list.append(keyboard_to_letters_encode_list[item])
    return res_list


def phone_nine_box_encode(str_list: list) -> list:
    """
    # 字母转手机九宫格
    :param str_list: list
    :return:
    """
    res_list = []
    for item in str_list:
        if not item.isalpha():
            print('This str list is not all letter')
            return []
        else :
            res_list.append(phone_nine_box_encode_dict[item])
    return res_list
