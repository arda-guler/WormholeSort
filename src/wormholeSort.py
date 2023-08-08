class WormholeList:
    def __init__(self, data):
        self.data = data
        self.idxmap = self.generate_idxmap()

    def generate_idxmap(self):
        idxmap = []
        items_with_sames = []
        for item in self.data:
            low_count = 0
            same_count = 0
            for item2 in self.data:
                if item2 < item:
                    low_count += 1
                elif item2 == item:
                    same_count += 1

            same_count -= 1

            if same_count > 0:
                num_of_sames = 0
                for potential_same in items_with_sames:
                    if item == potential_same:
                        num_of_sames += 1

                item_idx = low_count + num_of_sames
                items_with_sames.append(item)

            else:
                item_idx = low_count

            idxmap.append(item_idx)

        return idxmap

    def __getitem__(self, idx):
        return self.data[self.idxmap.index(idx)]

    def __repr__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)
