document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const searchInput = document.getElementById('campaign-search');
    const filterSelect = document.getElementById('campaign-filter');
    const campaignCards = document.querySelectorAll('.campaign-card');
    const modal = document.getElementById('emailModal');
    const closeBtn = document.querySelector('.close');

    // Email Preview System
    window.showEmailPreview = function(campaignId) {
        const modal = document.getElementById('emailModal');
        const modalContent = modal.querySelector('.modal-content');
        
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
        
        const emailPreview = modalContent.querySelector('.email-preview');
        emailPreview.innerHTML = '<div class="loading">Loading preview...</div>';

        fetch(`/generate_email/${campaignId}`)
            .then(response => {
                if (!response.ok) throw new Error('Network response error');
                return response.json();
            })
            .then(data => {
                if (data.status === 'error') throw new Error(data.message);
                
                emailPreview.innerHTML = `
                    <div class="email-field">
                        <label>To:</label>
                        <span>${data.recipients}</span>
                    </div>
                    <div class="email-field">
                        <label>Subject:</label>
                        <span>${data.subject}</span>
                    </div>
                    <div class="email-content">${data.body.replace(/\n/g, '<br>')}</div>
                `;
                
                const sendBtn = document.getElementById('sendEmailBtn');
                if (sendBtn) {
                    sendBtn.onclick = function() {
                        window.location.href = data.mailto;
                        closeModal();
                    };
                }
            })
            .catch(error => {
                console.error('Preview error:', error);
                emailPreview.innerHTML = `
                    <div class="error-message">
                        Failed to load email preview. Please try again.
                        <div class="error-details">${error.message}</div>
                    </div>`;
            });
    };

    // Modal Control Functions
    function closeModal() {
        if (modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    }

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

    // Close modal on outside click
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