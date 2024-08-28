#
# Description: Password encoding process with many functions
# Create: 2024-08-26
#

from .password_encode_dict import morse_encode_dict


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


def generate_final_processed_code(codes: list):
    res_str = str()
    for code in codes:
        res_str += code
        res_str += " "
    return res_str
