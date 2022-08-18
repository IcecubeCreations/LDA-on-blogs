from enchant import Dict
import glob, os

ERROR_MARGIN = 0.5

DOCUMENTS_FOLDER = "txtfiles"

def lang_test():
    txt_path = os.path.join(DOCUMENTS_FOLDER)
    os.chdir(txt_path)
    for filename in glob.glob("*.txt"):        
        file = open(filename, 'r', encoding='utf-8')
        data = file.read()
        words = data.split()
        if len(words) == 0:
            continue 
        d = Dict("en_US")
        error_count = 0

        for w in words:
            error_count += not d.check(w)
    
        if error_count / len(words) > ERROR_MARGIN:
            print(filename)
        file.close()
    
if __name__ == "__main__":    
        lang_test()