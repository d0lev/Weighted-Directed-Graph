package api;

import com.google.gson.*;

import java.awt.*;
import java.io.*;
import java.util.*;
import java.util.List;

/**
 * This interface represents a Directed (positive) Weighted Graph Theory Algorithms including:<br>
 * 0. clone(); (copy)<br>
 * 1. init(graph);<br>
 * 2. isConnected(); // strongly (all ordered pais connected)<br>
 * 3. double shortestPathDist(int src, int dest);<br>
 * 4. List<node_data> shortestPath(int src, int dest);<br>
 * 5. Save(file); // JSON file<br>
 * 6. Load(file); // JSON file
 */
public class DWGraph_Algo implements dw_graph_algorithms {
    directed_weighted_graph graph;
    static HashSet<edge_data> paths = new HashSet<>(); // list that contains all the pairs
    static final int GRAY = Color.GRAY.getRGB();
    static final double EPSILON = 0.001;

    /**
     * Init the graph on which this set of algorithms operates on.
     * @param g - a directed_weighted_graph type.
     */
    @Override
    public void init(directed_weighted_graph g) {
        graph = g;
    }

    /**
     * @return the underlying graph of which this class works.
     */
    @Override
    public directed_weighted_graph getGraph() {
        return graph;
    }

    /**
     * Compute a deep copy of this weighted graph.
     * @return a deep-copied graph.
     */
    @Override
    public directed_weighted_graph copy() {
        if (graph.getV().size() != 0) {
            DWGraph_DS copied = new DWGraph_DS();
            for (node_data runner : graph.getV()) {
                copied.addNode(new Node(runner));
                for (edge_data edge : graph.getE(runner.getKey())) {
                    if (!copied.hasNode(edge.getDest())) {
                        copied.addNode(new Node(((Edge) edge).destination));
                    }
                    copied.connect(runner.getKey(), edge.getDest(), edge.getWeight());
                }
            }
            return copied;
        }
        return null;
    }

    /**
     * @note a graph is said to be <strong>strongly connected</strong> if every vertex is reachable<br>
             from every other vertex.
     * @note This method implements the <strong> Kosaraju algorithm</strong>.<br>
             The first DFS is to find all the vertices u that are reachable from vertex v.<br>
             The second DFS is to check the reverse, i.e if all u can reach v. <br>
             The reverse check on the second DFS is made
             by transposing the graph via graphTranspose() method which is explained in its info.<br>
             Instead of testing each vertex u ( which are reachable from v) and can reach v back,<br>
             the second DFS on the transpose equivalently tests, if v can reach all u.<br>
     * @return true if the graph is strongly-connected.
     */
    @Override
    public boolean isConnected() {
        if (graph.getV().size() > 1) {
            Reset();
            directed_weighted_graph graph_transpose = new DWGraph_DS();

            Stack<node_data> stack = new Stack<>();
            for(node_data node : graph.getV()){
                if(node.getTag() != GRAY) {
                    DFS(graph, node, stack);
                }
            }

            graphTranspose(graph_transpose);

            ArrayList< ArrayList<node_data> > components = new ArrayList<>();


            while (!stack.isEmpty()) {
                Node node = (Node) graph_transpose.getNode(stack.pop().getKey());
                if(node.getTag() != GRAY) {

                    ArrayList<node_data> component = new ArrayList<>();
                    DFSTransposed(graph_transpose, node,component);
                    components.add(component);
                }

            }
            System.out.println("size: " + components.size());
//            for (int i = 0 ; i < components.size() ; i++) {
//                ArrayList<node_data> list = components.get(i);
//                for (int j = 0 ; j < list.size() ; j++) {
//                    System.out.print(list.get(j).getKey() + ", ");
//                }
//                System.out.println();
//            }
            return true;
        }
        return true;
    }

    /**
     * @note This method implements the <strong>DFS algorithm</strong>.<br>
             This is a recursive method. The basic idea is as follows:<br>
             Pick a starting node (runner) and mark it as a visited node.<br>
             This will prevent you from visiting the same node more than once. <br>
             Iterate all its adjacent nodes, if the next node to visit isn't visited before, then check its adjacent nodes and so on...<br>
             This process is repeated until there's no any more nodes to visited.<br>
             However, ensure that the nodes are visited and also to be a completely sure that it checked every node,<br>
             In every iteration we added an edge of between the current nodes inside paths DS.<br>
             So if paths size equals the original graph size, then we're completely ok.<br>
             In DFS, if we start from a start node it will mark all the nodes connected to the start node as visited.<br>
             Therefore, if we choose any node in a connected component and run DFS on that node it will mark the whole connected component as visited.<br>
     * @param graph - a directed_weighted_graph type.
     * @param vertex - a node_data type.
     */
    private void DFS(directed_weighted_graph graph, node_data vertex, Stack<node_data> stack) {
        Stack<node_data> stack_dfs = new Stack<>();
        Stack<node_data> stack_like_recursive = new Stack<>();
        stack_dfs.push(vertex);
        stack_like_recursive.push(vertex);

        while (!stack_dfs.isEmpty()) {
            Node current = (Node) stack_dfs.pop();
            current.setTag(GRAY);

            for (edge_data edge : graph.getE(current.getKey())) {
                node_data dest = ((Edge) edge).destination;
                paths.add(edge);
                if (dest.getTag() != GRAY) {
                    dest.setTag(GRAY);
                    stack_dfs.push(dest);
                    stack_like_recursive.push(dest);
                }
            }
        }

        while(!stack_like_recursive.isEmpty()) {
            stack.push(stack_like_recursive.pop());
        }
    }


    private void DFSTransposed(directed_weighted_graph graph_t, node_data vertex, ArrayList<node_data> component) {
        Stack<node_data> stack_dfs = new Stack<>();
        stack_dfs.push(vertex);
        vertex.setTag(GRAY);

        while (!stack_dfs.isEmpty()) {
            node_data current = stack_dfs.pop();
            component.add(current);
            for (edge_data edge : graph_t.getE(current.getKey())) {
                node_data dest = ((Edge) edge).destination;
                if (dest.getTag() != GRAY) {
                    dest.setTag(GRAY);
                    stack_dfs.push(dest);
                }
            }
        }
    }
    /**
     * Copying the original graph and transposing the copied one.<br>
     * This copied graph is a temporary graph and made only for Kosaraju or Dijkstra use.<br>
     * This method iterate over all edges and reverse their direction.<br>
     * @param g a new directed_weighted_graph
     */
    private void graphTranspose(directed_weighted_graph g) {
        for (node_data runner : graph.getV()) {
            runner.setTag(Color.red.getRGB());
            g.addNode(new Node(runner));
        }
        for (edge_data edge : paths) {
            g.connect(edge.getDest(), edge.getSrc(), edge.getWeight());
        }
    }

    /**
     * A method that return the length of the shortest path between two nodes.
     * @note This method is using the Dijkstra algorithm.
             In the end, Dijkstra returns the path, and this function returns the distance from the given source<br>
             to the last node from the given path (which is the given destination).
     * @param src - start (source) node
     * @param dest - end (destination) node
     * @return the tag that keep the destination node.
     */
    @Override
    public double shortestPathDist(int src, int dest) {
        node_data source = graph.getNode(src);
        node_data destination = graph.getNode(dest);
        LinkedList<node_data> path = new LinkedList<>(Dijkstra(source, destination));
        if (!path.isEmpty()) {
            return path.getLast().getWeight();
        }
        return -1;
    }

    /**
     *A method that return the path of the shortest path between two nodes.
     *@note  This method implements the Dijkstra algorithm just like the method above implements.
     * @param src - start (source) node
     * @param dest - end (destination) node
     * @return a LinkedList that contains the correct path that start with the source node,
               and end with the destination node.
     */
    @Override
    public List<node_data> shortestPath(int src, int dest) {
        node_data source = graph.getNode(src);
        node_data destination = graph.getNode(dest);
        LinkedList<node_data> path = new LinkedList<>(Dijkstra(source, destination));
        if (!path.isEmpty()) {
            return path;
        }
        return null;
    }

    /**
     * @note This method implements the <strong>Dijkstra algorithm</strong> by mark the nodes,.<br>
             and also keep on each node the shortest path from the source node.<br>
             These nodes enters a priority queue and the nodes that poll from the queue will be<br>
             the nodes with the shortest distance (by using a comparator) and also they will marked.<br>
             it follows that the destination node will keep the shortest distance from the source node.<br>
             Dijkstra() is using the graphTranspose() to reverse the graph for an efficient result with makePath().<br>
     * @param source the source of this path.
     * @param destination the destination of this path.
     * @return a Collection of nodes of the shortest path between source to destination.
     */
    private Collection<node_data> Dijkstra(node_data source, node_data destination) {
        if (graph.getV().contains(source) && graph.getV().contains(destination) && source != destination
                && source != null && destination != null) {
            Reset();
            paths = new HashSet<>();
            Queue<node_data> queue = new PriorityQueue<>(new Comparator());
            source.setWeight(0);
            queue.add(source);
            while (!queue.isEmpty()) {
                node_data w = queue.poll();
                w.setInfo("visited");
                for (edge_data edge : graph.getE(w.getKey())) {
                    node_data dest = ((Edge) edge).destination;
                    paths.add(edge);
                    if (dest.getInfo().equals("unvisited")) {
                        double weight = w.getWeight() + edge.getWeight();
                        if (weight < dest.getWeight()) {
                            dest.setWeight(weight);
                            queue.add(dest);
                        }
                    }
                }
            }
            directed_weighted_graph graph_transpose = new DWGraph_DS();
            graphTranspose(graph_transpose);
            node_data src = graph_transpose.getNode(source.getKey());
            node_data dest = graph_transpose.getNode(destination.getKey());
            return makePath(graph_transpose, src, dest);
        }
        return new LinkedList<>();
    }

    /**
     * This method is supporting the Dijkstra algorithm.
     * After the nodes kept the shortest distance from the source node,
     * they enter a stack by a loop that starts at the destination node and ends at the source node.
     * each node that enters the stack must have a distance that corresponding to that of the previous one.
     * and finally those nodes are goes inside a list from beginning to the end by (LIFO).
     * @param graph - a transposed directed_weighted_graph.
     * @param source - a node_data type.
     * @param destination - a node_data type.
     * @return the shortest path between source to destination.
     */
    private Collection<node_data> makePath(directed_weighted_graph graph, node_data source, node_data destination) {
        Stack<node_data> stack = new Stack<>();
        Queue<node_data> queue = new LinkedList<>();
        LinkedList<node_data> path = new LinkedList<>();
        if (destination.getWeight() != Double.MAX_VALUE) {
            stack.add(destination);
            node_data current = destination;
            while (current != source) {
                if(current != null) {
                    for (edge_data edge : graph.getE(current.getKey())) {
                        double weight = current.getWeight() - edge.getWeight();
                        node_data w = ((Edge) edge).destination;
                        if (Math.abs(w.getWeight() - weight) < EPSILON) {
                            stack.push(w);
                            queue.add(w);
                            break;
                        }
                    }
                    current = queue.poll();
                }
            }
            while (!stack.isEmpty()) {
                path.add(stack.pop());
            }
        }
        return path;
    }

    /**
     * A method that performs graph object serialization.
     * It serialize it to a JSON file, and save it in the default folder.
     * @param file - the file name (may include a relative path).
     * @return true if and only if the graph stored.
     */
    @Override
    public boolean save(String file) {
        Gson gson = new Gson();
        JsonObject jsonGraph = new JsonObject();
        JsonArray Edges = new JsonArray();
        JsonArray Nodes = new JsonArray();
        // initialize the nodes from the graph to Nodes jsonArray object
        for (node_data runner : graph.getV()) {
            JsonObject v = new JsonObject();
            String location = runner.getLocation().x() + "," + runner.getLocation().y() + "," + runner.getLocation().z();
            v.addProperty("pos", location);
            v.addProperty("id", runner.getKey());
            Nodes.add(v);
        }
        // initialize the edges from graph to Edges JsonArray object
        for (edge_data edge : ((DWGraph_DS) graph).edges) {
            JsonObject e = new JsonObject();
            e.addProperty("src", edge.getSrc());
            e.addProperty("w", edge.getWeight());
            e.addProperty("dest", edge.getDest());
            Edges.add(e);
        }
        jsonGraph.add("Edges", Edges);
        jsonGraph.add("Nodes", Nodes);
        String json = gson.toJson(jsonGraph);
        try {
            PrintWriter pw = new PrintWriter(file);
            pw.write(json);
            pw.close();
            return true;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return false;
    }

    /**
     * A method that preforms graph object deserialization.
     * The deserialization is used with 'graphDeserialization' object (for more details, check its info).
     * @param file - file name (may include a relative path).
     * @return true if and only if the graph is load in successful way.
     */
    @Override
    public boolean load(String file) {
        try {
            GsonBuilder builder = new GsonBuilder()
                    .registerTypeAdapter(directed_weighted_graph.class, new graphDeserialization());
            Gson gson = builder.create();
            FileReader fr = new FileReader(file);

            this.graph = gson.fromJson(fr, directed_weighted_graph.class);

            return true;
        } catch (FileNotFoundException f) {
            return false;
        }
    }

    /**
     * resets fields to avoid invalid markings.
     */
    private void Reset() {
        for (node_data runner : graph.getV()) {
            runner.setTag(Color.RED.getRGB());
            runner.setWeight(Double.MAX_VALUE);
            runner.setInfo("unvisited");
        }
    }

    /**
     * compare the weight of nodes, the minimal one will be its priority.
     */
    private static class Comparator implements java.util.Comparator<node_data> {
        @Override
        public int compare(node_data o1, node_data o2) {
            return Double.compare(o1.getWeight(), o2.getWeight());
        }
    }


    public void Analysis(String str) {
        System.out.println(" ---- TEST FOR "+str+" ---------");

        //load
        double start = System.currentTimeMillis();
        this.load(str);
        double end = (System.currentTimeMillis() - start) / 1000;
        System.out.println("-> load: "+end);

        // shortest path
        Node source = (Node) this.graph.getNode((int) (Math.random() * this.graph.nodeSize()));
        Node destination = (Node) this.graph.getNode((int) (Math.random() * this.graph.nodeSize()));
        start = System.currentTimeMillis();
        shortestPath(source.getKey(),destination.getKey());
        end = (System.currentTimeMillis() - start) / 1000;
        System.out.println("-> shortest path: "+end);

        // connected component
        start = System.currentTimeMillis();
        isConnected();
        end = (System.currentTimeMillis() - start) / 1000;
        System.out.println("-> connected component: "+end);

        // connected components
        start = System.currentTimeMillis();
        isConnected();
        end = (System.currentTimeMillis() - start) / 1000;
        System.out.println("-> connected components: "+end);
    }

    public static void main(String[] args) {
        System.out.println("---------- JAVA TEST --------- ");

        DWGraph_Algo algo = new DWGraph_Algo();
        ArrayList<String> list = new ArrayList<>();
        list.add("data/G_10_80_1.json");
        list.add("data/G_100_800_1.json");
        list.add("data/G_1000_8000_1.json");
        list.add("data/G_10000_80000_1.json");
        list.add("data/G_20000_160000_1.json");
        list.add("data/G_30000_240000_1.json");

        for(String str : list){
            algo.Analysis(str);
        }

    }
}
