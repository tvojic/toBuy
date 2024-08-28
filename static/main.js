function openAddProductPopup() {
    var popup = document.getElementById('addProductPopup');
    popup.classList.add('active');
}

// Function to close Add Product popup
function closeAddProductPopup() {
    var popup = document.getElementById('addProductPopup');
    popup.classList.remove('active');
}

// Function to validate Add Product form submission
function validateAddProductForm() {
    var popup = document.getElementById('addProductPopup');
    if (!popup.classList.contains('active')) {
        return false; // Prevent form submission
    }
    return true; // Allow form submission
}

// Function to open Remove Product popup
function openRemoveProductPopup() {
    var popup = document.getElementById('removeProductPopup');
    popup.classList.add('active');
}

// Function to close Remove Product popup
function closeRemoveProductPopup() {
    var popup = document.getElementById('removeProductPopup');
    popup.classList.remove('active');
}