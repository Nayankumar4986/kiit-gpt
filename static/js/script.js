async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST", headers: {
      "Content-Type": "application/json",
    },body: JSON.stringify(data), 
  });
  return response.json(); 
}


function reloadPage() {
    location.reload();
}



sendButton.addEventListener("click",async()=>{
  ////questionInput used as question in video check before using
    const questionInput = document.getElementById("questionInput").value;
    if (questionInput !== null) {
        questionInput.value = "";
      }
    document.querySelector(".right2").style.display = "block";
    document.querySelector(".right1").style.display = "none";

    const question1=document.getElementById("question1");
    const question2=document.getElementById("question2");
    question1.innerHTML=questionInput;
    question2.innerHTML=questionInput;

    let result = await postData("/api", {"question": questionInput})
    solution.innerHTML=result.result
})