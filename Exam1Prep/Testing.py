class Node():
    def init(self, item, link):
        self._item = item
        self._link = link

    def __repr__(self):
        return f"Node: {self._item}"
        


if __name__ == "__main__":
    unittest.main()
    