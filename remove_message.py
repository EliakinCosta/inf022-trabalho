import json


def has_more_than(sector):
    count = len([molecule for window in sector['windows'] for molecule in window['molecules']])
    if count > 10:
        return True
    return False


if __name__=='__main__':
    with open('dest_file_2.json', 'w') as dest_file:
        with open('./data.json', 'r') as source_file:
            data = json.load(source_file)
            new_list = [data['sectors'][index] for index in range(len(data['sectors'])) if has_more_than(data['sectors'][index])]
            data['sectors'] = new_list
            dest_file.write(json.dumps(data))
    # with open('./contributors.json', 'r+') as contributors_file:
    #     with open('./dest_file_2.json', 'r') as source_file:
    #         big_data = json.load(contributors_file)
    #         small_data = json.load(source_file)
    #         new_list = [contributor for contributor in big_data['contributors'] if contributor['name'] in [small_data['sectors'][index]['label'] for index in range(len(small_data['sectors']))]]
    #         big_data['contributors'] = new_list
    #         contributors_file.write(json.dumps(big_data))
