# Search Results

<div id="search-results-container">
  <div id="search-input-section" style="margin-bottom: 20px;">
    <input type="text" id="search-input" placeholder="Enter search term..." style="width: 100%; padding: 10px; font-size: 16px; border: 1px solid #ccc; border-radius: 4px;">
    <button id="search-button" style="padding: 10px 20px; margin-top: 10px; background-color: #623876; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px;">Search</button>
  </div>
  
  <div id="search-results" style="margin-top: 20px;">
    <p id="results-info" style="color: #666;">Enter a search term to get started.</p>
    <div id="results-list"></div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('search-input');
  const searchButton = document.getElementById('search-button');
  const resultsDiv = document.getElementById('results-list');
  const resultsInfo = document.getElementById('results-info');
  
  // Get search term from URL if present
  const urlParams = new URLSearchParams(window.location.search);
  const query = urlParams.get('q');
  
  if (query) {
    searchInput.value = query;
    performSearch(query);
  }
  
  searchButton.addEventListener('click', function() {
    const searchTerm = searchInput.value;
    if (searchTerm) {
      window.location.search = 'q=' + encodeURIComponent(searchTerm);
    }
  });
  
  searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      searchButton.click();
    }
  });
  
  function performSearch(searchTerm) {
    resultsDiv.innerHTML = '';
    
    if (!window.searchData) {
      resultsInfo.textContent = 'Search data not available yet. Please try again.';
      return;
    }
    
    const lowerSearchTerm = searchTerm.toLowerCase();
    const results = window.searchData.filter(item => {
      const title = (item.title || '').toLowerCase();
      const text = (item.text || '').toLowerCase();
      return title.includes(lowerSearchTerm) || text.includes(lowerSearchTerm);
    });
    
    if (results.length === 0) {
      resultsInfo.textContent = `No results found for "${searchTerm}".`;
    } else {
      resultsInfo.textContent = `Found ${results.length} result${results.length !== 1 ? 's' : ''} for "${searchTerm}".`;
      
      results.forEach(result => {
        const resultDiv = document.createElement('div');
        resultDiv.style.marginBottom = '20px';
        resultDiv.style.paddingBottom = '15px';
        resultDiv.style.borderBottom = '1px solid #eee';
        
        const link = document.createElement('a');
        link.href = result.location;
        link.textContent = result.title || 'Untitled';
        link.style.color = '#623876';
        link.style.fontSize = '18px';
        link.style.fontWeight = 'bold';
        link.style.textDecoration = 'none';
        link.style.display = 'block';
        link.style.marginBottom = '5px';
        
        link.addEventListener('mouseover', function() {
          link.style.textDecoration = 'underline';
        });
        link.addEventListener('mouseout', function() {
          link.style.textDecoration = 'none';
        });
        
        const text = document.createElement('p');
        let preview = result.text || '';
        const index = preview.toLowerCase().indexOf(lowerSearchTerm);
        if (index > -1) {
          const start = Math.max(0, index - 50);
          const end = Math.min(preview.length, index + lowerSearchTerm.length + 50);
          preview = (start > 0 ? '...' : '') + preview.substring(start, end) + (end < preview.length ? '...' : '');
        } else {
          preview = preview.substring(0, 150);
        }
        text.textContent = preview;
        text.style.color = '#666';
        text.style.fontSize = '14px';
        text.style.margin = '0';
        
        const path = document.createElement('p');
        path.textContent = result.location;
        path.style.color = '#999';
        path.style.fontSize = '12px';
        path.style.margin = '5px 0 0 0';
        
        resultDiv.appendChild(link);
        resultDiv.appendChild(text);
        resultDiv.appendChild(path);
        resultsDiv.appendChild(resultDiv);
      });
    }
  }
});
</script>

<style>
#search-input:focus {
  outline: none;
  border-color: #623876;
  box-shadow: 0 0 5px rgba(98, 56, 118, 0.3);
}

#search-button:hover {
  background-color: #917d9b;
}

#results-info {
  font-style: italic;
}
</style>
