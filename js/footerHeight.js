// Select the specific element
const element = document.querySelector(".forheight");

// Check if the element exists
if (element) {
    // Get the vertical distance from the top of the document to the element
    const distanceFromTop = element.offsetTop;

    // Log the distance to the console
    console.log("Distance from top of the document:", distanceFromTop, "px");
} else {
    console.error("Element not found.");
}

const footer = document.querySelector(".footer-home");
console.log(footer);

if (footer) { // Check if footer is found
    if (viewportHeight > 100) {
        let finalHeight = (viewportHeight - 100) / viewportHeight * 100; // Calculation to convert to 'vh'
        
        // Apply styles correctly
        footer.style.position = 'absolute'; // Set position to absolute
        footer.style.top = `${viewportHeight}vh`; // Set the top position using vh
    } else {
        // Optional: Reset styles if the condition is not met
        footer.style.position = '';
        footer.style.top = '';
    }
} else {
    console.error("Footer element not found.");
}
