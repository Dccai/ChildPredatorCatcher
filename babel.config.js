module.exports = function (api) {
  api.cache(true);
  return {
    presets: [],
    plugins: [
      "@babel/plugin-proposal-export-namespace-from",
      "react-native-reanimated/plugin",
      require.resolve("expo-router/babel"),
    ],
  };
};
