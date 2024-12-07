
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', () => {
        const productName = button.getAttribute('data-product-name');
        const quantity = button.getAttribute('data-quantity');
        const price = button.getAttribute('data-price');

        fetch('/update_cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-csrftoken': getcsrftoken(), // Ensure CSRF token is included
            },
            body: JSON.stringify({
                product_name: productName,
                quantity: quantity,
                price: price
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert(data.message);
            } else {
                alert('Failed to add item to cart');
            }
        });
    });
});

function getcsrfoken() {
    return document.querySelector('meta[name="csrf-token"]').value;
}
