from os.path import join, splitext

def media_saver(instance, filename):
    ext = splitext(filename)[1]
    if ext == '.avi' or ext == '.mp4':
        return '/'.join(['divers', 'video', filename])
    elif ext == '.jpg' or ext == '.png' or ext == '.gif':
        return '/'.join(['divers', 'image', filename])
    elif ext == '.mp3' or ext == '.wav':
        return '/'.join(['divers', 'sound', filename])
    elif ext == '.svg':
        return '/'.join(['divers', 'svg', filename])
    elif ext == '.pdf':
        return '/'.join(['divers', 'pdf', filename])
    else:
        return '/forbid/'.join([filename])

def content_file_name(instance, filename):
    return '/'.join([instance.name, filename])