// Define the API endpoint URL
const apiUrl = 'http://localhost:8000/products/';

// Define the function to fetch the data
async function fetchData() {
  try {
    // Send a GET request to the API endpoint
    const response = await fetch(apiUrl);
    // Check if the response was successful
    if (response.ok) {
      // Parse the response data as JSON
      const data = await response.json();
      // Display the data on the HTML page
      displayData(data);
    } else {
      console.error('Error fetching data:', response.status);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Define the function to display the data
function displayData(data) {
  // Get the div element to display the data
  const dataContainer = document.getElementById('data-container');
  // Clear the div element
  dataContainer.innerHTML = '';
  // Loop through the data and create HTML elements to display it
  data.forEach(item => {
    const element = document.createElement('p');
    element.textContent = `ID: ${item.id}, Name: ${item.name}`;
    dataContainer.appendChild(element);
  });
}

// Call the function to fetch the data
fetchData();
