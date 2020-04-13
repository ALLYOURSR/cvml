
def PackList(list_):
    """Generally each element in list_ should have element _pack() which returns a dictlike object
    But this is python so anything goes"""
    packed = []
    for l in list_:
        if not "_pack" in l.__dict__:
            continue
        else:
            packed.append(l._pack())

def PackOne(self, pack_name, packable):
        if type(packable) is str:
            self[pack_name] = packable
        elif type(packable) is int:
            self[pack_name] = str(packable)
        elif type(packable) is list: #TODO replace with test for collection?
            self[pack_name] = PackList(packable)
        elif "_pack" in packable.__dict__:
            self[pack_name] = packable._pack()
        else:
            raise AttributeError("All objects passed to _pack_one must be of type {} or have method {}".format({"str", "int"}, "_pack()"))

        print("Packing {}".format(pack_name))