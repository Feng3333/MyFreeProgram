#
# Description:
# Create: 2024-08-20
#

from password_processing.password_decode import morse_code_to_str, phone_nine_box_transform, keyboard_to_letters,\
        rail_fence_cipher_transform
from password_processing.password_encode import generate_final_processed_code, encode_to_morse_code


def password_encoding_process(strings: str):
    code_list = encode_to_morse_code(strings)
    return generate_final_processed_code(code_list)


if __name__ == '__main__':
    # morse_code = '....-/.----/----./....-/....-/.----/---../.----/....-/.----/-..../...--/' \
    #              '....-/.----/----./..---/-..../..---/..---/...--/--.../....-/'
    # # 解析摩斯密码
    # parsed_morse_codes = morse_code_to_str(morse_code)
    # # 解析后的摩斯密码重新组合
    # phone_nine_box_codes = []
    # for idx, item in enumerate(parsed_morse_codes):
    #     if idx % 2:
    #         continue
    #     code = item + parsed_morse_codes[idx + 1]
    #     phone_nine_box_codes.append(code)
    # # 手机九宫格数字转字母
    # str_codes = phone_nine_box_transform(phone_nine_box_codes)
    # letters = keyboard_to_letters(str_codes)
    # rail_fence_lists = rail_fence_cipher_transform(letters, 2)
    # print(rail_fence_lists[::-1])
    # print('finish')

    origin_str = 'ILOVEYOU'
    res_str = password_encoding_process(origin_str)
    print(res_str)
