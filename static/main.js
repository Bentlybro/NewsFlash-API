
// Frontend JavaScript for handling API interactions
async function fetchNews() {
    try {
        const response = await fetch('/api/news/');
        const news = await response.json();
        displayNews(news);
    } catch (error) {
        console.error('Error fetching news:', error);
    }
}

function displayNews(news) {
    // Display news posts logic
}

// Initialize the page
document.addEventListener('DOMContentLoaded', fetchNews);