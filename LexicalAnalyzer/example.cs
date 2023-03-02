using System;
namespace YourNamespace
{
     class Program
     {
         double sumCalc(double a, double b){
            if (a < b)
            {
                b = (b - a) * 2.0;
            }
            else b = (b+a) * 2.0;
            double sum = (a+b)*b/7;
            return sum;
        }
         static void Main(string[] args)
         {
            double a = 10;
            double b = 20;
            double result = sumCalc(a, b);
            string answer = result.ToString();
            Console.WriteLine(answer);
         }
     }
}


