from simplads import Bundle, pipe, lift, add_data

def create_view(view_files, example_files):
    return pipe(
        1,
        add_data(1),
        create_root)

def create_root(view_files):
    return view_files
