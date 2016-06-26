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
        'select name from sqlite_master where type= \'table\';').fetchall()]
    for table in table_names:
        if not table in found_table_names:
            return False
    return True

def get_match(conn, string):
    y = yaml.load(string)
    def match(table_name):
        res = conn.execute('select * from %s' % table_name).fetchall()
        return check_equal(y[table_name], res)
    return match

def check_equal(a, b):
    return check_equal_a(a, b) and check_equal_a(b, a)

def check_equal_a(a, b):
    for i, i_val in enumerate(a):
        for j, j_val in enumerate(i_val):
            if i >= len(b):
                print '%s >= len %s (%s)' % (i, b, len(b))
                print b[0]
                print '%s does not match %s' % (a, b)
                return False
            if j >= len(b[i]):
                print '%s >= len %s (%s)' % (a, b[i], len(b[i]))
                print '%s does not match %s' % (a, b)
                return False
            if j_val != b[i][j]:
                print '%s does not equal %s' % (j_val, b[i][j])
                print '%s does not equal %s' % (i_val, b[i])
                return False
    return True

def get_table_names():
    return [
        'files',
        'tags',
        'fileTags',
        'viewFolders',
        'viewSubfolders',
        'viewFolderContents']
