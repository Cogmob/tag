import yaml

def does_database_match_yaml(conn, string):
    match = get_match(conn, string)
    table_names = get_table_names()
    if not tables_exist(table_names, conn):
        return False

    for table_name in table_names:
        if not match(table_name):
            return False
    return True

def tables_exist(table_names, conn):
    found_table_names = [i[0] for i in conn.execute(
        'SELECT name FROM sqlite_master WHERE type= \'table\';').fetchall()]
    for table in table_names:
        if not table in found_table_names:
            return False
    return True

def get_match(conn, string):
    y = yaml.load(string)
    def match(table_name):
        res = conn.execute('select * from %s' % table_name).fetchall()
        print y
        print res
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
