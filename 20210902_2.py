import re

# input_file = "20180817_for_2_task.txt"
input_file = str(input("Enter the file name to parse:\n")).replace("\"", "").replace("'", "")
output_file = "output.txt"
mode = str(input("""Enter type of messages [EWIA]
(example: E, or EW, or EWI, or EWIA etc.):\n""")).upper().replace("\"", "").replace("'", "")
dict_log = []


def content_parse(file_to_parse, file_to_fill):
    """
    Parses file for messages with corresponding pattern.
    If input mode is incorrect, returns empty list.
    Fills output file with all matching records.
    :param file_to_parse: Input file
    :param file_to_fill: Output file
    :return List of dictionaries
    """
    try:
        with open(file_to_parse, "r") as file_read:
            with open(file_to_fill, "w") as file_write:
                full_text = ""
                for line in file_read:
                    full_text += line
                    dict_sample = {"msg": "", "type": "", "offset": 0, "text": ""}
                    pattern = re.findall(f"MVF\d\d\d\d\d[{mode}]", line)

                    if pattern.__len__() > 0 and pattern[0] in line:
                        file_write.write(line.strip() + "\n")
                        dict_sample["msg"] = line.strip().split(" ")[0]
                        dict_sample["type"] = (line.strip().split(" ")[0])[-1]
                        dict_sample["offset"] = full_text.find(pattern[0])
                        dict_sample["text"] = line.strip()[len(dict_sample["msg"]) + 1:]
                        dict_log.append(dict_sample)

        print(dict_log)

    except FileNotFoundError:
        print(f"File \"{input_file}\" not found!")


if __name__ == "__main__":
    content_parse(input_file, output_file)
