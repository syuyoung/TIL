// import
const path = require("path");
const HtmlPlugin = require("html-webpack-plugin");

// export
module.exports = {
  //파일을 읽어들이기 시작하는 진입점 설정
  entry: "./js/main.js",

  //결과물(번들)을 반환하는 설정
  output: {
    // path: path.resolve(__dirname, "dist"),
    // filename: "main.js",
    clean: true,
  },

  plugins: [
    new HtmlPlugin({
      template: "./index.html",
    }),
  ],

  devServer: {
    host: "localhost",
  },
};
