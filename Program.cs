// See https://aka.ms/new-console-template for more information
// input 

namespace Inverse
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the string you want to inverse: ");
            string stringToInverse = Console.ReadLine();

            Console.WriteLine(Inverse(stringToInverse));

            string Inverse(string name)
            {
                if (name.Length == 1)
                {
                    return name;
                }
                else
                {
                    return Inverse(name.Substring(1)) + name[0];
                }
            }
        }
    }


}
