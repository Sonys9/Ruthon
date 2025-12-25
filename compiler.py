import characters

class Compiler:
    def __init__(self, file_name):
        self.file_name = file_name

    def etoc(self, data):
        result = []
        in_quotes = False
        for k in data:
            if k == "'" or k == '"':
                result.append(k)
                in_quotes = not in_quotes
            elif k.lower() in characters.characters and not in_quotes:
                result.append(characters.characters[k.lower()] if k.islower() else characters.characters[k.lower()].upper())
            else:
                result.append(k)
        return ''.join(result)

    def convert(self):
        with open(self.file_name, 'r') as f:
            self.file_content = f.read()
            self.converted_content = self.etoc(self.file_content)

    def save(self):
        with open(self.file_name.replace('.py', '.пй'), 'w') as f:
            f.write(self.converted_content)