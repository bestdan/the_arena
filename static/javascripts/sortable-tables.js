/**
 * Interactive Table Enhancement for MkDocs Material
 * Adds filtering, sorting, and search to tables with class "favor-table"
 */

document.addEventListener('DOMContentLoaded', function() {
  // Find tables in the crowds_favor page or snak_shop pages
  if (window.location.pathname.includes('crowds_favor') || window.location.pathname.includes('snak_shop')) {
    const tables = document.querySelectorAll('.md-content table');
    tables.forEach(table => {
      // Add the favor-table class
      table.classList.add('favor-table');

      // Determine if this is a shop table or favor table
      const isShopTable = window.location.pathname.includes('snak_shop');
      enhanceTable(table, isShopTable);
    });
  }
});

function enhanceTable(table, isShopTable = false) {
  const wrapper = document.createElement('div');
  wrapper.className = 'favor-table-wrapper';
  table.parentNode.insertBefore(wrapper, table);
  wrapper.appendChild(table);

  const controls = document.createElement('div');
  controls.className = 'favor-table-controls';

  if (isShopTable) {
    // Shop-specific filters
    controls.innerHTML = `
      <div class="filter-row">
        <input type="text" id="favor-search" placeholder="🔍 Search items..." class="favor-search">
        <select id="cost-filter" class="favor-filter">
          <option value="">All Prices</option>
          <option value="5">5 GP</option>
          <option value="10">10 GP</option>
          <option value="15">15 GP</option>
          <option value="20">20 GP</option>
          <option value="25">25 GP</option>
          <option value="30">30 GP</option>
          <option value="40">40 GP</option>
          <option value="50">50 GP</option>
          <option value="60">60 GP</option>
          <option value="80">80 GP</option>
          <option value="90">90 GP</option>
          <option value="100">100 GP</option>
          <option value="120">120 GP</option>
          <option value="130">130 GP</option>
          <option value="150">150 GP</option>
          <option value="180">180 GP</option>
          <option value="200">200 GP</option>
        </select>
        <select id="category-filter" class="favor-filter">
          <option value="">All Categories</option>
          <option value="consumable">Consumable</option>
          <option value="equipment">Equipment</option>
          <option value="magic">Magic</option>
          <option value="service">Service</option>
        </select>
        <select id="action-filter" class="favor-filter">
          <option value="">All Actions</option>
          <option value="action">Action</option>
          <option value="worn">Worn</option>
          <option value="pre-match">Pre-Match</option>
        </select>
        <button id="clear-filters" class="clear-btn">Clear</button>
      </div>
      <div class="results-info">
        <span id="results-count"></span>
      </div>
    `;
  } else {
    // Favor-specific filters
    controls.innerHTML = `
      <div class="filter-row">
        <input type="text" id="favor-search" placeholder="🔍 Search abilities..." class="favor-search">
        <select id="cost-filter" class="favor-filter">
          <option value="">All Costs</option>
          <option value="1">Cost 1</option>
          <option value="2">Cost 2</option>
          <option value="3">Cost 3</option>
          <option value="5">Cost 5</option>
          <option value="6">Cost 6</option>
        </select>
        <select id="category-filter" class="favor-filter">
          <option value="">All Categories</option>
          <option value="offense">Offense</option>
          <option value="defense">Defense</option>
          <option value="mobility">Mobility</option>
          <option value="control">Control</option>
          <option value="support">Support</option>
          <option value="stealth">Stealth</option>
          <option value="signature">Signature</option>
        </select>
        <select id="action-filter" class="favor-filter">
          <option value="">All Actions</option>
          <option value="free">Free</option>
          <option value="bonus">Bonus</option>
          <option value="reaction">Reaction</option>
          <option value="declared">Declared</option>
        </select>
        <button id="clear-filters" class="clear-btn">Clear</button>
      </div>
      <div class="results-info">
        <span id="results-count"></span>
      </div>
    `;
  }
  wrapper.insertBefore(controls, table);

  const headers = table.querySelectorAll('thead th');
  headers.forEach((header, index) => {
    header.style.cursor = 'pointer';
    header.classList.add('sortable');
    header.setAttribute('data-sort-direction', 'none');
    header.innerHTML += ' <span class="sort-arrow">⇅</span>';
    header.addEventListener('click', () => sortTable(table, index, header));
  });

  const searchInput = document.getElementById('favor-search');
  const costFilter = document.getElementById('cost-filter');
  const categoryFilter = document.getElementById('category-filter');
  const actionFilter = document.getElementById('action-filter');
  const clearBtn = document.getElementById('clear-filters');

  function applyFilters() {
    const searchTerm = searchInput.value.toLowerCase();
    const costValue = costFilter.value.toLowerCase();
    const categoryValue = categoryFilter.value.toLowerCase();
    const actionValue = actionFilter.value.toLowerCase();
    const rows = table.querySelectorAll('tbody tr');
    let visibleCount = 0;

    rows.forEach(row => {
      const cells = row.querySelectorAll('td');
      const cost = cells[0].textContent.toLowerCase();
      const name = cells[1].textContent.toLowerCase();
      const category = cells[2].textContent.toLowerCase();
      const action = cells[3].textContent.toLowerCase();
      const effect = cells[4].textContent.toLowerCase();
      const pitch = cells[5] ? cells[5].textContent.toLowerCase() : '';

      const matchesSearch = searchTerm === '' || name.includes(searchTerm) || effect.includes(searchTerm) || category.includes(searchTerm) || pitch.includes(searchTerm);
      const matchesCost = costValue === '' || cost === costValue;
      const matchesCategory = categoryValue === '' || category === categoryValue;
      const matchesAction = actionValue === '' || action === actionValue;

      if (matchesSearch && matchesCost && matchesCategory && matchesAction) {
        row.style.display = '';
        visibleCount++;
      } else {
        row.style.display = 'none';
      }
    });

    const itemType = isShopTable ? 'items' : 'abilities';
    document.getElementById('results-count').textContent = `Showing ${visibleCount} of ${rows.length} ${itemType}`;
  }

  searchInput.addEventListener('input', applyFilters);
  costFilter.addEventListener('change', applyFilters);
  categoryFilter.addEventListener('change', applyFilters);
  actionFilter.addEventListener('change', applyFilters);
  clearBtn.addEventListener('click', () => {
    searchInput.value = '';
    costFilter.value = '';
    categoryFilter.value = '';
    actionFilter.value = '';
    applyFilters();
  });

  applyFilters();
}

function sortTable(table, columnIndex, header) {
  const tbody = table.querySelector('tbody');
  const rows = Array.from(tbody.querySelectorAll('tr'));
  const currentDirection = header.getAttribute('data-sort-direction');

  table.querySelectorAll('th').forEach(th => {
    if (th !== header) {
      th.setAttribute('data-sort-direction', 'none');
      th.querySelector('.sort-arrow').textContent = '⇅';
    }
  });

  let newDirection;
  if (currentDirection === 'none' || currentDirection === 'desc') {
    newDirection = 'asc';
    header.querySelector('.sort-arrow').textContent = '↑';
  } else {
    newDirection = 'desc';
    header.querySelector('.sort-arrow').textContent = '↓';
  }
  header.setAttribute('data-sort-direction', newDirection);

  rows.sort((a, b) => {
    const aValue = a.querySelectorAll('td')[columnIndex].textContent.trim();
    const bValue = b.querySelectorAll('td')[columnIndex].textContent.trim();
    const aNum = parseFloat(aValue);
    const bNum = parseFloat(bValue);

    if (!isNaN(aNum) && !isNaN(bNum)) {
      return newDirection === 'asc' ? aNum - bNum : bNum - aNum;
    }

    const comparison = aValue.localeCompare(bValue);
    return newDirection === 'asc' ? comparison : -comparison;
  });

  rows.forEach(row => tbody.appendChild(row));
}
