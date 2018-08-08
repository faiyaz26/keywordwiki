var frequency_list = [{"text":"study","size":40},{"text":"motion","size":15},
                      {"text":"forces","size":10},{"text":"electricity","size":15},
                      {"text":"movement","size":10},{"text":"relation","size":5},
                      {"text":"things","size":10},{"text":"force","size":5},
                      {"text":"ad","size":5},{"text":"energy","size":85},
                      {"text":"living","size":5},{"text":"nonliving","size":5},
                      {"text":"laws","size":15},{"text":"speed","size":45},
                      {"text":"velocity","size":30},{"text":"define","size":5},
                      {"text":"constraints","size":5},{"text":"universe","size":10},
                      {"text":"physics","size":120},{"text":"describing","size":5},
                      {"text":"matter","size":90},{"text":"physics-the","size":5},
                      {"text":"world","size":10},{"text":"works","size":10},
                      {"text":"science","size":70},
                      {"text":"interactions","size":30},{"text":"studies","size":5},
                      {"text":"properties","size":45},{"text":"nature","size":40},
                      {"text":"branch","size":30},{"text":"concerned","size":25},
                      {"text":"source","size":40},{"text":"google","size":10},
                      {"text":"defintions","size":5},{"text":"two","size":15},
                      {"text":"grouped","size":15},{"text":"traditional","size":15},
                      {"text":"fields","size":15},{"text":"acoustics","size":15},
                      {"text":"optics","size":15},{"text":"mechanics","size":20},
                      {"text":"thermodynamics","size":15},{"text":"electromagnetism","size":15},
                      {"text":"modern","size":15},{"text":"extensions","size":15},
                      {"text":"thefreedictionary","size":15},{"text":"interaction","size":15}];


function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}


var colorRange = ["#a7aae1", "#a7bae1", 
"#a7cae1", "#a7dae1", 
"#a7eae1", "#8486ea"];

var windowHeight = $(window).height();
var windowWidth  = $(window).width();
var color = d3.scale.linear()
        .domain([0,1,2,3,4,5,6,10,15,20,100])
        .range(colorRange);

d3.layout.cloud().size([800, 300])
        .words(frequency_list)
        .rotate(0)
        .fontSize(function(d) { return d.size; })
        .on("end", draw)
        .start();

function draw(words) {
    d3.select("#keywordCloud").append("svg")
            .attr("preserveAspectRatio", "xMinYMin meet")
            .attr("viewBox", "0 0 960 500")
            .attr("class", "wordcloud")
            .append("g")
            // without the transform, words words would get cutoff to the left and top, they would
            // appear outside of the SVG area
            .style('transform', 'translate(40%, 45%)')
            .selectAll("text")
            .data(words)
            .enter().append("text")
            .style("font-size", function(d) { return d.size + "px"; })
            .style("fill", function(d, i) {
                var pos = getRandomArbitrary(0, colorRange.length - 1);
                return color(pos); 
            })
            .attr("transform", function(d) {
                return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
            })
            .text(function(d) { return d.text; });
}