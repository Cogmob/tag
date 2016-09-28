from .implement_view_file import implement_view_file

def get_add_view_file_func(view_file):
    def f(directory):
        return implement_view_file(view_file, directory)
    return f
