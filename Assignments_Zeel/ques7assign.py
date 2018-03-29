
def hour_to_min(inp):
    mins= (inp*60)
    return mins
def min_to_sec(mins):
    secs= (mins*60)
    return secs

inp = int(input("Please enter an hour?  "))
print("Result of hours hours sec", min_to_sec(hour_to_min(inp)))
