#
# Description: Some treatment of the content of the chatting
# Create: 2025-01-09
#

import os
import json


def output_ori_contents(person_info_list, each_person_chat_contents, all_chat_contents, output_path):
    each_person_chat_content_dict = {}
    for key, value in each_person_chat_contents.items():
        each_info = f'{key}_{person_info_list[key]}'
        each_person_chat_content_dict[each_info] = value
    each_person_chat_content_file = os.path.join(output_path, 'each_person_chat_contents.json')
    with open(each_person_chat_content_file, 'w', encoding="utf-8") as json_file:
        json.dump(each_person_chat_content_dict, json_file, ensure_ascii=False, indent=4)

    all_chat_contents_file = os.path.join(output_path, 'all_chat_contents.json')
    with open(all_chat_contents_file, 'w', encoding="utf-8") as json_file:
        json.dump(all_chat_contents, json_file, ensure_ascii=False, indent=4)
    return


def chat_content_process(person_info_list, each_person_chat_contents, all_chat_contents, output_path):
    # 1. output original contents
    output_ori_contents(person_info_list, each_person_chat_contents, all_chat_contents, output_path)
