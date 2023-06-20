import json
import os
import pandas as pd


def process_json_file(file_path, output_path, output_num):
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)

    df = pd.json_normalize(data)

    # Excel sınırını aşıyorsa, output_num parametresine göre dosya ismi oluştur
    if len(df) > 1048576:
        new_output_path = os.path.splitext(output_path)[0] + f"-{output_num}.xlsx"
        df[:1048576].to_excel(new_output_path, index=False)
        remaining_df = df[1048576:]
        if len(remaining_df) > 0:
            process_remaining_df(remaining_df, new_output_path, output_num + 1)
    else:
        df.to_excel(output_path, index=False)


def process_remaining_df(df, output_path, output_num):
    if len(df) > 1048576:
        new_output_path = os.path.splitext(output_path)[0] + f"-{output_num}.xlsx"
        df[:1048576].to_excel(new_output_path, index=False)
        remaining_df = df[1048576:]
        if len(remaining_df) > 0:
            process_remaining_df(remaining_df, new_output_path, output_num + 1)
    else:
        df.to_excel(output_path, index=False)


def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                output_path = os.path.splitext(file_path)[0] + ".xlsx"
                process_json_file(file_path, output_path, 2)


folder_path = "C:/Users/ilker/tweet-scraper/all-json/Osmaniye"
process_folder(folder_path)
