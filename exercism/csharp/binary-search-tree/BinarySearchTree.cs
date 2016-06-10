using System;
using System.Collections.Generic;
using System.Linq;

public class BinarySearchTree
{
    public int Value;
    public BinarySearchTree Left;
    public BinarySearchTree Right;

    public BinarySearchTree (int val)
    {
        Value = val;
    }

    public BinarySearchTree (int[] vals)
    {
        Value = vals[0];
        foreach (int val in vals.Skip(1)) Add(val);
    }

    public BinarySearchTree Add (int val)
    {
        var newTree = new BinarySearchTree(val);
        if (val <= Value) {
            Left = Left == null ? newTree : Left.Add(val);
        } else {
            Right = Right == null ? newTree : Right.Add(val);
        }
        return this;
    }

    public IEnumerable<int> AsEnumerable ()
    {
          if (Left != null) {
              foreach (int v in Left.AsEnumerable()) yield return v;
          }
          yield return Value;
          if (Right != null) {
              foreach (int v in Right.AsEnumerable()) yield return v;
          }
    }
}
