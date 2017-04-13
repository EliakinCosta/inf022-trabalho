import json


def has_more_than(sector):
    count = len([molecule for window in sector['windows'] for molecule in window['molecules']])
    if count > 25:
        return True
    return False

if __name__=='__main__':
    with open('dest_file_2.json', 'w') as dest_file:
        with open('./data.json', 'r') as source_file:
            data = json.load(source_file)
            new_list = [data['sectors'][index] for index in range(len(data['sectors'])) if has_more_than(data['sectors'][index])]
            data['sectors'] = new_list
            dest_file.write(json.dumps(data))
