import { determineFilePath, findClosestDataPoint, parseCSVAndFindData } from '@/scripts/DataSearching';

describe('DataSearching.js', () => {
  describe('determineFilePath', () => {
    it('should return the correct file path for the deck option', () => {
      expect(determineFilePath('deck', 'high')).toBe('/deck.csv');
    });

    it('should return the correct file path for pier with high rate option', () => {
      expect(determineFilePath('pier', 'high')).toBe('/pier_high.csv');
    });

    it('should return the correct file path for pier with low rate option', () => {
      expect(determineFilePath('pier', 'low')).toBe('/pier_low.csv');
    });

    it('should throw an error for an unknown data option', () => {
      expect(() => determineFilePath('unknown', 'high')).toThrowError('Unknown data option: unknown');
    });
  });

  describe('findClosestDataPoint', () => {
    const mockData = [
      ['Longitude', 'Latitude', 'Year1', 'Year2'],
      [10, 20, '2006', '2007'],
      [11, 21, '2006', '2007'],
      [12, 22, '2006', '2007'],
    ];

    it('should find the closest data point correctly', () => {
      const closestIndex = findClosestDataPoint(mockData, 20.4, 10.5);
      expect(closestIndex).toBe(0); // The closest point should be the second row
    });

    it('should normalize negative longitude and find the closest data point', () => {
      const closestIndex = findClosestDataPoint(mockData, 20.6, -349.5); // -349.5 is equivalent to 10.5
      expect(closestIndex).toBe(1);
    });

   
  });

  describe('parseCSVAndFindData', () => {
    let mockPapaParse;

    beforeAll(() => {
      // Mock Papa.parse
      mockPapaParse = jest.spyOn(require('papaparse'), 'parse');
    });

    afterAll(() => {
      jest.restoreAllMocks();
    });

    it('should parse CSV and call onComplete with results', (done) => {
      const mockCSVData = [
        ['Longitude', 'Latitude', 'Year1', 'Year2'],
        [10, 20, '2006', '2007'],
        [11, 21, '2006', '2007'],
      ];

      mockPapaParse.mockImplementation((filePath, options) => {
        options.complete({ data: mockCSVData });
      });

      const onComplete = jest.fn((result) => {
        expect(result).toEqual({
          Year1: '2006',
          Year2: '2007',
        });
        done();
      });

      const onError = jest.fn();

      parseCSVAndFindData('/deck.csv', 21, 11, onComplete, onError);
      expect(onError).not.toHaveBeenCalled();
    });

    it('should handle errors and call onError callback', (done) => {
      mockPapaParse.mockImplementation((filePath, options) => {
        options.error(new Error('Parsing error'));
      });

      const onComplete = jest.fn();
      const onError = jest.fn((error) => {
        expect(error.message).toBe('Parsing error');
        done();
      });

      parseCSVAndFindData('/deck.csv', 21, 11, onComplete, onError);
      expect(onComplete).not.toHaveBeenCalled();
    });
  });
});
