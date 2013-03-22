object Solution {
  def main(args: Array[String]) = { 
    val m :Int = Integer.parseInt(Console.readLine)
    val grid = (0 until m).map( x => Console.readLine ) mkString ""
    displayPathtoPrincess(m,grid);
  }
  def displayPathtoPrincess(M:Int,grid:String)={
    val found = grid.zipWithIndex.filter(x => x._1 != '-')
    val List(p,m) = ((if (found(0)._1 == 'p') found else found.reverse).toList).map(x => (x._2 % M, x._2 / M))
    val h = if (p._1>m._1) "RIGHT" else "LEFT"
    val v = if (p._2>m._2) "UP" else "DOWN"
    for( _ <- 0 until (p._1-m._1).abs ) println(h)
    for( _ <- 0 until (p._2-m._2).abs ) println(v)
  }
}
