class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")

    def pop(self, index=None):
        if index is None:
            popped_item = super().pop()
            print(f"Popped [{popped_item}] from the list.")
        else:
            popped_item = super().pop(index)
            print(f"Popped [{popped_item}] from the list.")
