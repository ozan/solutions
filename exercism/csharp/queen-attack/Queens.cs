using System;
using System.Collections.Generic;
using System.Linq;

public class Queen
{
    public int Rank;
    public int File;

    public Queen (int rank, int file)
    {
        Rank = rank;
        File = file;
    }
}

public class Queens
{
    Queen White;
    Queen Black;

    public Queens (Queen white, Queen black)
    {
        if (white.Rank == black.Rank && white.File == black.File)
            throw new ArgumentException();
        White = white;
        Black = black;
    }

    public bool CanAttack ()
    {
        return White.Rank == Black.Rank
            || White.File == Black.File
            || Math.Abs(White.Rank - Black.Rank) == Math.Abs(White.File - Black.File);
    }
}
