from transformers import BertTokenizer

# 填写你的本地模型路径
model_path = "/root/SAGCN/SAGCN-ASTE-main/SAGCN-ASTE-main/bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained("/root/bert-base-uncased", local_files_only=True)
print(tokenizer("hello world"))