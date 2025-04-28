document.addEventListener('DOMContentLoaded', function() {
    const pokerForm = document.getElementById('pokerForm');
    const clearButton = document.getElementById('clearButton');
    const resultCard = document.getElementById('resultCard');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const resultContent = document.getElementById('resultContent');
    const errorContent = document.getElementById('errorContent');
    const gameStage = document.getElementById('gameStage');
    const recommendedAction = document.getElementById('recommendedAction');
    const simulationCount = document.getElementById('simulationCount');
    const errorMessage = document.getElementById('errorMessage');

    // Handle form submission
    pokerForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show result card with spinner
        resultCard.style.display = 'block';
        loadingSpinner.style.display = 'block';
        resultContent.style.display = 'none';
        errorContent.style.display = 'none';
        
        // Scroll to result card
        resultCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        // Gather form data
        const formData = {
            holeCards: document.getElementById('holeCards').value.trim(),
            communityCards: document.getElementById('communityCards').value.trim(),
            stacks: document.getElementById('stacks').value.trim(),
            positions: document.getElementById('positions').value.trim(),
            potSize: document.getElementById('potSize').value.trim(),
            facingBet: document.getElementById('facingBet').value.trim(),
            minRaise: document.getElementById('minRaise').value.trim(),
            simulations: document.getElementById('simulations').value.trim() || '5000'
        };
        
        // Send data to server
        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            // Hide spinner
            loadingSpinner.style.display = 'none';
            
            if (data.error) {
                // Show error
                errorContent.style.display = 'block';
                errorMessage.textContent = data.error;
            } else {
                // Show result
                resultContent.style.display = 'block';
                gameStage.textContent = data.stage;
                recommendedAction.textContent = capitalizeFirstLetter(data.recommendation);
                simulationCount.textContent = data.simulations.toLocaleString();
                
                // Apply styling based on action
                const action = data.recommendation.split(' ')[0].toLowerCase();
                if (action === 'fold') {
                    recommendedAction.style.color = '#e74c3c';
                    recommendedAction.style.backgroundColor = 'rgba(231, 76, 60, 0.1)';
                } else if (action === 'call' || action === 'check') {
                    recommendedAction.style.color = '#f39c12';
                    recommendedAction.style.backgroundColor = 'rgba(243, 156, 18, 0.1)';
                } else if (action === 'raise') {
                    recommendedAction.style.color = '#27ae60';
                    recommendedAction.style.backgroundColor = 'rgba(39, 174, 96, 0.1)';
                }
            }
        })
        .catch(error => {
            // Hide spinner and show error
            loadingSpinner.style.display = 'none';
            errorContent.style.display = 'block';
            errorMessage.textContent = 'Network error. Please try again.';
            console.error('Error:', error);
        });
    });
    
    // Handle clear button
    clearButton.addEventListener('click', function() {
        pokerForm.reset();
        resultCard.style.display = 'none';
    });
    
    // Helper function to capitalize first letter
    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
    
    // Simple form validation for card format
    const holeCardsInput = document.getElementById('holeCards');
    const communityCardsInput = document.getElementById('communityCards');
    
    function validateCardFormat(input) {
        if (!input.value.trim()) return;
        
        const cardPattern = /^([AKQJT2-9][hsdc]\s*)+$/i;
        if (!cardPattern.test(input.value.trim())) {
            input.setCustomValidity('Invalid card format. Use rank (A,K,Q,J,T,9-2) followed by suit (h,s,d,c)');
        } else {
            input.setCustomValidity('');
        }
    }
    
    holeCardsInput.addEventListener('input', function() {
        validateCardFormat(this);
    });
    
    communityCardsInput.addEventListener('input', function() {
        validateCardFormat(this);
    });
    
    // Example presets for quick testing
    const examplePresets = [
        {
            name: 'Pre-flop AK suited',
            data: {
                holeCards: 'Ah Kh',
                communityCards: '',
                stacks: '1000 1200 800 1500 1300',
                positions: 'utg mp co btn sb',
                potSize: '100',
                facingBet: '50',
                minRaise: '',
                simulations: '5000'
            }
        },
        {
            name: 'Flop top pair',
            data: {
                holeCards: 'Ah Kh',
                communityCards: 'Ad 7c 2s',
                stacks: '950 1150 750 1450 1250',
                positions: 'utg mp co btn sb',
                potSize: '200',
                facingBet: '100',
                minRaise: '',
                simulations: '5000'
            }
        }
    ];
    
    // Add example data loading feature (uncomment to enable)
    /*
    const examplesSection = document.createElement('div');
    examplesSection.className = 'examples-section';
    examplesSection.innerHTML = '<h3>Example Hands</h3>';
    
    const exampleButtonsContainer = document.createElement('div');
    exampleButtonsContainer.className = 'example-buttons';
    
    examplePresets.forEach(preset => {
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'example-button';
        button.textContent = preset.name;
        button.addEventListener('click', () => {
            Object.entries(preset.data).forEach(([id, value]) => {
                const element = document.getElementById(id);
                if (element) element.value = value;
            });
        });
        exampleButtonsContainer.appendChild(button);
    });
    
    examplesSection.appendChild(exampleButtonsContainer);
    document.querySelector('.card-form').appendChild(examplesSection);
    */
});