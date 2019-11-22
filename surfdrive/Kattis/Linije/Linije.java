import java.util.Scanner;
import java.util.HashSet;
class Linije
{
	public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        HashSet<Integer> x = new HashSet<Integer>();
        HashSet<Integer> y = new HashSet<Integer>();
	   	int numCoord = in.nextInt();
	   	for(int i=0; i<numCoord; i++){
	   		x.add(new Integer(in.nextInt()));
	   		y.add(new Integer(in.nextInt()));
	   	}
	   	if(x.size()%2==1 || y.size()%2==1){
	   		System.out.printf("Mirko");
	   	} else {
	   		System.out.printf("Slavko");
	   	}
	}
}
