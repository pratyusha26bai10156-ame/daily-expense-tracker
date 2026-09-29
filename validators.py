from expense import ALLOWED_CATEGORIES

def validate_amount(val):
    try:
        v = float(val)
        if v <= 0:
            return False
        return True
    except:
        return False

def validate_category(cat):
    return cat in ALLOWED_CATEGORIES