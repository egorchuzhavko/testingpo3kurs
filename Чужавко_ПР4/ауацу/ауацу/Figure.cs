using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ауацу
{
    abstract class Figure
    {
        protected double a;
        protected double b;
        public double GetA() { return a; }
        public double GetB() { return b; }

        public void SetA(double value) { a = value; }
        public void SetB(double value) { b = value; }
        public abstract double Square();

        public Figure(double a, double b)
        {
            this.a = a;
            this.b = b;
        }
    }

    class Pryamougolnik : Figure
    {
        public Pryamougolnik(double a,double b) : base(a, b) { }
        public override double Square() { return a * b; }
    }

    class Parallelepiped : Pryamougolnik
    {
        protected double h;
        public Parallelepiped(double a, double b, double h) : base(a, b) { this.h = h; }

        public double GetH() { return h; }
        public void SetH(double value) { h = value; }

        public override double Square() { return 2 * (h * a + h * b + a * b); }
    }

    class Line
    {
        private double a;
        private double b;

        public Line(double a, double b)
        {
            this.a = a;
            this.b = b;
        }

        public bool IsEqual(Line other)
        {
            if (this.a == other.a & this.b == other.b)
                return true;
            else
                return false;
        }
    }

    abstract class Figuree
    {
        protected double r;

        abstract public double Square();

        public Figuree(double r) { this.r = r; }
    }

    class Circle : Figuree
    {
        public Circle(double r) : base(r) { }

        public override double Square() { return Math.PI * Math.Pow(r, 2); }
    }

    class Kvadrat
    {
        protected double a;

        public Kvadrat(double a) { this.a = a; }

        public virtual double Square() { return Math.Pow(a,2); }
        public virtual double Perimetr() { return 4 * a; }
    }
    class Pryamoygolnik : Kvadrat
    {
        protected double b;
        public Pryamoygolnik(double a, double b):base(a) { this.b = b; }
        public override double Square() { return a * b; }
        public override double Perimetr() { return a * 2 + b * 2; }
    }

    interface IPrint
    {
        void Print();
    }

    public class Student : IPrint
    {
        private string fio;
        private double mark;

        public Student(string fio, double mark)
        {
            this.fio = fio;
            this.mark = mark;
        }
        public void Print()
        {
            Console.WriteLine($"{fio} имеет оценку {mark} по КПиЯП");
        }
    }

    public class Circlee: IComparable
    {
        public double s;
        public Circlee(double s) { this.s = s; }

        public int CompareTo(object obj)
        {
            Circlee c=obj as Circlee;
            return this.s.CompareTo(c.s);
        }
    }
}
