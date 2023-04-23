//Init NodeTable
d3.select("#NodeTable")
 .append("table")
// done

// To click a node
function clickNode(node_id) {

//  alert(node_id);

  // remove the original table/plots
  d3.select("#NodeTable")
      .select("table")
      .remove();
  // done

  // update the NodeTable
  d3.tsv("NodeTable.tsv", function(error, NodeData) {

      NodeArray = [];
      NodeData.forEach(function(d, i){// update the NodeTable
          NodeArray.push([d.key, d[node_id]]);
      });

      //alert(NodeArray[0][1]);

      //Add a new (updated) NodeTable
      d3.select("#NodeTable")
          .append("table")
          .attr("style", "font-size: 15px")
          .append("tbody")
          .selectAll("tr")
          .data(NodeArray)
          .enter()
          .append("tr")
          .selectAll("td")
          .data(function(d) {return d;})
          .enter()
          .append("td")
          .html(function(d) {return d;})
          .selectAll(".fake-link")
          .on("click", function(){
              var touch_id = d3.select(this).attr('id');
              clickNode(touch_id);
          });

  });
}
