###  <area id="Node_1" shape="circle" coords="5,5,20" onclick="clickNode(this.id)">
###  <area id="Node_2" shape="circle" coords="5,595,20" onclick="clickNode(this.id)">
###  <area id="Node_3" shape="circle" coords="1095,5,20" onclick="clickNode(this.id)">
###  <area id="Node_4" shape="circle" coords="1095,595,20" onclick="clickNode(this.id)">

###  <area id="Node_up" shape="circle" coords="240,48,8" onclick="clickNode(this.id)">
###  <area id="Node_left" shape="circle" coords="18,318,8" onclick="clickNode(this.id)">
###  <area id="Node_right" shape="circle" coords="1087,282,8" onclick="clickNode(this.id)">
###  <area id="Node_bottom" shape="circle" coords="275,552,8" onclick="clickNode(this.id)">

def get_coordinate(a, b):
    x1 = -2743.7663122500826
    x2 = 3516.035275051505
    y1 = -1879.3702290076342
    y2 = 1085.6297709923658
    
    up = 48
    bottom = 552
    left = 18
    right = 1087
    
    x_bin = (right - left)/(x2 - x1)
    y_bin = (bottom - up)/(y2 - y1)
    
    a_ = (a - x1) * x_bin + left
    b_ = (b - y1) * y_bin + up
    
    return a_, b_

file = open("/Users/cxqiu/Downloads/Jax_website/data/nodes.txt")
key_id = ["key"]
celltype_name = ["Cell type name"]
celltype_group = ["Developmental subgroup"]
out = open("/Users/cxqiu/Downloads/Jax_website/data/nodes_coor.txt", "w")
for line in file:
    l = line.rstrip().split("\t")
    key_id.append(l[0])
    celltype_name.append(l[1])
    celltype_group.append(l[2])
    a_, b_ = get_coordinate(float(l[3]), float(l[4]))
    out.write('''<area id="%s" shape="circle" coords="%s,%s,8" onclick="clickNode(this.id)">'''%(l[0], str(a_), str(b_)) + "\n")
file.close()
out.close()


out = open("/Users/cxqiu/Downloads/Jax_website/NodeTable.tsv", "w")
out.write("\t".join(key_id) + '\n')
out.write("\t".join(celltype_name) + '\n')
out.write("\t".join(celltype_group) + '\n')
out.close()