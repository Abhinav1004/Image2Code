import os
from os.path import basename
from classes.Utils import *
from classes.Compiler import *

input_folder_path = "/Users/abhjha8/kaggle_competitions/Image2Code/pix2code/datasets/web/model_result_gui"
output_folder_path = "/Users/abhjha8/kaggle_competitions/Image2Code/pix2code/datasets/web/model_result_final/"
FILL_WITH_RANDOM_TEXT = True
TEXT_PLACE_HOLDER = "[]"
dsl_path = "assets/web-dsl-mapping.json"
compiler = Compiler(dsl_path)

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

def render_content_with_text(key, value):
    if FILL_WITH_RANDOM_TEXT:
        if key.find("btn") != -1:
            value = value.replace(TEXT_PLACE_HOLDER, Utils.get_random_text())
        elif key.find("title") != -1:
            value = value.replace(TEXT_PLACE_HOLDER, Utils.get_random_text(length_text=5, space_number=0))
        elif key.find("text") != -1:
            value = value.replace(TEXT_PLACE_HOLDER,
                                  Utils.get_random_text(length_text=56, space_number=7, with_upper_case=False))
    return value

exception_count=0;total_count=0
for input_file in os.listdir(input_folder_path):
    input_file = "{}/{}".format(input_folder_path, input_file)
    file_uid = basename(input_file)[:basename(input_file).find(".")]
    path = input_file[:input_file.find(file_uid)]
    input_file_path = "{}{}.gui".format(path, file_uid)
    output_file_path = "{}{}.html".format(output_folder_path, file_uid)

    try:
        compiler.compile(input_file_path, output_file_path, rendering_function=render_content_with_text)
    except Exception as e:
        print("Not able to compile file: {}".format(input_file))
        print("Exception raised {}".format(e))
        exception_count+=1
        continue
    total_count+=1

print("Total files: {} and exception count: {}".format(total_count, exception_count))