using System;
using System.Collections.Generic;
using System.Linq;

public class SimpleLinkedList<T> : IEnumerable<T>
{
    public T Value;
    public SimpleLinkedList<T> Next;

    public SimpleLinkedList (T val)
    {
        Value = val;
    }

    public SimpleLinkedList (IEnumerable<T> vals)
    {
        Value = vals.First();
        var node = this;
        foreach (var val in vals.Skip(1)) {
            node.Add(val);
            node = node.Next;
        }
    }

    public SimpleLinkedList<T> Add (T val)
    {
        var nextLink = new SimpleLinkedList<T>(val);
        nextLink.Next = Next;
        Next = nextLink;
        return this;
    }

    public IEnumerator<T> GetEnumerator()
    {
        yield return Value;
        if (Next != null) {
          foreach (var val in Next) yield return val;
        }
    }

    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
    {
        return this.GetEnumerator();
    }
}
