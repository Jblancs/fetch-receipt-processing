class Receipt:
    def __init__(self, retailer, total, items, purchase_datetime):
        self.id = None
        self.retailer = retailer
        self.purchase_datetime = purchase_datetime
        self.items = items
        self.total = total
        self.points = 0

    def to_dict(self):
        return {
            'id': self.id,
            'retailer': self.retailer,
            'total': self.total,
            'items': self.items,
            'purchase_datetime': self.purchase_datetime,
            'points': self.points,
        }
