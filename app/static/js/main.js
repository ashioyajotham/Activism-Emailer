// Campaign search and filter
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('campaign-search');
    const filterSelect = document.getElementById('campaign-filter');
    const campaignCards = document.querySelectorAll('.campaign-card');
    const copyButton = document.getElementById('copy-email');
    const shareButtons = document.querySelectorAll('.share-btn');

    if (searchInput) {
        searchInput.addEventListener('input', debounce(filterCampaigns, 300));
    }

    if (filterSelect) {
        filterSelect.addEventListener('change', filterCampaigns);
    }

    // Search and filter functionality
function filterCampaigns() {
    const searchTerm = searchInput?.value.toLowerCase() || '';
    const filterValue = filterSelect?.value || 'all';
    
    campaignCards.forEach(card => {
        const title = card.querySelector('h2').textContent.toLowerCase();
        const status = card.querySelector('.status-badge').textContent.toLowerCase();
        const matchesSearch = title.includes(searchTerm);
        const matchesFilter = filterValue === 'all' || status === filterValue;
        
        card.style.display = matchesSearch && matchesFilter ? 'block' : 'none';
        
        // Add archived class if status is archived
        if (status === 'archived') {
            card.classList.add('archived');
        } else {
            card.classList.remove('archived');
        }
    });
}

    // Copy to clipboard functionality
    if (copyButton) {
        copyButton.addEventListener('click', async () => {
            const emailContent = document.querySelector('.email-content').textContent;
            try {
                await navigator.clipboard.writeText(emailContent);
                showToast('Email content copied to clipboard!');
            } catch (err) {
                showToast('Failed to copy email content', 'error');
            }
        });
    }

    // Share functionality
    shareButtons.forEach(button => {
        button.addEventListener('click', () => {
            const platform = button.dataset.platform;
            const url = window.location.href;
            const title = document.title;
            
            const shareUrls = {
                twitter: `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(title)}`,
                facebook: `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`,
                email: `mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(url)}`
            };

            window.open(shareUrls[platform], '_blank');
        });
    });
});

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function showToast(message, type = 'success') {
    const toast = document.getElementById('copy-confirmation');
    if (toast) {
        toast.textContent = message;
        toast.className = `toast ${type}`;
        toast.classList.remove('hidden');
        
        setTimeout(() => {
            toast.classList.add('hidden');
        }, 3000);
    }
}

function showEmailPreview(campaignId) {
    fetch(`/generate_email/${campaignId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('emailSubject').textContent = data.subject;
            document.getElementById('emailBody').innerHTML = data.body.replace(/\n/g, '<br>');
            document.getElementById('emailModal').style.display = 'block';
            
            document.getElementById('sendEmailBtn').onclick = function() {
                window.location.href = data.mailto;
            };
        });
}

// Close modal when clicking X or outside
document.querySelector('.close').onclick = function() {
    document.getElementById('emailModal').style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == document.getElementById('emailModal')) {
        document.getElementById('emailModal').style.display = 'none';
    }
}