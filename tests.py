from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


def test():
	# # Test ./functions/get_files_info.py
	# result = get_files_info("calculator", ".")
	# print("Result for current directory:")
	# print(result)
	# print("")
	# result = get_files_info("calculator", "pkg")
	# print("Result for 'pkg' directory:")
	# print(result)
	# print("")
	# result = get_files_info("calculator", "/bin")
	# print("Result for '/bin' directory")
	# print(result)
	# print("")
	# result = get_files_info("calculator", "../")
	# print("Result for '../' directory")
	# print(result)
	# print("")

	# # Tests ./functions/get_file_content.py
	# result = get_file_content("calculator", "main.py")
	# print(result)
	# print("")	
	# result = get_file_content("calculator", "pkg/calculator.py")
	# print(result)
	# print("")	
	# result = get_file_content("calculator", "/bin/cat")
	# print(result)
	# print("")	
	# result = get_file_content("calculator", "pkg/does_not_exist.py")
	# print(result)
	# print("")

	# Tests ./functions/write_file.py
	result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
	print(result)
	print("")

	result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
	print(result)
	print("")

	result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
	print(result)
	print("")


if __name__ == "__main__":
	test()
