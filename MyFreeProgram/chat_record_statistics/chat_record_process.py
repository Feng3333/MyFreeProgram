#
# Description: Program Entry
# Create: 2025-01-09
#

import os
from chat_record_tools import chat_record_statistic_process
from chat_text_summary import chat_content_process


if __name__ == '__main__':
    print('chat_record_process start: ')
    # 1. file path process
    file_name = os.path.join(r'D:\TempFile\HistoryRecord\chatting.txt')
    front_part = os.path.dirname(file_name)
    output_path = os.path.join(front_part, 'chat_record')
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)
    # 2. chat_record_statistic_process
    person_info_list, person_chat_contents, all_chat_contents = chat_record_statistic_process(file_name, output_path)
    # 3.
    chat_content_process(person_info_list, person_chat_contents, all_chat_contents, output_path)
    print('end......')

