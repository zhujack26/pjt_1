const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      // url 리소스를 추가하기
      '/topics': {
        // 해당 리소스가 있는 url일 경우 타겟으로 baseURL을 변경
        "target": 'https://www.bbc.com/korean/',
        "pathRewrite":{'^/':''},
        // 기본 베이스 URL을 바꿔줄지 여부
        "changeOrigin":true,
        "secure":false
      },
    }
  }
})
