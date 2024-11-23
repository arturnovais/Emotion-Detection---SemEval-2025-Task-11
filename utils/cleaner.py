import re
from Args.clean_args import CleanArgs

class Cleaner():
    def __init__(self):
        self.args = CleanArgs()
        
        
    def clean_laught(self, text):
        laugh_token = self.args.LAUGHT_TOKEN
        laugh_pattern = r'\b[kK]{2,}\b'
        return re.sub(laugh_pattern, laugh_token, text)
    

    def clean_text(self, text):
        return self.clean_laught(text)