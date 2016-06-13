import yaml

def does_database_match_yaml(conn, string):
    match = get_match(conn, string)
    table_names = get_table_names()
    for table_name in table_names:
        if not match(table_name):
            return False
    return True

def get_match(conn, string):
    y = yaml.load(string)
    def match(table_name):
        res_lines = conn.execute('select * from %s' % table_name)
        res = []
        for line in res_lines:
            res.push(line)
        print 'y ='
        print y
        print 'res ='
        print res
        print 'equal?'
        print y == res
        return y == res
    return match

def get_table_names():
    return [
        'files',
        'tags',
        'fileTags',
        'viewFolders',
        'viewSubfolders',
        'viewFolderContents']
