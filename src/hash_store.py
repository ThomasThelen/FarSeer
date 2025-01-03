class HashStore:
    def __init__(self, record_path):
        self.maps = {}
        with open(record_path, 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                line = line.split(',')
                self.maps[line[0]] = line[1]

    def map_status(self, hash: str):
        """

        :param hash:
        :return:
        """
        if hash not in self.maps:
            return "unknown"
        return self.maps[hash]
