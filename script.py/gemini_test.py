from google import genai
client = genai.Client(api_key="AIzaSyD3zRq6ScGkWW7aghQVYC779yAcW4IvsWA")
# キャラクター設定
character = "あなたは阿波弁botです。必ず阿波弁で返答してください。"
# 履歴（ユーザーとAIの発言のみ）
history = []
print("阿波弁botです。終了はqキーを押してください")
while True:
    user_input = input("あなた: ")
    if user_input == "q":
        print("終了します")
        break
    # 履歴にユーザーの発言を追加
    history.append(f"ユーザー: {user_input}")
    # キャラクター設定 + 会話履歴全体をプロンプトに組み立てる
    prompt = character + "\n\n" + "\n".join(history) + "\nAI: "
    response = client.models.generate_content(
        model="gemini-3-flash-preview",  
        contents=prompt
    )
    ai_reply = response.text.strip()
    # 履歴にAIの返答を追加
    history.append(f"AI: {ai_reply}")
    print(f"AI: {ai_reply}")