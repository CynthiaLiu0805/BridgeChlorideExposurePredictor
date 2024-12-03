import Papa from 'papaparse';

/**
 * Determine the file path based on the data and rate options.
 * @param {string} dataOption - The selected data option.
 * @param {string} rateOption - The selected rate option.
 * @returns {string} - The file path for the selected data.
 */
export function determineFilePath(dataOption, rateOption) {
  if (dataOption === 'deck') {
    return '/deck.csv';
  } else if (dataOption === 'pier') {
    return rateOption === 'high' ? '/pier_high.csv' : '/pier_low.csv';
  } else {
    throw new Error(`Unknown data option: ${dataOption}`);
  }
}

/**
 * Find the closest data point based on latitude and longitude.
 * @param {Array} data - Parsed CSV data.
 * @param {number} latitude - Latitude of the target location.
 * @param {number} longitude - Longitude of the target location.
 * @returns {number} - The index of the closest data point.
 */
export function findClosestDataPoint(data, latitude, longitude) {
  const normalizedLon = longitude < 0 ? longitude + 360 : longitude;

  const distances = data.slice(1).map((row) => {
    const latDiff = parseFloat(row[1]) - latitude;
    const lonDiff = parseFloat(row[0]) - normalizedLon;
    return Math.sqrt(latDiff ** 2 + lonDiff ** 2);
  });

  const closestIndex = distances.indexOf(Math.min(...distances.filter((d) => !isNaN(d))));
  return closestIndex;
}

/**
 * Parse the CSV file and find the closest data point's result.
 * @param {string} filePath - The path to the CSV file.
 * @param {number} latitude - Latitude of the target location.
 * @param {number} longitude - Longitude of the target location.
 * @param {Function} onComplete - Callback to execute with parsed data.
 * @param {Function} onError - Callback to execute in case of an error.
 */
export function parseCSVAndFindData(filePath, latitude, longitude, onComplete, onError) {
  Papa.parse(filePath, {
    download: true,
    complete: (results) => {
      const years = results.data[0].slice(2);
      const closestIndex = findClosestDataPoint(results.data, latitude, longitude);
      const resultRow = results.data[closestIndex + 1]; // Account for header row

      const result = years.reduce((acc, year, index) => {
        acc[year] = resultRow[index + 2]; // Skip lat/lon columns
        return acc;
      }, {});

      onComplete(result);
    },
    error: (error) => {
      onError(error);
    },
  });
}
