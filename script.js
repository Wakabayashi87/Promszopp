const promos = [
  {shop:'Biedronka', product:'Pierś z kurczaka 1 kg', price:'9,99 zł', discount:'-33 %'},
  {shop:'Lidl', product:'Czekolada Milka 100 g', price:'2,99 zł', discount:'-40 %'},
  {shop:'Kaufland', product:'Jogurt naturalny 400 g', price:'1,69 zł', discount:'-32 %'},
  {shop:'Aldi', product:'Pomidory malinowe 500 g', price:'4,99 zł', discount:'-29 %'},
  {shop:'Netto', product:'Mleko UHT 1 l', price:'2,49 zł', discount:'-22 %'},
  {shop:'Dino', product:'Płatki owsiane 500 g', price:'2,99 zł', discount:'-30 %'},
  // … możesz dopisać resztę z Twojej tabelki
];

const grid = document.getElementById('promoGrid');
const search = document.getElementById('search');

function render(list){
  grid.innerHTML = '';
  list.forEach(p=>{
    grid.insertAdjacentHTML('beforeend', `
      <div class="col-12 col-sm-6 col-md-4">
        <div class="card card-promo">
          <div class="card-header d-flex justify-content-between">
            <span class="shop-badge ${p.shop.toLowerCase()}">${p.shop}</span>
            <span class="badge bg-danger">${p.discount}</span>
          </div>
          <div class="card-body">
            <h6 class="card-title">${p.product}</h6>
            <p class="fw-bold text-success">${p.price}</p>
          </div>
        </div>
      </div>
    `);
  });
}

render(promos);

search.addEventListener('input', ()=>{
  const v = search.value.toLowerCase();
  render(promos.filter(p=>p.product.toLowerCase().includes(v)));
});
