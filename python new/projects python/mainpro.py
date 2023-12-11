import os
def list_items():
   print(os.curdir)
   new_path=os.path.join(os.curdir,'words_dir')
   print(new_path)
   file1=os.listdir('words_dir')
   files=[os.path.join(new_path,f)for f in os.listdir(new_path)]
   print(file1)
   return (files)


def find_words(search):
   list_files=list_items()
   for file in list_files:
      with open(file,'r') as f:
         line=f.readlines()
         for x in line:
            if search in x:
               print(x)
find_words('jim')

