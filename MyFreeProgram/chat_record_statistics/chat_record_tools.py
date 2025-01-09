#
# Description: chat record statistic process
# Create: 2024-12-28
#
import re

from collections import defaultdict
from data_to_excel_table import chat_record_data_to_excel_process

# PERSON_INFO_PATTERN ：人名+(首字母开头的工号)
PERSON_INFO_PATTERN = r"^[\u4e00-\u9fa5]+\([a-zA-Z0-9]+\)"


def read_chat_record_file(file_path):
    content_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            content_list.append(line)
    return content_list


def filter_person_name(content_list):
    # person_info_list: Record basic information about each person
    person_info_list = {}
    # person_chat_frequency: Record chat times about each person
    person_chat_frequency = {}
    # each_person_chat_contents: Record chatting information about each person
    each_person_chat_contents = defaultdict(list)
    # all_chat_contents: Record chatting information about all
    all_chat_contents = []

    # cur_person: Record who might have said this content
    cur_person = None
    for content in content_list:
        # Determine whether the content is personal information
        person_info = content.split('\t')[0]
        if re.match(PERSON_INFO_PATTERN, person_info):
            person_name = person_info.split('(')[0]
            person_number = person_info.split('(')[1][:-1]
            person_info_list[person_number] = person_name
            cur_person = person_number
        elif cur_person is not None:
            each_person_chat_contents[cur_person].append(content)
            all_chat_contents.append(content)
        else:
            all_chat_contents.append(content)
        if person_number not in person_chat_frequency:
            person_chat_frequency[cur_person] = 1
        else:
            person_chat_frequency[cur_person] += 1
    return person_info_list, person_chat_frequency, each_person_chat_contents, all_chat_contents


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


def chat_record_statistic_process(file_path, output_path):
    # 1. read files
    content_list = read_chat_record_file(file_path)
    # 2. Filtering Person Name
    person_info_list, person_chat_frequency, person_chat_contents, all_chat_contents = filter_person_name(content_list)
    # 3. Count the number of chats of all people.
    processed_person_dict = count_people_chat_number(person_info_list, person_chat_frequency)
    # 4. Record the person_chat_info results in an Excel file.
    chat_record_data_to_excel_process(processed_person_dict, output_path)
    return person_info_list, person_chat_contents, all_chat_contents
