import os
from chat_record_tools import chat_record_statistic_process


if __name__ == '__main__':
    file_name = os.path.join(r'D:\TempFile\HistoryRecord\chatting.txt')
    chat_record_statistic_process(file_name)
