import os

# 경로 요소 결합
path1 = "C:/Users"
path2 = "Username"
full_path = os.path.join(path1, path2)
print("Joined Path:", full_path)

# 경로 존재 여부 확인
file_path = "/path/to/your/file.txt"
if os.path.exists(file_path):
    print("File exists:", file_path)
else:
    print("File does not exist:", file_path)

# 파일 또는 디렉토리 여부 확인
if os.path.isfile(file_path):
    print("It's a file:", file_path)
elif os.path.isdir(file_path):
    print("It's a directory:", file_path)

# 파일 이름과 확장자 분리한다
file_name = "example.txt"
name, extension = os.path.splitext(file_name)
print("File Name:", name)
print("Extension:", extension)

# 절대 경로로 변환한다
relative_path = "../documents/file.txt"
absolute_path = os.path.abspath(relative_path)
print("Absolute Path:", absolute_path)
