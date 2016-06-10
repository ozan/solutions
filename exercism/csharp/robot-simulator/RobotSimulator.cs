using System;
using System.Collections.Generic;
using System.Linq;

public enum Bearing { North, East, South, West };

public class Coordinate : System.Object
{
    public int X, Y;

    public Coordinate (int x, int y)
    {
        this.X = x;
        this.Y = y;
    }

    public override string ToString ()
    {
        return String.Format("{0}, {1}", this.X, this.Y);
    }

    public override bool Equals (System.Object obj)
    {
        if (obj == null) return false;
        Coordinate other = obj as Coordinate;
        if ((System.Object)other == null) return false;
        return X == other.X && Y == other.Y;
    }

}

public class RobotSimulator
{
    public Bearing Bearing;
    public Coordinate Coordinate;

    static Dictionary<Bearing, Coordinate> Offsets = new Dictionary<Bearing, Coordinate> {
        { Bearing.North, new Coordinate(0, 1) },
        { Bearing.East, new Coordinate(1, 0) },
        { Bearing.South, new Coordinate(0, -1) },
        { Bearing.West, new Coordinate(-1, 0) }
    };

    public RobotSimulator (Bearing bearing, Coordinate coords)
    {
        this.Bearing = bearing;
        this.Coordinate = coords;
    }

    public void TurnRight () { Turn(1); }

    public void TurnLeft () { Turn(-1); }

    public void Simulate (string instructions)
    {
        foreach (var ch in instructions) {
            switch (ch) {
                case 'L':
                    TurnLeft();
                    break;
                case 'R':
                    TurnRight();
                    break;
                case 'A':
                    Advance();
                    break;
            }
        }
    }

    void Advance ()
    {
        var offset = Offsets[this.Bearing];
        this.Coordinate = new Coordinate(
            this.Coordinate.X + offset.X,
            this.Coordinate.Y + offset.Y
        );
    }

    void Turn (int amount)
    {
        this.Bearing = (Bearing)Remainder((int)this.Bearing + amount, 4);
    }

    int Remainder (int n, int k)
    {
        return ((n % k) + k) % k;
    }
}
