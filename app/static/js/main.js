document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const searchInput = document.getElementById('campaign-search');
    const filterSelect = document.getElementById('campaign-filter');
    const campaignCards = document.querySelectorAll('.campaign-card');
    const modal = document.getElementById('emailModal');
    const closeBtn = document.querySelector('.close');
    const modalContent = document.querySelector('.email-preview');

    // Email Preview Handler
    window.showEmailPreview = function(campaignId) {
        if (!modal || !modalContent) return;
        
        modal.style.display = 'block';
        modalContent.innerHTML = '<div class="loading">Loading preview...</div>';

        fetch(`/generate_email/${campaignId}`)
            .then(response => {
                if (!response.ok) throw new Error('Network response error');
                return response.json();
            })
            .then(data => {
                if (data.status === 'error') throw new Error(data.message);
                
                // Update preview content
                const emailTo = document.getElementById('emailTo');
                const emailSubject = document.getElementById('emailSubject');
                const emailBody = document.getElementById('emailBody');
                const sendBtn = document.getElementById('sendEmailBtn');

                if (emailTo) emailTo.textContent = data.recipients;
                if (emailSubject) emailSubject.textContent = data.subject;
                if (emailBody) emailBody.innerHTML = data.body.replace(/\n/g, '<br>');

                // Setup send button
                if (sendBtn) {
                    sendBtn.onclick = function(e) {
                        e.preventDefault();
                        window.location.href = data.mailto;
                        modal.style.display = 'none';
                    };
                }
            })
            .catch(error => {
                console.error('Preview error:', error);
                modalContent.innerHTML = `
                    <div class="error-message">
                        Failed to load email preview. Please try again.
                        <div class="error-details">${error.message}</div>
                    </div>`;
            });
    };

    // Campaign Filter Function
    function filterCampaigns() {
        if (!searchInput || !filterSelect || !campaignCards) return;

        const searchTerm = searchInput.value.toLowerCase();
        const filterValue = filterSelect.value;
        
        campaignCards.forEach(card => {
            const title = card.querySelector('h2')?.textContent.toLowerCase() || '';
            const status = card.querySelector('.status-badge')?.textContent.toLowerCase() || '';
            const matchesSearch = title.includes(searchTerm);
            const matchesFilter = filterValue === 'all' || status === filterValue;
            
            card.style.display = matchesSearch && matchesFilter ? 'block' : 'none';
            card.classList.toggle('archived', status === 'archived');
        });
    }

    // Modal Control Functions
    function closeModal() {
        if (modal) modal.style.display = 'none';
    }

    // Event Listeners
    if (searchInput) {
        searchInput.addEventListener('input', filterCampaigns);
    }

    if (filterSelect) {
        filterSelect.addEventListener('change', filterCampaigns);
    }

    if (closeBtn) {
        closeBtn.addEventListener('click', closeModal);
    }

    window.onclick = function(event) {
        if (event.target === modal) {
            closeModal();
        }
    };

    // Copy Email Functionality
    const copyEmailBtn = document.getElementById('copy-email');
    if (copyEmailBtn) {
        copyEmailBtn.addEventListener('click', () => {
            const emailContent = document.querySelector('.email-content')?.innerText;
            if (!emailContent) return;

            navigator.clipboard.writeText(emailContent)
                .then(() => {
                    copyEmailBtn.textContent = 'Copied!';
                    setTimeout(() => {
                        copyEmailBtn.textContent = 'Copy Email Text';
                    }, 2000);
                })
                .catch(err => console.error('Copy failed:', err));
        });
    }

    // Initialize
    filterCampaigns();
});