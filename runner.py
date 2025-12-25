import characters

class Runner:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_char(self, val):
        keys = [k for k, v in characters.characters.items() if v == val]
        return keys[0] if keys else '' 

    def ctoe(self, data):
        result = []
        in_quotes = False
        for k in data:
            if k == "'" or k == '"':
                result.append(k)
                in_quotes = not in_quotes
            elif k in characters.characters.values() and not in_quotes:
                result.append(self.get_char(k))
            else:
                result.append(k)
        return ''.join(result)

    def convert(self):
        with open(self.file_name, 'r') as f:
            self.file_content = f.read()
            self.converted_content = self.ctoe(self.file_content)

    def run(self):
        exec(self.converted_content)