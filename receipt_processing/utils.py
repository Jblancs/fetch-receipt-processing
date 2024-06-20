from datetime import datetime

def generate_id(existing_receipts):
    '''
    Generate id for new receipts
    '''
    if not existing_receipts:
        return 1
    else:
        return max(existing_receipts.keys()) + 1

def combine_date_time(date, time):
    purchase_datetime_str = f"{date} {time}"
    purchase_datetime = datetime.strptime(purchase_datetime_str, '%Y-%m-%d %H:%M')

    return purchase_datetime
