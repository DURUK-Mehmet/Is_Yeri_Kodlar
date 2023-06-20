import json
import os
import pandas as pd
import xlsxwriter

def process_json_file(file_path, output_path):
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)

    df = pd.json_normalize(data)
    return df


def process_folder(folder_path):
    output_path = os.path.join(folder_path, "şanlıurfa.xlsx")
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                sheet_name = os.path.splitext(file)[0][:31]  # Max sheet name length is 31
                try:
                    df = process_json_file(file_path, output_path)
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                except pd.errors.EmptyDataError:
                    print(f"{file_path} is empty, skipping.")

    writer.save()

    # If the output file exceeds Excel limit, save to new files
    if os.path.getsize(output_path) > 25000000:
        output_num = 2
        while True:
            new_output_path = os.path.join(folder_path, f"output-{output_num}.xlsx")
            if not os.path.exists(new_output_path):
                writer = pd.ExcelWriter(new_output_path, engine='xlsxwriter')
                break
            output_num += 1

        for sheet_name, df in pd.read_excel(output_path, sheet_name=None).items():
            if len(df) > 1048576:
                df[:1048576].to_excel(writer, sheet_name=sheet_name, index=False)
                remaining_df = df[1048576:]
                while len(remaining_df) > 0:
                    if len(remaining_df) > 1048576:
                        output_num += 1
                        new_sheet_name = f"{sheet_name[:26]}-{output_num}"
                        remaining_df[:1048576].to_excel(writer, sheet_name=new_sheet_name, index=False)
                        remaining_df = remaining_df[1048576:]
                    else:
                        remaining_df.to_excel(writer, sheet_name=sheet_name, index=False)
                        remaining_df = pd.DataFrame()

        writer.save()
        os.remove(output_path)


folder_path = "C:/Users/ilker/tweet-scraper/all-json/şanlıurfa"
process_folder(folder_path)
