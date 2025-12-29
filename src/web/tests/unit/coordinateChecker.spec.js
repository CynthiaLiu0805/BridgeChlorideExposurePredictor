jest.mock('@turf/turf', () => ({
  booleanPointInPolygon: jest.fn(() => true),
  point: jest.fn(),
  polygon: jest.fn(),
}));

jest.mock('@/assets/boundary.json', () => ({  type: 'FeatureCollection',
  features: [
    {
      type: 'Feature',
      geometry: {
        type: 'Polygon',
        coordinates: [
          [
            [-90, 40], // A simple polygon mock
            [-85, 40],
            [-85, 45],
            [-90, 45],
            [-90, 40],
          ],
        ],
      },
    },
  ],
}));

import { handleDataOptionChange, convertLongitude, convertLatitude } from '@/scripts/CoordinateChecker.js';

// coordinateChecker.spec.js

describe('coordinateChecker', () => {
  describe('convertLongitude', () => {
    it('should convert positive longitude correctly', () => {
      expect(convertLongitude(100)).toBe(-260);
    });

    it('should return the same negative longitude', () => {
      expect(convertLongitude(-45)).toBe(-45);
    });

    it('should handle non-numeric input and set error message', () => {
      const result = convertLongitude('abc');
      expect(result).toEqual({ errorMessage: 'InputTypeMismatchError: Invalid longitude' });
    });

    it('should handle empty input and set error message', () => {
      const result = convertLongitude('');
      expect(result).toEqual({ errorMessage: 'InputTypeMismatchError: Invalid longitude' });
    });

    it('should handle boundary case of 0', () => {
      expect(convertLongitude(0)).toBe(0);
    });
  });

  describe('convertLatitude', () => {
    it('should return valid latitude', () => {
      expect(convertLatitude(45)).toBe(45);
    });

    it('should handle non-numeric input and set error message', () => {
      const result = convertLatitude('xyz');
      expect(result).toEqual({ errorMessage: 'InputTypeMismatchError: Invalid latitude' });
    });

    it('should handle empty input and set error message', () => {
      const result = convertLatitude('');
      expect(result).toEqual({ errorMessage: 'InputTypeMismatchError: Invalid latitude' });
    });
  });

  describe('handleDataOptionChange', () => {
    it('should reset rateOption to high when not selecting pier', () => {
      const rateOption = handleDataOptionChange('deck', 'low');
      expect(rateOption).toBe('high');
    });

    it('should keep rateOption unchanged for pier', () => {
      const rateOption = handleDataOptionChange('pier', 'low');
      expect(rateOption).toBe('low');
    });
  });


});

