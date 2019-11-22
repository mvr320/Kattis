import java.util.Scanner;
class ColdputerScience
{
	public static void main(String args[]){
        Scanner in = new Scanner(System.in);
	   	in.next();
	   	in.useDelimiter("\n");
	   	String result = in.next();
	   	int sum=0;
	   	for(int i=0; i<result.length(); i++){
	   		sum += result.charAt(i)=='-' ? 1 : 0;
	   	}
	   	System.out.printf("%d",sum);
        }
}
