class auto_dict():
    def __init__(self, text_file:str, web_dict:str) -> None:
        self.wordset = self.take_word(text_file)

    def take_word(self, file:str) -> list:
        with open(file, "r") as f:
            content = f.read()
        return content.split("\n")

    