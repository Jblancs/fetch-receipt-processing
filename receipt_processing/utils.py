def generate_id(existing_receipts):
    '''
    Generate id for new receipts
    '''
    if not existing_receipts:
        return 1
    else:
        return max(existing_receipts.keys()) + 1
