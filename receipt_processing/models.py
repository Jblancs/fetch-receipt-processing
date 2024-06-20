class Receipt:
    def __init__(self, store_name, total_amount, items, purchase_datetime):
        self.id = None
        self.store_name = store_name
        self.total_amount = total_amount
        self.items = items
        self.purchase_datetime = purchase_datetime
        self.points = 0

    def to_dict(self):
        return {
            'id': self.id,
            'store_name': self.store_name,
            'total_amount': self.total_amount,
            'items': self.items,
            'purchase_datetime': self.purchase_datetime,
            'points': self.points,
        }
