from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

#get_files_info("calculator", ".")
#get_files_info("calculator", "pkg")
#get_files_info("calculator", "/bin")
#get_files_info("calculator", "../")

#content = get_file_content("calculator", "lorem.txt")
#print(content)
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))
