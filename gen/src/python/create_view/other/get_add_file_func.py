def get_add_file_func(file_tags):
    def f(directory):
        if 'stored_files' not in directory:
            directory['stored_files'] = []
        directory['stored_files'].append(file_tags)
        epr(file_tags)
        return directory
    return f
