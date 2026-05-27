// Dark mode functionality

const themeToggle = document.getElementById('themeToggle');
const body = document.body;

// Check for saved theme preference or default to light mode
const currentTheme = localStorage.getItem('theme') || 'light';

// Apply saved theme on page load
if (currentTheme === 'dark') {
    body.classList.add('dark-mode');
    updateThemeToggleIcon(true);
}

// Theme toggle event listener
if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        
        const isDark = body.classList.contains('dark-mode');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        
        updateThemeToggleIcon(isDark);
        
        // Update charts if they exist
        updateChartsTheme();
    });
}

// Update theme toggle icon and text
function updateThemeToggleIcon(isDark) {
    const icon = themeToggle.querySelector('i');
    const text = themeToggle.querySelector('span');
    
    if (isDark) {
        icon.className = 'fas fa-sun';
        text.textContent = 'Light Mode';
    } else {
        icon.className = 'fas fa-moon';
        text.textContent = 'Dark Mode';
    }
}

// Update charts theme when toggling
function updateChartsTheme() {
    // This will be called when theme changes
    // Charts will be updated in charts.js
    if (typeof updateAllCharts === 'function') {
        updateAllCharts();
    }
}

// Listen for system theme changes
if (window.matchMedia) {
    const darkModeQuery = window.matchMedia('(prefers-color-scheme: dark)');
    
    darkModeQuery.addEventListener('change', (e) => {
        // Only auto-switch if user hasn't manually set a preference
        if (!localStorage.getItem('theme')) {
            if (e.matches) {
                body.classList.add('dark-mode');
                updateThemeToggleIcon(true);
            } else {
                body.classList.remove('dark-mode');
                updateThemeToggleIcon(false);
            }
            updateChartsTheme();
        }
    });
}
