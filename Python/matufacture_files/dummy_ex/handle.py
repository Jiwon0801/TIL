import os

# mac
# os.chdir('/Users/student/PycharmProjects/matufacture_files/dummy_ex')

# windows
os.chdir(r'C:\Users\student\PycharmProjects\matufacture_files\dummy_ex')

filenames = os.listdir('.')
for filename in filenames:
    txt = os.path.splitext(filename)[-1].lower()
    if txt == '.txt':
        os.rename(filename, filename.replace('지원자', '합격자'))








