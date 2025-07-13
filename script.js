let promos = [];

function initApp() {
  const shops = [...new Set(promos.map(p => p.shop))].sort();
  const promoGrid = document.getElementById('promoGrid');
  const shopNav   = document.getElementById('shopNav');
  const countSpan = document.getElementById('count');
  const todaySpan = document.getElementById('today');
  const lastUpdateSpan = document.getElementById('lastUpdate');

  todaySpan.textContent      = new Date().toLocaleDateString('pl-PL', {day:'numeric', month:'long', year:'numeric'});
  lastUpdateSpan.textContent = new Date().toLocaleString('pl-PL');

  shops.forEach(shop => {
    const btn = document.createElement('a');
    btn.className = 'btn btn-outline-light btn-sm';
    btn.href = `#${shop.toLowerCase()}`;
    btn.textContent = shop;
    shopNav.appendChild(btn);
  });
  const allBtn = document.createElement('a');
  allBtn.className = 'btn btn-outline-light btn-sm';
  allBtn.href = '#all';
  allBtn.textContent = 'Wszystkie';
  shopNav.appendChild(allBtn);

  function render() {
    const hash = location.hash.slice(1) || 'all';
    const list = hash === 'all' ? promos : promos.filter(p => p.shop.toLowerCase() === hash);
    promoGrid.innerHTML = '';
    list.forEach(p => {
      const card = document.createElement('div');
      card.className = 'col-6 col-md-4 col-lg-3';
      card.innerHTML = `
        <div class="card card-promo h-100 shadow-sm">
          <div class="card-body">
            <h6 class="card-title">${p.product}</h6>
            <p class="mb-1"><strong>${p.price.toFixed(2)} zł</strong></p>
            <span class="badge bg-danger">${p.discount}%</span>
            <span class="shop-badge ${p.shop.toLowerCase()} ms-1">${p.shop}</span>
          </div>
        </div>`;
      promoGrid.appendChild(card);
    });
    document.getElementById('count').textContent = list.length;
  }

  window.addEventListener('hashchange', render);
  render();
}

// ładujemy JSON z root repo
fetch('promos.json')
  .then(r => r.json())
  .then(data => { promos = data; initApp(); })
  .catch(() => { promos = []; initApp(); });
