const path = require('path');

module.exports = {
    entry: './assets/js/main.js',
    output: {
        'path': path.resolve(__dirname, 'core', 'static', 'core'),
        'filename': 'bundle.js'
    },
    resolve: {
        extensions: ['.ts', '...']
    },
    module: {
        rules: [
            {
                test: /\.css/i,
                use: [
                    'style-loader',
                    'css-loader'
                ]
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)/i,
                type: 'asset/resource',
            },
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
            }
        ]
    }
}