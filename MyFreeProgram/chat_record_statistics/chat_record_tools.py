import re

# PERSON_INFO_PATTERN ：人名+(首字母开头的工号)
PERSON_INFO_PATTERN = r"^[\u4e00-\u9fa5]+\([a-zA-Z0-9]+\)"


def read_chat_record_file(file_path):
    content_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            content_list.append(line)
    return content_list


def filter_person_name(content_list):
    person_info_list = {}
    person_chat_frequency = {}
    for content in content_list:
        # if '(' not in content or ')' not in content:
        #     continue
        person_info = content.split('\t')[0]
        if not re.match(PERSON_INFO_PATTERN, person_info):
            continue
        person_name = person_info.split('(')[0]
        person_number = person_info.split('(')[1][:-1]
        person_info_list[person_number] = person_name
        if person_number not in person_chat_frequency:
            person_chat_frequency[person_number] = 1
        else:
            person_chat_frequency[person_number] += 1
    return person_info_list, person_chat_frequency


def count_people_chat_number(person_info_list, person_chat_frequency):
    person_dict = {}
    for employee_id in person_info_list:
        person_dict[employee_id] = []
        person_infos = dict()
        person_infos['name'] = person_info_list[employee_id]
        person_infos['chat_frequency'] = person_chat_frequency[employee_id]
        person_dict[employee_id].append(person_infos)
    sorted_person_dict = dict(sorted(person_dict.items(), key=lambda x: x[1][0]['chat_frequency'], reverse=True))
    return sorted_person_dict


def chat_record_statistic_process(file_path):
    # 1. read files
    content_list = read_chat_record_file(file_path)
    # 2. Filtering Person Name
    person_info_list, person_chat_frequency = filter_person_name(content_list)
    # 3. Count the number of chats of all people.
    count_people_chat_number(person_info_list, person_chat_frequency)
