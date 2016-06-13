def initialise_database(c):
    files(c)
    tags(c)
    views(c)
    file_tags(c)
    view_folders(c)
    view_subfolders(c)
    view_folder_contents(c)

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

def view_folders(c):
    c.execute('''
        create table viewFolders(
            id integer primary key,
            viewId integer,
            name text,
            foreign key (viewId) references view(id))''')

def view_subfolders(c):
    c.execute('''
        create table viewSubfolders(
            parentId integer references viewFolders(id),
            childId integer references viewFolders(id),
            childOrder integer)''')

def view_folder_contents(c):
    c.execute('''
        create table viewFolderContents(
            folderId integer references viewFolders(id),
            fileId integer references files(id),
            fileOrder integer)''')
