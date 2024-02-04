#helper function for file operations

mime_types = {
    'csv' : 'text/csv',
    'json' : 'applications/json',
    'xlsx' : 'application/vnd.'
}

def get_mime_types(file_path):
    ext = file_path.split('.')[-1]
    return mime_types.get(ext, 'text/plain')