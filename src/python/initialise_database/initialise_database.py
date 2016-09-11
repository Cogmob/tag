def initialise_database(c):
    files(c)
    tags(c)
    file_tags(c)

def files(c):
    c.execute('''
        create table files(
            id integer primary key,
            name text)''')

def views(c):
    c.execute('''
        create table views(
            id integer primary key,
            name text)''')

def tags(c):
    c.execute('''
        create table tags(
            id integer primary key,
            name text)''')

def file_tags(c):
    c.execute('''
        create table fileTags(
            fileId integer,
            tagId integer,
            foreign key (fileId) references files(id),
            foreign key (tagId) references tags(id))''')
