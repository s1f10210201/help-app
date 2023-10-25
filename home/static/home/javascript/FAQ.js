function askQuestion() {
    const userQuestion = document.getElementById("userQuestion").value;
    const answerElement = document.getElementById("answer");

    // ChatGPT APIに質問を送信して、回答を受け取ることができるコードをここに追加

    // 仮の回答（APIを使用した実際の回答に置き換える）
    const answer = getAnswer(userQuestion);

    answerElement.textContent = `A: ${answer}`;
}

function getAnswer(question) {
    // ChatGPT APIを呼び出して質問に対する回答を取得します
    // 実際のAPIリクエストと応答のロジックに置き換える必要があります

    // 仮の回答
    return "ChatGPTはAIベースの言語モデルです。";
}
