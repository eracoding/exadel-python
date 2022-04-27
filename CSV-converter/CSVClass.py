from FileType import File


class CsvFile(File):
    """
        CSV class that converts CSV file to JSON file
        Note that the JSON structure produced is the following:
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
        self._csv_header = None
        self._csv_body = []
        self._json = ''
        self._output = fileout

        # Receiving data from File of ".csv" type
        self._data = self.ReadFile(filename)

        # Performing Parsing of the data
        self.ParseInput()

        # Writing the parsed data to the file
        self.WriteOutput()

    def ParseInput(self):
        """
        Parsing of CSV data and reformatting it to JSON data. Note that the JSON structure produced is the following:
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
        # Retrieving all keys
        self._csv_header = self._data.pop(0).rstrip('\n').split(',')

        # Retrieving all values
        self._data = [item.rstrip('\n').split(',') for item in self._data]

        # Concatenating the splitted by ',' double quotes
        self.concatenateOverDouble(self._csv_header)

        # Concatenating the splitted by ',' single quotes
        self.concatenateOverSingle(self._csv_header)
        for item in self._data:
            # Concatenating the splitted by ',' double quotes
            self.concatenateOverDouble(item)

            # Concatenating the splitted by ',' double quotes
            self.concatenateOverSingle(item)

            # Removing double quotes
            item = [elem.replace('"', '') for elem in item]

            # Removing single quotes
            item = [elem.replace("'", '') for elem in item]

            # Adding formatted elements of list
            self._csv_body.append(item)

        # Formatting JSON structured output as string
        self._json += '{'
        for i in range(len(self._csv_body)):
            # Adding Row# to structure
            self._json += f'\n\t"Row{i+1}" : {{'
            for k in range(len(self._csv_header)):
                # Checking whether to add comma at the end or not
                if k != len(self._csv_header) - 1:
                    # Checking if the value is number or not, if so -> removing double quotes
                    if self._csv_body[i][k].isnumeric():
                        self._json += f'\n\t\t"{self._csv_header[k]}": {self._csv_body[i][k]},'
                    else:
                        self._json += f'\n\t\t"{self._csv_header[k]}": "{self._csv_body[i][k]}",'
                else:
                    # Checking if the value is number or not, if so -> removing double quotes
                    if self._csv_body[i][k].isnumeric():
                        self._json += f'\n\t\t"{self._csv_header[k]}": {self._csv_body[i][k]}'
                    else:
                        self._json += f'\n\t\t"{self._csv_header[k]}": "{self._csv_body[i][k]}"'
            # Closing the Row# and checking whether it is the last row or not
            if i != len(self._csv_body) - 1:
                self._json += '\n\t},'
            else:
                self._json += '\n\t}'
        # Closing the Json format
        else:
            self._json += '\n}'

    def WriteOutput(self):
        # Opening file to write
        with open(self._output, 'w') as out:
            out.write(self._json)
            out.write('\n')

    def __str__(self):
        return self._json

    @staticmethod
    def concatenateOverDouble(value):
        """
        Concatenating list elements which contain Double quote character inside
        :param value:
        :return:
        """
        # Index start
        begin = 0
        # Index end
        end = 0
        i = 0
        for item in value:
            # Setting the first element that contain quote
            if item.find('"') != -1 and not begin and not end:
                begin = i
            # Setting the last element that contain quote and concatenating them. Setting again the start and end to 0
            elif item.find('"') != -1 and begin and not end:
                end = i
                value[begin:end + 1] = [','.join(value[begin:end + 1])]
                begin = 0
                end = 0
            i += 1

    @staticmethod
    def concatenateOverSingle(value):
        """
        Concatenating list elements which contain Single quote character inside
        :param value:
        :return:
        """
        # Index start
        begin = 0
        # Index end
        end = 0
        i = 0
        for item in value:
            # Setting the first element that contain quote
            if item.find("'") != -1 and not begin and not end:
                begin = i
            # Setting the last element that contain quote and concatenating them. Setting again the start and end to 0
            elif item.find("'") != -1 and begin and not end:
                end = i
                value[begin:end + 1] = [','.join(value[begin:end + 1])]
                begin = 0
                end = 0
            i += 1

