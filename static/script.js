document.getElementById("timeBtn").addEventListener("click", async () => {
  const result = document.getElementById("result");
  try {
    const res = await fetch("/api/time");
    const data = await res.json();
    result.textContent = "Server time: " + data.time;
  } catch (e) {
    result.textContent = "Could not reach the server.";
  }
});
