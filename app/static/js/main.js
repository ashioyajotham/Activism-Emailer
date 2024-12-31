// DOM Elements
const searchInput = document.getElementById('campaign-search');
const filterSelect = document.getElementById('campaign-filter');
const campaignCards = document.querySelectorAll('.campaign-card');
const modal = document.getElementById('emailModal');
const closeBtn = document.querySelector('.close');

// Filter and Search Functionality
function filterCampaigns() {
    const searchTerm = searchInput?.value.toLowerCase() || '';
    const filterValue = filterSelect?.value || 'all';
    
    campaignCards.forEach(card => {
        const title = card.querySelector('h2').textContent.toLowerCase();
        const status = card.querySelector('.status-badge').textContent.toLowerCase();
        const matchesSearch = title.includes(searchTerm);
        const matchesFilter = filterValue === 'all' || status === filterValue;
        
        card.style.display = matchesSearch && matchesFilter ? 'block' : 'none';
        
        if (status === 'archived') {
            card.classList.add('archived');
        } else {
            card.classList.remove('archived');
        }
    });
}

// Email Preview and Send Functionality
function showEmailPreview(campaignId) {
    fetch(`/generate_email/${campaignId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('emailTo').textContent = data.recipients;
            document.getElementById('emailSubject').textContent = data.subject;
            document.getElementById('emailBody').innerHTML = data.body.replace(/\n/g, '<br>');
            
            const sendBtn = document.getElementById('sendEmailBtn');
            sendBtn.onclick = () => sendEmail(data.mailto);
            
            modal.style.display = 'block';
        })
        .catch(error => {
            console.error('Error loading email preview:', error);
            alert('Failed to load email preview. Please try again.');
        });
}

// Email Sending Function
function sendEmail(mailtoLink) {
    const mailtoAnchor = document.createElement('a');
    mailtoAnchor.href = mailtoLink;
    mailtoAnchor.style.display = 'none';
    document.body.appendChild(mailtoAnchor);
    mailtoAnchor.click();
    document.body.removeChild(mailtoAnchor);
    closeModal();
}

// Modal Controls
function closeModal() {
    modal.style.display = 'none';
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

window.addEventListener('click', (event) => {
    if (event.target === modal) {
        closeModal();
    }
});

// Copy Email Text Functionality
const copyEmailBtn = document.getElementById('copy-email');
if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', () => {
        const emailBody = document.querySelector('.email-content').innerText;
        navigator.clipboard.writeText(emailBody)
            .then(() => alert('Email text copied to clipboard!'))
            .catch(err => console.error('Failed to copy text:', err));
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', filterCampaigns);