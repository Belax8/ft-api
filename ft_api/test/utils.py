import uuid


def generate_email_address():
    return '{0}@{1}.com'.format(str(uuid.uuid4())[:10], str(uuid.uuid4())[:5])


def generate_id(size=30):
    return str(uuid.uuid4()).replace('-', '')[:size]


def generate_string(size=30):
    return str(uuid.uuid4()).replace('-', '')[:size]
