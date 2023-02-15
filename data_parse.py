import os


def parse_speeches(src_file, target_dir):
    with open(src_file, "rb") as speeches_file:
        speeches = speeches_file.read().decode("utf-8", "ignore")
        for i, speech in enumerate(speeches.split("\n")):
            with open(target_dir + "\\" + f"speech{i}.txt", "wb") as my_file:
                my_file.write(speech.replace("</p><p>", "").encode("utf-8", "ignore"))


if __name__ == "__main__":
    parse_speeches("speeches\Cleaned_Speeches\Speeches_ECB_Cleaned.csv", "parsed_speeches")