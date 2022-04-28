from FileType import File


class JsonFile(File):
    """
    JSON class that converts JSON file to CSV file
    Only the following specified json input-type can be converted:
        {
            "Row1" : {
                "key": value
                },
            "Row2" : {
                "key": value
                }
        }
    """
    def __init__(self, filename, fileout):
        super().__init__()
        self._csv = ''
        self._values = []
        self._keys = []
        self._output = fileout

        # Receiving data from File of ".json" type
        self._data = self.ReadFile(filename)

        # Performing Parsing of the data
        self.ParseInput()

        # Writing the parsed data to the file
        self.WriteOutput()

    def ParseInput(self):
        """
        Parsing of JSON data and reformatting it to CSV data. Note that the expected JSON structure is the following:
            {
            "Row1" : {
                "key": value
                },
            "Row2" : {
                "key": value
                }
            }
        :return:
        """
        # Retrieving keys and values from list
        self._keys, self._values = self.KeyValuesList(self._data)

        # Formatting keys list
        self._keys = [key[key.find('"') + 1: len(key) - 1] for key in self._keys]

        # Creating values holder
        body = list()
        body_csv = ''

        # Formatting values list
        for i in range(len(self._values)):
            self._values[i] = [val.lstrip()[1:] if val.find('"') != -1 else val.lstrip() for val in self._values[i]]
            for item in self._values[i]:
                if item != self._values[i][-1]:
                    if item.find('"') != -1:
                        body.append(item[:item.find('"')])
                    else:
                        body.append(item[:item.find(',')])
                else:
                    if item.find('"') != -1:
                        body.append(item[:item.find('"')])
                    else:
                        body.append(item[:-1])
        index = 0

        # Formatting to csv format obtained values
        for _ in body:
            if str(_).find(',') != -1:
                _ = '"' + _ + '"'
            body_csv += _ + ','
            if not (index + 1) % len(self._keys):
                body_csv = body_csv[:-1] + '\n'
            index += 1

        # Formatting to csv format all data
        self._csv = ','.join(self._keys) + '\n' + body_csv[:-1] + '\n'

    def WriteOutput(self):
        # Opening file to write
        with open(self._output, 'w') as out:
            out.write(self._csv)
            out.write('\n')

    def __str__(self):
        return self._csv

    @staticmethod
    def KeyValuesList(array) -> ([], []):
        """
        Splits JSON formatted data according to ':' char and return keys and values as packed lists
        :param array:
        :return:
        """
        all_values = []
        begin = 0
        end = 0

        # Retrieving all data to a single list
        for i in range(1, len(array) - 1):
            if array[i].find('{') != -1 or array[i].find('}') != -1 and not begin:
                begin = i
            elif array[i].find('{') != -1 or array[i].find('}') != -1 and not end:
                end = i
                all_values.append(array[begin + 1: end])
                begin = 0
                end = 0
        key, values = [], []

        # Splitting data
        for i in range(len(all_values)):
            value = list()
            for item in all_values[i]:
                x, y = item.split(':')
                if x not in key:
                    key.append(x)
                value.append(y)
            values.append(value)

        return key, values
