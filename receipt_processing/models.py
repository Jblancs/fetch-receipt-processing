from datetime import datetime

class Receipt:
    def __init__(self, store_name, total_amount, items, purchase_date, purchase_time):
        self.id = None
        self.store_name = store_name
        self.total_amount = total_amount
        self.items = items
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.points = 0

    def to_dict(self):
        return {
            'id': self.id,
            'store_name': self.store_name,
            'total_amount': self.total_amount,
            'items': self.items,
            'purchase_date': self.purchase_date,
            'purchase_time': self.purchase_time,
            'points': self.points,
        }
