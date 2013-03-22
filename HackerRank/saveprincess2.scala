object Solution {
  def main(args: Array[String]) = { 
    val m :Int = Integer.parseInt(Console.readLine)
    val List(y,x) = Console.readLine.split(" ").map(x=>x.toInt).toList
    val grid = (0 until m).map( x => Console.readLine ) mkString ""
    nextMove(m,x,y,grid)
  }
  def nextMove(M:Int,x:Int, y:Int,grid:String)={
    val List(p) = List(grid.indexOf('p')).map( x => ( x % M, x / M ) )
    println (
      if ( x > p._1 ) "LEFT" else
        if ( x < p._1 ) "RIGHT" else
          if ( y > p._2 ) "UP" else 
          "DOWN"
        )
  }
}
