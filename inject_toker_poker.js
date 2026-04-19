// Load Toker Poker products and inject them into the storefront
fetch('/toker_poker_products_final.json')
  .then(response => response.json())
  .then(products => {
    const container = document.getElementById('toker-poker-products');
    if (!container) {
      console.error('Toker Poker container not found');
      return;
    }
    
    container.innerHTML = '';
    
    products.forEach(product => {
      if (!product.available) return;
      
      const productCard = document.createElement('div');
      productCard.className = 'card';
      productCard.onclick = () => openModal(product.sku);
      productCard.setAttribute('data-search', `${product.title.toLowerCase()} ${product.description.toLowerCase()} toker poker`);
      productCard.setAttribute('data-name', product.title);
      productCard.setAttribute('data-brand', 'Toker Poker');
      productCard.setAttribute('data-cat', product.description);
      productCard.setAttribute('data-price', product.price);
      
      productCard.innerHTML = `
        <img src="${product.image}" alt="${product.title}" class="card-img" loading="lazy">
        <div class="card-body">
          <div class="card-brand">Toker Poker</div>
          <div class="card-title">${product.title}</div>
          <div class="card-price">$${product.price}</div>
        </div>
      `;
      
      container.appendChild(productCard);
    });
  })
  .catch(error => console.error('Error loading Toker Poker products:', error));

// Add a Toker Poker section to the storefront if it doesn't exist
if (!document.getElementById('toker-poker-products')) {
  const section = document.createElement('section');
  section.className = 'product-section';
  section.innerHTML = `
    <h2>Toker Poker Lighters</h2>
    <div class="grid" id="toker-poker-products"></div>
  `;
  
  // Append to the end of the body
  document.body.appendChild(section);
  
  // Load the products
  fetch('/toker_poker_products_final.json')
    .then(response => response.json())
    .then(products => {
      const container = document.getElementById('toker-poker-products');
      container.innerHTML = '';
      
      products.forEach(product => {
        if (!product.available) return;
        
        const productCard = document.createElement('div');
        productCard.className = 'card';
        productCard.onclick = () => openModal(product.sku);
        productCard.setAttribute('data-search', `${product.title.toLowerCase()} ${product.description.toLowerCase()} toker poker`);
        productCard.setAttribute('data-name', product.title);
        productCard.setAttribute('data-brand', 'Toker Poker');
        productCard.setAttribute('data-cat', product.description);
        productCard.setAttribute('data-price', product.price);
        
        productCard.innerHTML = `
          <img src="${product.image}" alt="${product.title}" class="card-img" loading="lazy">
          <div class="card-body">
            <div class="card-brand">Toker Poker</div>
            <div class="card-title">${product.title}</div>
            <div class="card-price">$${product.price}</div>
          </div>
        `;
        
        container.appendChild(productCard);
      });
    })
    .catch(error => console.error('Error loading Toker Poker products:', error));
}