'use strict';

const gulp = require('gulp');
const { watch, parallel } = require('gulp');
const sass = require('gulp-sass');
const babel = require('gulp-babel');

function styles(cb) {
    gulp.src('./app/static/styles/src/*.scss')
        .pipe(sass({ outputStyle: 'compressed' }).on('error', sass.logError))
        .pipe(gulp.dest('./app/static/styles/dist/'))
    cb();
}

function scripts(cb) {
    gulp.src('./app/static/scripts/src/*.js')
        .pipe(babel({ presets: ['@babel/env'] }))
        .pipe(gulp.dest('./app/static/scripts/dist/'))
    cb();
}

exports.run = parallel(scripts, styles);

exports.default = function () {
    watch('./app/static/styles/src/*.scss', styles);
    watch('./app/static/scripts/src/*.js', scripts);
};
