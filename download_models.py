import os
import subprocess

def download_file(file_id, output_path):
    if os.path.exists(output_path):
        print(f"{output_path} đã tồn tại, bỏ qua tải.")
        return
    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Đang tải file từ {url} về {output_path} ...")
    try:
        import gdown
        gdown.download(url, output_path, quiet=False)
    except ImportError:
        print("gdown chưa được cài đặt, đang cài đặt...")
        subprocess.check_call(["pip", "install", "--upgrade", "gdown"])
        import gdown
        gdown.download(url, output_path, quiet=False)

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)

    # ID file TinyLlama
    tinyllama_file_id = "16xOFZJBXuSGrGEEZJo3cNaCVtRNMgE2K"
    tinyllama_path = "models/tinyllama-1.1b-chat-v1.0.Q2_K.gguf"
    download_file(tinyllama_file_id, tinyllama_path)