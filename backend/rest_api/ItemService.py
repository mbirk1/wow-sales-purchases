from models import Item

class ItemService:

    def getAllItems(self)-> int:
        # SQL Alchemy

        return 0

def validate(item: Item) -> bool:
    if item.value is None:
        return False
    elif item.name is None:
        return False
    else:
        return True
