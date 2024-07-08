// import { createRequire } from 'module';
// const require = createRequire(import.meta.url);

// const fs = require('fs');
// const turf = require('@turf/turf');

class InputCheck {
    constructor(lon, lat) {
        this.fileName = 'ontario_boundary.geojson'; // this file is in root dir
        this.lon = lon;
        this.lat = lat;
        // this.boundary = null;
    }

    async loadGeoJSON() {
        return new Promise((resolve, reject) => {
            fs.readFile(this.fileName, 'utf8', (err, data) => {
                if (err) {
                    reject(err);
                } else {
                    resolve(JSON.parse(data));
                }
            });
        });
    }

    async isWithinOntario() {
        try {
            const ontarioBoundary = await this.loadGeoJSON();
            const point = turf.point([this.lon, this.lat]);
            const polygon = turf.multiPolygon(ontarioBoundary.features[0].geometry.coordinates);
            return turf.booleanPointInPolygon(point, polygon);
        } catch (error) {
            console.error('Error checking point in polygon:', error);
            return false;
        }
    }
    
    // async loadBoundary() {
    //     try {
    //         const response = await fetch(this.fileName);
    //         if (!response.ok) {
    //             throw new Error('Network response was not ok');
    //         }
            
    //         this.boundary = await response.json();
    //         console.log("111");
    //     } catch (error) {
    //         console.error('Error fetching GeoJSON data:', error);
    //     }
    // }

    // isWithinOntario() {
    //     try {
    //         const response =  fetch(this.fileName);
    //         if (!response.ok) {
    //             throw new Error('Network response was not ok');
    //         }
            
    //         this.boundary =  response.json();
    //         console.log("111");
    //     } catch (error) {
    //         console.error('Error fetching GeoJSON data:', error);
    //     }
    //     if (!this.boundary) {
    //         console.error('Boundary data is not loaded.');
    //         return false;
    //     }
    //     const point = turf.point([this.lon, this.lat]);
    //     const polygon = turf.polygon(this.boundary.features[0].geometry.coordinates);
    //     return turf.booleanPointInPolygon(point, polygon);
    // }
}

// export default InputCheck;

// fetch('ontario_boundary.geojson')
//     .then(response => response.json())
//     .then(data => {
//     if (isWithinOntario(lat, lon, data)) {

//         // do the search


//         console.log("The point is within the province.");
//     } else {
//         console.log("The point is outside the province.");
//     }
//     })
//     .catch(error => console.error('Error fetching GeoJSON data:', error));
        

//     // Load the GeoJSON file
//     loadFile() {
//         try {
//             const data = fs.readFileSync(this.fileName, 'utf8');
//             this.boundary = JSON.parse(data);
//         } catch (e) {
//             throw new Error(`FileNotFoundError: ${e.message}`);
//         }
//     }
// function isWithinOntario(lat, lon, provinceGeoJSON) {
//     const point = turf.point([lon, lat]);
//     const polygon = turf.polygon(provinceGeoJSON.features[0].geometry.coordinates);
//     return turf.booleanPointInPolygon(point, polygon);
// }

  // Example usage
//   const lat = 49.2827; // Latitude of Vancouver
//   const lon = -123.1207; // Longitude of Vancouver


    // Convert the longitude to float, and make it negative if needed
    // convertLongitude() {
    //     try {
    //         const longitude = parseFloat(this.lon);
    //         if (isNaN(longitude)) {
    //             throw new Error('InputTypeMismatchError: Invalid longitude');
    //         }
    //         return longitude > 0 ? longitude - 360 : longitude;
    //     } catch (e) {
    //         throw new Error(`InputTypeMismatchError: ${e.message}`);
    //     }
    // }

    // Convert the latitude to float
    // convertLatitude() {
    //     try {
    //         const latitude = parseFloat(this.lat);
    //         if (isNaN(latitude)) {
    //             throw new Error('InputTypeMismatchError: Invalid latitude');
    //         }
    //         return latitude;
    //     } catch (e) {
    //         throw new Error(`InputTypeMismatchError: ${e.message}`);
    //     }
    // }

    // Check if the input is inside Ontario
//     isWithinOntario() {
//         try {
//             this.loadFile();

//             const longitude = this.convertLongitude();
//             const latitude = this.convertLatitude();

//             // Create a Turf.js point for the coordinate
//             const point = turf.point([longitude, latitude]);

//             // Iterate through each polygon in the boundary and check if the point is within it
//             for (const feature of this.boundary.features) {
//                 if (turf.booleanPointInPolygon(point, feature)) {
//                     return true;
//                 }
//             }
//             return false;
//         } catch (e) {
//             throw e;
//         }
//     }
// }

// // Example usage:
// const checker = new InputCheck('-79.07264', '43.26259');
// console.log(checker.isWithinOntario()); // Output: true or false based on the point
