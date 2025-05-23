import os
import subprocess

def download_file(url, output_path):
    if os.path.exists(output_path):
        print(f"{output_path} đã tồn tại, bỏ qua tải.")
        return
    print(f"Đang tải file từ {url} về {output_path} ...")
    try:
        import gdown
        # gdown vẫn dùng được với link trực tiếp Hugging Face (hoặc có thể dùng wget)
        subprocess.check_call(["wget", "-O", output_path, url])
    except Exception as e:
        print(f"Lỗi khi tải file: {e}")

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)
    hf_url = "https://huggingface.co/reach-vb/TinyLlama-1.1B-Chat-v1.0-Q2_K-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0-q2_k.gguf"
    output_path = "models/tinyllama-1.1b-chat-v1.0.Q2_K.gguf"
    download_file(hf_url, output_path)
