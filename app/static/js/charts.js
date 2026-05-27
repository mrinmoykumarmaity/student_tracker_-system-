// Chart.js configurations and functions

// Get theme-aware colors
function getChartColors() {
    const isDark = document.body.classList.contains('dark-mode');
    
    return {
        primary: '#6366f1',
        secondary: '#8b5cf6',
        success: '#10b981',
        warning: '#f59e0b',
        danger: '#ef4444',
        text: isDark ? '#f9fafb' : '#111827',
        grid: isDark ? '#374151' : '#e5e7eb',
        background: isDark ? 'rgba(99, 102, 241, 0.1)' : 'rgba(99, 102, 241, 0.1)'
    };
}

// Default chart options
function getDefaultOptions() {
    const colors = getChartColors();
    
    return {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: {
                labels: {
                    color: colors.text,
                    font: {
                        size: 12
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    color: colors.text
                },
                grid: {
                    color: colors.grid
                }
            },
            x: {
                ticks: {
                    color: colors.text
                },
                grid: {
                    color: colors.grid
                }
            }
        }
    };
}

// Update daily trend chart
function updateDailyChart(data) {
    const ctx = document.getElementById('dailyTrendChart');
    if (!ctx) return;
    
    const colors = getChartColors();
    
    if (window.dailyChart) {
        window.dailyChart.destroy();
    }
    
    window.dailyChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(d => {
                const date = new Date(d.date);
                return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
            }),
            datasets: [{
                label: 'Study Hours',
                data: data.map(d => d.hours),
                borderColor: colors.primary,
                backgroundColor: colors.background,
                tension: 0.4,
                fill: true
            }]
        },
        options: getDefaultOptions()
    });
}

// Update subject distribution chart
function updateSubjectChart(data) {
    const ctx = document.getElementById('subjectChart');
    if (!ctx) return;
    
    const colors = getChartColors();
    const chartColors = [
        colors.primary,
        colors.secondary,
        colors.success,
        colors.warning,
        colors.danger,
        '#ec4899',
        '#14b8a6',
        '#f97316'
    ];
    
    if (window.subjectChart) {
        window.subjectChart.destroy();
    }
    
    window.subjectChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.map(d => d.subject),
            datasets: [{
                data: data.map(d => d.hours),
                backgroundColor: chartColors.slice(0, data.length),
                borderWidth: 2,
                borderColor: document.body.classList.contains('dark-mode') ? '#1f2937' : '#ffffff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: colors.text,
                        padding: 15,
                        font: {
                            size: 12
                        }
                    }
                }
            }
        }
    });
}

// Update weekly trend chart
function updateWeeklyChart(data) {
    const ctx = document.getElementById('weeklyTrendChart');
    if (!ctx) return;
    
    const colors = getChartColors();
    
    if (window.weeklyChart) {
        window.weeklyChart.destroy();
    }
    
    window.weeklyChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.map(d => {
                const date = new Date(d.week);
                return 'Week of ' + date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
            }),
            datasets: [{
                label: 'Study Hours',
                data: data.map(d => d.hours),
                backgroundColor: colors.primary,
                borderRadius: 8
            }]
        },
        options: getDefaultOptions()
    });
}

// Update daily pattern chart (for analytics page)
function updateDailyPatternChart(data) {
    const ctx = document.getElementById('dailyPatternChart');
    if (!ctx) return;
    
    const colors = getChartColors();
    
    if (window.dailyPatternChart) {
        window.dailyPatternChart.destroy();
    }
    
    window.dailyPatternChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.map(d => {
                const date = new Date(d.date);
                return date.toLocaleDateString('en-US', { weekday: 'short' });
            }),
            datasets: [{
                label: 'Hours',
                data: data.map(d => d.hours),
                backgroundColor: colors.success,
                borderRadius: 6
            }]
        },
        options: getDefaultOptions()
    });
}

// Update subject distribution chart (for analytics page)
function updateSubjectDistChart(data) {
    const ctx = document.getElementById('subjectDistChart');
    if (!ctx) return;
    
    const colors = getChartColors();
    const chartColors = [
        colors.primary,
        colors.secondary,
        colors.success,
        colors.warning,
        colors.danger,
        '#ec4899',
        '#14b8a6',
        '#f97316'
    ];
    
    if (window.subjectDistChart) {
        window.subjectDistChart.destroy();
    }
    
    window.subjectDistChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: data.map(d => d.subject),
            datasets: [{
                data: data.map(d => d.hours),
                backgroundColor: chartColors.slice(0, data.length),
                borderWidth: 2,
                borderColor: document.body.classList.contains('dark-mode') ? '#1f2937' : '#ffffff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'right',
                    labels: {
                        color: colors.text,
                        padding: 15,
                        font: {
                            size: 12
                        }
                    }
                }
            }
        }
    });
}

// Update all charts (called when theme changes)
function updateAllCharts() {
    // This function will be called from darkmode.js
    // It will refresh all existing charts with new theme colors
    
    if (window.dailyChart) {
        const data = window.dailyChart.data;
        updateDailyChart(data.labels.map((label, i) => ({
            date: label,
            hours: data.datasets[0].data[i]
        })));
    }
    
    if (window.subjectChart) {
        const data = window.subjectChart.data;
        updateSubjectChart(data.labels.map((label, i) => ({
            subject: label,
            hours: data.datasets[0].data[i]
        })));
    }
    
    if (window.weeklyChart) {
        const data = window.weeklyChart.data;
        updateWeeklyChart(data.labels.map((label, i) => ({
            week: label,
            hours: data.datasets[0].data[i]
        })));
    }
    
    if (window.dailyPatternChart) {
        const data = window.dailyPatternChart.data;
        updateDailyPatternChart(data.labels.map((label, i) => ({
            date: label,
            hours: data.datasets[0].data[i]
        })));
    }
    
    if (window.subjectDistChart) {
        const data = window.subjectDistChart.data;
        updateSubjectDistChart(data.labels.map((label, i) => ({
            subject: label,
            hours: data.datasets[0].data[i]
        })));
    }
}
