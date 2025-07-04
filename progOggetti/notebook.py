
import sys
import datetime
class Note:
    note_db=[]
    def __init__(self,memo,tags,):
        self.memo = memo
        self.tags = tags 
        self.creation_date = datetime.date.today()
        last_id = 0
        last_id += 1
        self.id=last_id
    def __repr__(self):
        return "memo:"+self.memo+"\ntags:"+self.tags+"\ndate:"+str(self.creation_date)+"\nid:"+str(self.id)
    
    def match(self,string):
        for note in self.note_db:
            if note.memo == string:
                return True
        return False
    
class Notebook:
    def __init__(self):
        self.db=Note.note_db

    def add(self,memo,tags=""):
        self.db.append(Note(memo,tags))

    def modify(self,id,memo,tags):
        for note in self.db:
            if note.id == id:
                note.memo =memo 
                note.tags = tags
                break
        return "Nota modificata con successo!"
    
    def search(self,memo):
        for note in self.db:
            if note.match(memo):
                return note
            
class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choose = {"1":self._show_notes,
                       "2":self._add_notes,
                       "3":self._modify_notes,
                       "4":self._search_note,
                       "5":self._quit}
    

    def _show_menu(self):
        return """
        1.show all notes
        2.add a new note
        3.modify a note
        4.search a note
        5.quit"""
    
    def run(self):
        
        while True:
            print(self._show_menu())
            choose = input("choose what you want to do:")
            action = self.choose.get(choose)
            if action:
                action()
            else:
                print("invalid input")

    def _show_notes(self):
        for note in self.notebook.db:
            print("********************")
            print(note)

    def _add_notes(self):
        memo = str(input("insert the memo:"))
        tags = str(input("insert the tags:"))
        self.notebook.add(memo,tags)
        print("memo added succesfully")

    def _modify_notes(self):
        for note in self.notebook.db:
            print(note)
        id = int(input("insert the memo id you want to modify"))
        memo = str(input("insert the new memo:"))
        tags = str(input("insert the new tags"))
        self.notebook.add(id,memo,tags)
    
    def _search_note(self):
        memo = str(input("insert the mem of the note you want to search:"))
        print(self.notebook.search(memo))
        input("press enter to continue...")

    def _quit(self):
        print("quitting...")
        sys.exit(0)
if __name__=="__main__":
    m = Menu()
    m.run()