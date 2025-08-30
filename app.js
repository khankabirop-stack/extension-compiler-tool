const API_URL = "http://localhost:8000/compile"; // change after deploy

document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById("fileInput");
  if (!fileInput.files.length) return alert("Please select a file");

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  document.getElementById("status").innerText = "Compiling...";

  const res = await fetch(API_URL, { method: "POST", body: formData });
  if (res.ok) {
    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "output.aix";
    document.body.appendChild(a);
    a.click();
    a.remove();
    document.getElementById("status").innerText = "Done ✅";
  } else {
    document.getElementById("status").innerText = "Error compiling ❌";
  }
});
