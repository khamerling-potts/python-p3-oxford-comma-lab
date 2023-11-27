def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return " and ".join(items)
    items[-1] = "and " + items[-1]
    return ", ".join(items)


print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))
