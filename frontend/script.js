fetch("http://localhost:5000/api/matches")
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById("matches");
    data.forEach(match => {
      const li = document.createElement("li");
      li.textContent = `${match.home} vs ${match.away}  ${match.score}`;
      list.appendChild(li);
    });
  });
