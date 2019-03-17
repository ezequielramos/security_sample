# This file simulates a data from database
safe_data = [
    {'id': '1', 'text': 'Safe data 1', 'owner': ['ezequiel ramos']},
    {'id': '2', 'text': 'Safe data 2', 'owner': ['pedro burguesan']},
    {'id': '3', 'text': 'Safe data 3', 'owner': ['ezequiel ramos', 'pedro burguesan']}
]

def get_data(info):
    for data in safe_data:
        if data['id'] == info:
            return data

    return None
