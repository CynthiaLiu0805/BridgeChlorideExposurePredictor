const path = require('path');

module.exports = {
  preset: '@vue/cli-plugin-unit-jest',

  moduleFileExtensions: ['js', 'json', 'vue'], // Include Vue files

  testEnvironment: 'jsdom',
  transform: {
    '^.+\\.js$': 'babel-jest',
  },
  transformIgnorePatterns: [
    '/node_modules/(?!(point-in-polygon-hao|robust-predicates)/)',
  ],
  moduleNameMapper: {
    '\\.(css|scss|sass)$': 'identity-obj-proxy', // Mock CSS imports
    '^@/(.*)$': '<rootDir>/src/$1', // Map @ to src folder

  },
};
