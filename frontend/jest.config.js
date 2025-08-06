export default {
  testEnvironment: "jsdom",
  preset: 'ts-jest',
  transform: {
    "^.+\\.(ts|tsx)$": "ts-jest",
  },
  moduleFileExtensions: ["ts", "tsx", "js"],
  setupFilesAfterEnv: ["<rootDir>/src/setupTests.ts"],
};
