from opencc import OpenCC

mode_config = {
    "簡體->繁體":"s2t",
    "簡體->繁體台灣":"s2tw",
    "簡體->繁體台灣(含慣用詞)": "s2twp"
}
MODE = "簡體->繁體台灣(含慣用詞)"
FILE_INPUT = "data/input.txt"
FILE_OUTPUT = "data/output.txt"
#%%
if __name__ == "__main__":
    cc = OpenCC(mode_config[MODE])

    # 輸入
    with open(FILE_INPUT, "r", encoding="utf-8") as f:
        text = f.read()
    
    # 輸出
    with open(FILE_OUTPUT, "w", encoding="utf-8") as f:
        f.write(cc.convert(text))