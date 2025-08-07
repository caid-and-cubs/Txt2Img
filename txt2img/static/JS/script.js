const form = document.getElementById('generateForm');
const loading = document.getElementById('loading');
const result = document.getElementById('result');
const generateBtn = document.getElementById('generateBtn');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const prompt = document.getElementById('prompt').value;
    if (!prompt.trim()) return;
    
    // Show loading state
    loading.style.display = 'block';
    result.innerHTML = '';
    generateBtn.disabled = true;
    generateBtn.textContent = 'Generating...';
    
    try {
        const response = await fetch('/api/generate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: prompt })
        });
        
        const data = await response.json();
        
        if (data.success) {
            result.innerHTML = `
                <h3>Generated Image:</h3>
                <img src="${data.image_url}" alt="Generated image" class="generated-image">
                <p><strong>Prompt:</strong> ${data.prompt}</p>
            `;
        } else if (data.status === 'loading') {
            result.innerHTML = `
                <div class="status">
                    <p>Model is loading... Estimated time: ${data.estimated_time} seconds</p>
                    <p>Please try again in a moment.</p>
                </div>
            `;
        } else {
            result.innerHTML = `
                <div class="error">
                    <p>Error: ${data.error || 'Unknown error occurred'}</p>
                </div>
            `;
        }
    } catch (error) {
        result.innerHTML = `
            <div class="error">
                <p>Network error: ${error.message}</p>
            </div>
        `;
    } finally {
        // Hide loading state
        loading.style.display = 'none';
        generateBtn.disabled = false;
        generateBtn.textContent = 'Generate Image';
    }
});

// Check model status on page load
async function checkModelStatus() {
    try {
        const response = await fetch('/api/status/');
        const data = await response.json();
        
        if (data.status === 'loading') {
            result.innerHTML = `
                <div class="status">
                    <p>AI Model is warming up... Estimated time: ${data.estimated_time} seconds</p>
                </div>
            `;
        }
    } catch (error) {
        console.log('Status check failed:', error);
    }
}

// Check status when page loads
checkModelStatus();