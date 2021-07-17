import re

def solution(new_id):
    temp_list = []
    avail_list = 'abcdefghijklmnopqrstuvwxyz-_.1234567890'

    new_id = new_id.lower()

    for i in range(len(new_id)):
        if new_id[i] in avail_list:
            temp_list.append(new_id[i])

    new_id = ''.join(temp_list)
    new_id = re.sub('\.\.+', '.', new_id)
    new_id = new_id.strip('.')

    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    answer = new_id
    return answer