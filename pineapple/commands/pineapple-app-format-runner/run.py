import os
import sys

def binary_to_text(binary_lines):
    chars = [chr(int(line.strip(), 2)) for line in binary_lines if line.strip()]
    return ''.join(chars)

def run_pineapple_app(file_path):
    if not os.path.exists(file_path):
        print(f"[ERROR] The file '{file_path}' does not exist.")
        return

    with open(file_path, 'r') as f:
        binary_lines = f.readlines()

    decoded_code = binary_to_text(binary_lines)

    app_name = os.path.basename(file_path).replace(".pineapple_app", "")
    temp_file = f"/tmp/temp_{app_name}_file.pineapple_binary_app_source"

    with open(temp_file, "w") as temp:
        temp.write(decoded_code)

    os.system(f"python3 {temp_file}")
    os.remove(temp_file)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_pineapple_app(sys.argv[1])
    else:
        print("[ERROR] No .pineapple_app file provided.")
