def make_extremum(type="max"):
    def extremum(collection):
        if type == "max":
            return max(collection)
        else:
            return min(collection)
    return extremum