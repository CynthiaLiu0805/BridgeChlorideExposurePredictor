import * as turf from '@turf/turf';
import boundary from '@/assets/boundary.json';

/**
 * Converts a longitude value to a normalized format for use in spatial calculations.
 * 
 * @param {number|string} lon - The longitude to convert.
 * @returns {number|Object} A converted longitude value or an error object if the conversion fails.
 */
export function convertLongitude(lon) {
  try {
    const floatLon = parseFloat(lon);
    if (isNaN(floatLon)) {
      throw new Error('InputTypeMismatchError: Invalid longitude');
    }
    return floatLon > 0 ? floatLon - 360 : floatLon;
  } catch (error) {
    return { errorMessage: error.message };
  }
}


/**
 * Converts a latitude value to a normalized format for use in spatial calculations.
 * 
 * @param {number|string} lat - The latitude to convert.
 * @returns {number|Object} A converted latitude value or an error object if the conversion fails.
 */
export function convertLatitude(lat) {
  try {
    const floatLat = parseFloat(lat);
    if (isNaN(floatLat)) {
      throw new Error('InputTypeMismatchError: Invalid latitude');
    }
    return floatLat;
  } catch (error) {
    return { errorMessage: error.message };
  }
}


/**
 * Validates whether the provided latitude and longitude coordinates are within Ontario.
 * 
 * @param {number|string} latitude - Latitude to be checked.
 * @param {number|string} longitude - Longitude to be checked.
 * @returns {Object} An object containing:
 *   - `isWithinOntario`: Boolean indicating if the coordinates are within Ontario.
 *   - `errorMessage`: A string describing any error that occurred, or `null` if no error.
 */
export function checkCoordinate(latitude, longitude) {
  if (!boundary) {
    return {
      isWithinOntario: false,
      errorMessage: 'Ontario GeoJSON data is not loaded or is invalid.',
    };
  }

  const convertedLongitude = convertLongitude(longitude);
  const convertedLatitude = convertLatitude(latitude);

  if (convertedLongitude?.errorMessage || convertedLatitude?.errorMessage) {
    return {
      isWithinOntario: false,
      errorMessage:
        convertedLongitude?.errorMessage || convertedLatitude?.errorMessage,
    };
  }

  const point = turf.point([convertedLongitude, convertedLatitude]);
  const isWithinOntario = turf.booleanPointInPolygon(point, boundary);

  return {
    isWithinOntario,
    errorMessage: isWithinOntario
      ? null
      : 'The coordinate is not within Ontario.',
  };
}


/**
 * Handles changes to the data option selection and resets the rate option if necessary.
 * 
 * @param {string} selectedOption - The newly selected data option.
 * @param {string} rateOption - The current rate option, which may be reset.
 * @returns {string} The updated rate option.
 */
export function handleDataOptionChange(selectedOption, rateOption) {
  // Reset rate option when switching data options
  if (selectedOption !== 'pier') {
    rateOption = 'high'; // Reset to default for non-pier options
  }
  return rateOption;
}

