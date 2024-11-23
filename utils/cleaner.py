import re
from Args.clean_args import CleanArgs

class Cleaner():
    def __init__(self):
        self.args = CleanArgs()
        
        
    def clean_laught(self, text):
        laugh_token = self.args.LAUGHT_TOKEN
        laugh_pattern = r'\b[kK]{2,}\b'
        return re.sub(laugh_pattern, laugh_token, text)
    
    
    def aplly_abbreviations(self, text):
        for abbr, full_form in self.abbreviations.items():
            text = re.sub(r'\b' + re.escape(abbr) + r'\b', full_form, text)
        return text
    

    def clean_text(self, text):
        text = self.apply_abbreviations(text)
        text = self.clean_laught(text)
        
        return text