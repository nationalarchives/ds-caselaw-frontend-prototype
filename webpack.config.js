const path = require('path');

module.exports = {
  mode: 'development',
  devtool: false,
  entry: './app/static/scripts/src/app.js',
  output: {
    filename: 'app.js',
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