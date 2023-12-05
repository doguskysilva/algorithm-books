enum class COLOR {
    WHITE,
    GREY,
    BLACK,
}

data class Node(
    val value: String,
    val color: COLOR = COLOR.WHITE,
    val distance: Int = -1,
    val next: Node? = null
)

class Graph {

    private var vertices: Int
    private lateinit var graph: List<Node?>

    constructor(vertices: Int) {
        this.vertices = vertices
        this.graph = List(vertices) { null }
    }

    fun addEdge(s: String, d: String) {
        val node = Node(d)
        node.next = this.graph.get()
    }
}

fun main() {
    print("Hello BFS")
    val graph = Graph(5)


}