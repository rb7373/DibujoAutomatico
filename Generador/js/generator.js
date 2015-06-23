var generator = (function () {

    function splitSVG(svg) {
        var result;
        svg = svg.replace(/\n/g, '');
        result = svg.split(';');
        return result;
    }

    function getPoints(svgCanvasString) {
        for (var i = 0, length = svgCanvasString.length; i < length; ++i) {

        }
    }

    var generator = {
        splitSVG: splitSVG
    };

    return generator;

})(window, document);

console.log(generator.splitSVG(data));
