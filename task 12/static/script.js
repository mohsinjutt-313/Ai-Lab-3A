document.getElementById('predictForm').addEventListener('submit', async function(e){
  e.preventDefault();
  const payload = {
    Crop: document.getElementById('Crop').value,
    Crop_Year: document.getElementById('Crop_Year').value,
    Season: document.getElementById('Season').value,
    State: document.getElementById('State').value,
    Area: document.getElementById('Area').value,
    Annual_Rainfall: document.getElementById('Annual_Rainfall').value,
    Fertilizer: document.getElementById('Fertilizer').value,
    Pesticide: document.getElementById('Pesticide').value,
  };

  const res = await fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  const data = await res.json();
  const el = document.getElementById('result');
  if (data.predicted_yield !== undefined) {
    el.textContent = 'Predicted Yield: ' + data.predicted_yield.toFixed(4);
  } else {
    el.textContent = 'Prediction failed';
  }
});
