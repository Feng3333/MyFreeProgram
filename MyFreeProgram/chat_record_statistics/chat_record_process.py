#
# Description: Program Entry
# Create: 2025-01-09
#

import os
from chat_record_tools import chat_record_statistic_process
from chat_text_summary import chat_content_process


if __name__ == '__main__':
    file_name = os.path.join(r'D:\TempFile\HistoryRecord\chatting.txt')
    front_part = os.path.dirname(file_name)
    # 1. chat_record_statistic_process
    person_info_list, person_chat_contents, all_chat_contents = chat_record_statistic_process(file_name, front_part)
    chat_content_process(person_info_list, person_chat_contents, all_chat_contents, front_part)
