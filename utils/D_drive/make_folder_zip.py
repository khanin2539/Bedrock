import shutil


directory_name = '11_15_2021_8th_test_corrupted_cropped'
zip_name = directory_name

# Create 'path\to\zip_file.zip'
shutil.make_archive(zip_name, 'zip', directory_name)


