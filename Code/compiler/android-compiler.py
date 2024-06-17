import os
from os.path import basename
from classes.Utils import *
from classes.Compiler import *
#
# if __name__ == "__main__":
#     argv = sys.argv[1:]
#     length = len(argv)
#     if length != 0:
#         input_file = argv[0]
#     else:
#         print("Error: not enough argument supplied:")
#         print("android-compiler.py <input file>")
#         exit(0)

input_folder_path = "/Users/abhjha8/kaggle_competitions/Image2Code/pix2code/datasets/android/model_result_gui"
output_folder_path = "/Users/abhjha8/kaggle_competitions/Image2Code/pix2code/datasets/android/model_result_final/"


TEXT_PLACE_HOLDER = "[TEXT]"
ID_PLACE_HOLDER = "[ID]"

dsl_path = "assets/android-dsl-mapping.json"
compiler = Compiler(dsl_path)


def render_content_with_text(key, value):
    value = value.replace(TEXT_PLACE_HOLDER, Utils.get_random_text(length_text=5, space_number=0))
    while value.find(ID_PLACE_HOLDER) != -1:
        value = value.replace(ID_PLACE_HOLDER, Utils.get_android_id(), 1)
    return value

# file_uid = basename(input_file)[:basename(input_file).find(".")]
# path = input_file[:input_file.find(file_uid)]
#
# input_file_path = "{}{}.gui".format(path, file_uid)
# output_file_path = "{}{}.xml".format(path, file_uid)
#
# compiler.compile(input_file_path, output_file_path, rendering_function=render_content_with_text)

exception_count=0;total_count=0
for input_file in os.listdir(input_folder_path):
    input_file = "{}/{}".format(input_folder_path, input_file)
    file_uid = basename(input_file)[:basename(input_file).find(".")]
    path = input_file[:input_file.find(file_uid)]
    input_file_path = "{}{}.gui".format(path, file_uid)
    output_file_path = "{}{}.xml".format(output_folder_path, file_uid)

    try:
        compiler.compile(input_file_path, output_file_path, rendering_function=render_content_with_text)
    except Exception as e:
        print("Not able to compile file: {}".format(input_file))
        print("Exception raised {}".format(e))
        exception_count+=1
        continue
    total_count+=1

print("Total files: {} and exception count: {}".format(total_count, exception_count))