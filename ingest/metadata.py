import time

def create_metadata(source_type, file_name, page=None, slide=None):
    return {
        "source_type": source_type,
        "file_name": file_name,
        "page": page,
        "slide": slide,
        "timestamp": time.time()
    }
