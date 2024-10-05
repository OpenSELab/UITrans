from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
checkpoint = r"D:\Code\Python\harmony-pilot\models\reader\reader-lm-1.5b"

device = "cuda" # for GPU usage or "cpu" for CPU usage
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

# example html content
html_content = "\n<!DOCTYPE html>\n<html lang=\"cn\">\n  <head>\n    <meta charset=\"utf-8\"/>\n    <title>文档中心</title>\n    <base href=\"/consumer/cn/doc/\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>\n    <meta name=\"applicable-device\" content=\"pc,mobile\"/>\n    <link rel=\"icon\" type=\"image/x-icon\" href=\"favicon.ico\"/>\n    <link rel=\"canonical\" id=\"canonical\" href=\"\"/>\n    <meta name=\"MobileOptimized\" content=\"width\"/>\n    <meta name=\"jsha\" content=\"202408071049091\"/>\n    <meta name=\"HandheldFriendly\" content=\"true\"/>\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=Edge,chrome=1\"/>\n    <link rel=\"stylesheet\" href=\"/config/commonResource/font/font.css\"/>\n    <link rel=\"stylesheet\" href=\"./assets/css/reset.css?202408071049091\"/>\n    <script typet=\"text/javascript\" src=\"./assets/js/base.js?20240807104909\"></script>\n    <script typet=\"text/javascript\" src=\"./assets/const/official/env.20240808220342.js?20240807104912\"></script>\n    <script typet=\"text/javascript\" src=\"./assets/constant/search.js?20240807104909\"></script>\n    <link rel=\"stylesheet\" href=\"./assets/css/document.css?2024080710495\"/>\n    \n  <link rel=\"stylesheet\" href=\"styles.21482879eaad347fb311.css\"></head>\n  <body>\n    <app-root></app-root>\n  <script src=\"runtime-es2015.c020973bdbb05eb65ae9.js?20240919\" type=\"module\"></script><script src=\"runtime-es5.c020973bdbb05eb65ae9.js\" nomodule defer></script><script src=\"polyfills-es5.645418600718ba030061.js\" nomodule defer></script><script src=\"polyfills-es2015.6f7483ee715c6bd07e4c.js\" type=\"module\"></script><script src=\"vendor-es2015.e3f30e81c35df9b6923c.js\" type=\"module\"></script><script src=\"vendor-es5.e3f30e81c35df9b6923c.js\" nomodule defer></script><script src=\"main-es2015.876a55c0e203892b01da.js\" type=\"module\"></script><script src=\"main-es5.876a55c0e203892b01da.js\" nomodule defer></script></body>\n</html>\n"

messages = [{"role": "user", "content": html_content}]
input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)
attention_mask = (input_ids != tokenizer.pad_token_id)

streamer = TextStreamer(tokenizer=tokenizer, skip_prompt=True, skip_special_tokens=True)
model.generate(input_ids=input_ids, attention_mask=attention_mask, max_new_tokens=1024, temperature=0.01, streamer=streamer)


# print(tokenizer.decode(outputs[0], skip_special_tokens=True))
