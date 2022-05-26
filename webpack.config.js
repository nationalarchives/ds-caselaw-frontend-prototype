const path = require('path');

module.exports = {
  mode: 'development',
  devtool: false,
  entry: {
    judgment_scripts: './app/static/scripts/src/judgment_scripts.js',
    application_scripts: './app/static/scripts/src/application_scripts.js'
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'app/static/scripts/dist'),
  },
  module: {
  rules: [
    {
      test: /\.m?js$/,
      exclude: /(node_modules|bower_components)/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env']
        }
      }
    }
  ]
}
};