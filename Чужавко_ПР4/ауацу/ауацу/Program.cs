//using ауацу;

//Figure[] mas = new Figure[2];
//mas[0] = new Pryamougolnik(2, 4);
//mas[1] = new Parallelepiped(4, 3, 2);
//foreach(var figure in mas)
//{
//    Console.WriteLine(figure.Square());
//}

//Circle circle = new Circle(3);
//Console.WriteLine(circle.Square());


//Kvadrat[] mass=new Kvadrat[2];
//mass[0]=new Kvadrat(2);
//mass[1] = new Pryamoygolnik(2, 4);
//foreach(var fig in mass)
//{
//    Console.WriteLine($"s={fig.Square()}\np={fig.Perimetr()}");
//}

//Circlee[] mmm=new Circlee[2];
//mmm[0] = new Circlee(4);
//mmm[1]=new Circlee(3);
//Array.Sort(mmm);
//foreach(var fig in mmm)
//{
//    Console.WriteLine(fig.s)
//}

int[] mas=new int[10] {3,0,1,3,5,6,0,6,4,1};
int sum = 0, firstzero=-1, lastzero=-1;
for(int i = 0; i < mas.Length; i++)
    if(mas[i] == 0)
    {
        firstzero = i;
        break;
    }
for(int i = mas.Length-1;i>=0;i--)
    if(mas[i] == 0)
    {
        lastzero = i;
        break;
    }
for(;firstzero<lastzero;firstzero++)
    sum+=mas[firstzero];
Console.WriteLine(sum);