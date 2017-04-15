import json
import os


if __name__=='__main__':

    count = 1
    files = os.listdir('./commits_files')
    files.sort()

    # with open('./details/commit_details_{0}.json'.format(str(count)), 'w') as dest_file:
    #     with open('./commits_files/{0}'.format('commits_details_32000_33000.json')) as data:
    #         commits = json.load(data)
    #         for commit in commits:
    #             for _file in commit['files']:
    #                 _file.pop('patch', None)
    #                 _file.pop('raw_url', None)
    #                 _file.pop('blob_url', None)
    #         dest_file.write(json.dumps(commits))

    for filename in files:
        if filename.split('.')[1]=='json':
            with open('./details/commit_details_{0}.json'.format(str(count)), 'w') as dest_file:
                with open('./commits_files/{0}'.format(filename)) as data:
                    commits = json.load(data)
                    for commit in commits:
                        for _file in commit['files']:
                            _file.pop('patch', None)
                            _file.pop('raw_url', None)
                            _file.pop('blob_url', None)
                    dest_file.write(json.dumps(commits))
                    count += 1
