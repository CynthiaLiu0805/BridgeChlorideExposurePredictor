// Get the form element
// const form = document.getElementById('search-form');
// import { isWithinOntario } from 'input_check.js';

window.onload = function(){ 
    var submitButton = document.getElementById("btnsubmit");

    submitButton.onclick = async function submit() {
        var lat = document.getElementById('latitude').value;
        var lon = document.getElementById('longitude').value;

        // alert("11" + "\n" + lat + "\n" + long) 
        
    
        try {
                // Create an instance of InputCheck
                const inputCheck = new InputCheck(lon, lat);
                // await inputCheck.loadBoundary();
                if (inputCheck.isWithinOntario()) {
                    console.log("The point is within Ontario.");
                } else {
                    console.log("The point is outside Ontario.");
                }

                // const verification = new InputCheck(lon, lat);
                // fetch('ontario_boundary.geojson')
                // .then(response => response.json())
                // .then(data => {
                // if (isWithinOntario(lat, lon, data)) {

                //     // do the search


                //     console.log("The point is within the province.");
                // } else {
                //     console.log("The point is outside the province.");
                // }
                // })
                // .catch(error => console.error('Error fetching GeoJSON data:', error));
        
                // Check if the coordinates are within Ontario
                // if (verification.isWithinOntario()) {
                //     alert("is with in ontario")

                //     // // Create an instance of Search
                //     // const result = new Search(lon, lat);
                //     // // Perform the search and return the result
                //     // return result.searchCoordinates();

                // } else {
                //     // Throw an InputOutofOntarioError if coordinates are not within Ontario
                //     throw new InputOutofOntarioError('Coordinates are outside of Ontario.');
                // }
            } catch (error) {
                // Handle the error
                if (error instanceof InputOutofOntarioError) {
                    console.error(error.message);
                } else {
                    console.error('An unexpected error occurred:', error.message);
                }
            }
    }



}





// function inputchecking(val){
//     console.log(val);
//   }
// Add an event listener for the form submission
// form.addEventListener('submit', function(event) {

    // Prevent the default form submission behavior
    // event.preventDefault();
    // console.log(`Latitude: ${latitude}`);
    // console.log(`Longitude: ${longitude}`);

    // // Get the latitude and longitude values from the form inputs
    // const lat = document.getElementById('latitude').value;
    // const long = document.getElementById('longitude').value;

//     try {
//         // Create an instance of InputCheck
//         const verification = new InputCheck(long, lat);

//         // Check if the coordinates are within Ontario
//         if (verification.isWithinOntario()) {
//             console.log("is with in ontario")
//             // // Create an instance of Search
//             // const result = new Search(lon, lat);
//             // // Perform the search and return the result
//             // return result.searchCoordinates();
//         } else {
//             // Throw an InputOutofOntarioError if coordinates are not within Ontario
//             throw new InputOutofOntarioError('Coordinates are outside of Ontario.');
//         }
//     } catch (error) {
//         // Handle the error
//         if (error instanceof InputOutofOntarioError) {
//             console.error(error.message);
//         } else {
//             console.error('An unexpected error occurred:', error.message);
//         }
//     }

//     // Log the values to the console (you can perform other actions here)
    
    
// }


// Example usage
// const lon = '-79.3832';
// const lat = '43.6532';
// console.log(performSearch(lon, lat));  // Output: Searching for coordinates: Latitude 43.6532, Longitude -79.3832
