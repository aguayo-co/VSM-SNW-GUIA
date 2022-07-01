const { resolve } = require('path');

module.exports = {
  plugins: [],
  root: resolve('./vsm_snw/static/'),
  base: '/static/',
  server: {
    host: 'localhost',
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  resolve: {
    extensions: ['.js', '.json'],
  },
  build: {
    outDir: resolve('./vsm_snw/static/'),
    assetsDir: '',
    manifest: true,
    rollupOptions: {
      input: {
        main: resolve('./vsm_snw/static/js/main.js'),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
};