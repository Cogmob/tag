insert into files (name) values ('file name')
insert into views (name) values ('view name')
insert into tags (name) values ('tag name')
insert into fileTags (fileId, tagId) values (1, 1)
insert into viewFolders (viewId, name) values (1, 'view folder name')
insert into viewSubfolders (parentId, childId, childOrder) values (1, 1, 1)
insert into viewFolderContents(folderId, fileId, fileOrder) values (1, 1, 1)