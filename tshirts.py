class tshirts:
    def size(self, cms):
        if (cms in range(0, 20)) or (cms in range(55, 100)):
            return 'Not applicable'
        elif cms in range(20, 34):
            return 'XS'
        elif cms in range(34, 38):
            return 'S'
        elif cms in range(38, 42):
            return 'M'
        elif cms in range(42, 50):
            return 'L'
        elif cms in range(50, 55):
            return 'XL'
