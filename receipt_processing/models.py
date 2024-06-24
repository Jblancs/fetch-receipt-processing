class Receipt:
    def __init__(self, retailer, total, items, purchase_date, purchase_time):
        self.id = None
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = items
        self.total = total
        self.points = 0

    def to_dict(self):
        return {
            'id': self.id,
            'retailer': self.retailer,
            'total': self.total,
            'items': self.items,
            'purchase_date': self.purchase_date,
            'purchase_time': self.purchase_time,
            'points': self.points,
        }
