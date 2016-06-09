using System;
using System.Collections.Generic;


class Node<T>
{
    public T Value;
    public Node<T> Next;
    public Node<T> Prior;

    public Node (T item)
    {
        Value = item;
    }
}


public class Deque<T>
{
    Node<T> Head;
    Node<T> Tail;

    public void Push (T item)
    {
        var newNode = new Node<T>(item);
        if (Tail != null) {
            newNode.Prior = Tail;
            Tail.Next = newNode;
            Tail = newNode;
        } else {
            Head = newNode;
            Tail = newNode;
        }
    }

    public void Unshift (T item)
    {
        var newNode = new Node<T>(item);
        if (Head != null) {
            newNode.Next = Head;
            Head.Prior = newNode;
            Head = newNode;
        } else {
            Head = newNode;
            Tail = newNode;
        }
    }

    public T Pop ()
    {
        if (Tail == null) throw new InvalidOperationException();
        var toReturn = Tail.Value;
        if (Tail.Prior != null) Tail.Prior.Next = null;
        Tail = Tail.Prior;
        return toReturn;
    }

    public T Shift ()
    {
        if (Head == null) throw new InvalidOperationException();
        var toReturn = Head.Value;
        if (Head.Next != null) Head.Next.Prior = null;
        Head = Head.Next;
        return toReturn;
    }
}
