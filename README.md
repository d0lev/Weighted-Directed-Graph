[![neural-network-shutterstock.jpg](https://i.postimg.cc/fLzS3WMr/neural-network-shutterstock.jpg)](https://postimg.cc/1gd32QnG)

 
<h2>Weighted Directed Graph</h2>
<p>Project as part of the object-oriented course.</p>
<p>The above project deals with the construction of the data structure - an Directed and Weighted graph, using other data structures.</p>
<p><strong>In this project you can find algorithms that deal with solving various problems:</strong></p>
<ol>
<li>The shortest path between two nodes</li>
<li>Finding the Connected components</li>
<li>Deserialization and Serialization</li>
</ol>

<p>&nbsp;</p>
<p>The classes of the project :</p>
<ol>
<li><strong>DiGraph</strong> which extends the abstract class : <strong>GraphInterface</strong></li>

</ol>
<figure><table>
<thead>
<tr><th>Data members:</th><th>Description</th></tr></thead>
<tbody><tr><td>vertices</td><td>representing by Dictionary</td></tr><tr><td>adjacency</td><td>representing by Dictionary</td></tr><tr><td>edges</td><td>representing the edges of the graph -  list of tuples (source,destination,weight)</td></tr><tr><td>v</td><td>representing the number of nodes</td></tr><tr><td>e</td><td>representing the number of edges</td></tr><tr><td>mc</td><td>representing number of operations performed in the graph</td></tr></tbody>
</table></figure>
<figure><table>
<thead>
<tr><th>Methods:</th><th>Description</th></tr></thead>
<tbody><tr><td>add_node</td><td>adding a node in the graph</td></tr><tr><td>get_node</td><td>return the node that associated with the initial key</td></tr><tr><td>add_edge</td><td>adding an edge between two nodes that associated with the initial keys</td></tr><tr><td>getEdge</td><td>return the weight of the edge that associated with the initial keys</td></tr><tr><td>getEdge</td><td>return the weight of the edge that associated with the initial keys</td></tr><tr><td>all_in_edges_of_node</td><td>return a dictionary that represents all the nodes that  pointing of the initial key</td></tr><tr><td>all_out_edges_of_node</td><td>return a dictionary that represents all the nodes that  pointed by the initial key</td></tr><tr><td>remove_edge</td><td>remove the edge between two nodes in the graph</td></tr><tr><td>removeNode</td><td>remove a node from the graph</td></tr><tr><td>graph_transpose</td><td>return the directed weighted graph transpose</td></tr></tbody>
</table></figure>
<p>1.2 <strong>DiNode</strong>  </p>
<figure><table>
<thead>
<tr><th>Data members</th><th>Description</th></tr></thead>
<tbody><tr><td>key</td><td>represent the key of each node</td></tr><tr><td>position</td><td>represent the location of the node (tuple (x,y,z))</td></tr><tr><td>info</td><td>represent the info of each node</td></tr><tr><td>weight</td><td>represent the weight of each node</td></tr></tbody>
</table></figure>
<figure><table>
<thead>
<tr><th>Methods:</th><th>Description</th></tr></thead>
<tbody><tr><td>getKey</td><td>return the key of the node</td></tr><tr><td>getInfo</td><td>return the info of the node</td></tr><tr><td>setInfo</td><td>set the info of the node</td></tr><tr><td>getWeight</td><td>return the weight of the node</td></tr><tr><td>setWeight</td><td>set the weight of the node</td></tr><tr><td>getPosition</td><td>get the position of the node (tuple)</td></tr><tr><td>setPosition</td><td>set the position of the node (tuple)</td></tr></tbody>
</table></figure>
<p>2 .<strong>GraphAlgo</strong> which extends the abstract class : <strong>GraphInterface</strong></p>
<figure><table>
<thead>
<tr><th>Data members</th><th>Description</th></tr></thead>
<tbody><tr><td>graph</td><td>an object (DiGraph) that represents a graph</td></tr></tbody>
</table></figure>
<figure><table>
<thead>
<tr><th>Methods:</th><th>Description</th></tr></thead>
<tbody><tr><td>get_graph</td><td>return a graph object</td></tr><tr><td>shortest_path</td><td>return tuple of two objects (length of the path, list of nodes that are in the path)</td></tr><tr><td>connected_component</td><td>return a list that represent the strongly component that associated with the initial key</td></tr><tr><td>connected_components</td><td>return a list of lists that representing the strongly components in the graph</td></tr><tr><td>plot_graph</td><td>making a graphic user interface by using the library mathplotlib</td></tr><tr><td>save_to_json</td><td>graph object serialization</td></tr><tr><td>load_from_json</td><td>graph object deserialization</td></tr></tbody>
</table></figure>
<p>&nbsp;</p>
<h2><u>Visualization of given graphs</u></h2>
<a href="https://ibb.co/Cw5QbzX"><img src="https://i.ibb.co/rQGHxmL/image-20210111170240724.png" alt="image-20210111170240724" border="0"></a>
<h2>Visualization of random graphs</h2>
<a href="https://ibb.co/crmBR4L"><img src="https://i.ibb.co/BC1pv0N/image-20210111170633382.png" alt="image-20210111170633382" border="0"></a><p>&nbsp;</p>

Clone our project:
`$ git clone https://github.com/d0lev/Weighted-Directed-Graph.git`

<a href="https://github.com/d0lev/Weighted-Directed-Graph/wiki" title="Wiki"><img src="https://t3.ftcdn.net/jpg/00/37/56/34/240_F_37563459_R1WRmGUm1zvlRpxloYYV9D01BQtOGiPX.jpg" alt="wiki" width="100px" height="30px"></a>
