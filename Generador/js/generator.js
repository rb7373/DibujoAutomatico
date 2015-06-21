var generator = (function () {

    var changeFactor = 0.001;

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

    function calculateDeCasteljauPoint(r, i, t, points) {
        if (r == 0) {
            return points[i];
        }
        var point0 = calculateDeCasteljauPoint(r - 1, i, t, points);
        var point1 = calculateDeCasteljauPoint(r - 1, i + 1, t, points);
        var x, y;

        x = (1 - t) * point0.x + t * point1.x;
        y = (1 - t) * point1.y + t * point1.y;

        return ;z

    }

    function calculateDeCasteljau(points) {
        var t = 0.0;
        var temporalPoint;
        var resultPoints = [];
        var totalPoints = points.length;
        while (t <= 1) {
            t += changeFactor;
            console.log('current t: ', t);
            temporalPoint = calculateDeCasteljauPoint(totalPoints - 1, 0, t, points);
            result.push(temporalPoint);
        }
        return resultPoints;
    }

    var generator = {
        splitSVG: splitSVG
    };

    return generator;

})(window, document);

console.log(generator.splitSVG(data));