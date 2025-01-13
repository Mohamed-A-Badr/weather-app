document.addEventListener('DOMContentLoaded', () => {
    const weatherForm = document.getElementById('weatherForm');
    const locationInput = document.getElementById('location');
    const startDateInput = document.getElementById('startDate');
    const endDateInput = document.getElementById('endDate');
    const loadingIndicator = document.getElementById('loading');
    const weatherResults = document.getElementById('weatherResults');
    const temperatureData = document.getElementById('temperatureData');
    const errorMessage = document.getElementById('errorMessage');

    weatherForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Reset previous results
        weatherResults.style.display = 'none';
        errorMessage.style.display = 'none';
        loadingIndicator.style.display = 'block';

        const location = locationInput.value;
        const startDate = startDateInput.value;
        const endDate = endDateInput.value;

        try {
            const response = await fetch(`http://127.0.0.1:8000/api/weather/?location=${encodeURIComponent(location)}&start_date=${startDate}&end_date=${endDate}`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json'
                }
            });

            const responseData = await response.json();

            if (!response.ok) {
                // Use backend error message if available
                throw new Error(responseData.error || responseData.message || 'Weather data fetch failed');
            }

            // Parse and display weather data
            let resultHTML = `
                <div class="card-header bg-primary text-white">
                    <h5>Weather Forecast for ${responseData.resolvedAddress}</h5>
                </div>
                <ul class="list-group list-group-flush">
            `;

            // Iterate through days
            responseData.days.forEach(day => {
                resultHTML += `
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <div>
                            <strong>${day.datetime}</strong>
                            <p class="text-muted mb-0">${day.conditions}</p>
                        </div>
                        <div class="text-end">
                            <span class="badge bg-info me-2">Max: ${day.tempmax}°C</span>
                            <span class="badge bg-secondary">Min: ${day.tempmin}°C</span>
                        </div>
                    </li>
                `;
            });

            resultHTML += `</ul>
                <div class="card-footer text-muted">
                    <small>Timezone: ${responseData.timezone}${responseData.currentConditions ? ` | Local Time: ${responseData.currentConditions.datetime}` : ''}</small>
                </div>
            `;

            temperatureData.innerHTML = resultHTML;
            weatherResults.style.display = 'block';
        } catch (error) {
            console.error('Fetch error:', error);
            errorMessage.innerHTML = `
                <strong>Error:</strong> ${error.message}
                <button type="button" class="btn-close float-end" aria-label="Close"></button>
            `;
            errorMessage.style.display = 'block';
            
            // Add close button functionality
            const closeButton = errorMessage.querySelector('.btn-close');
            if (closeButton) {
                closeButton.addEventListener('click', () => {
                    errorMessage.style.display = 'none';
                });
            }
        } finally {
            loadingIndicator.style.display = 'none';
        }
    });
});