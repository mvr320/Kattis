import java.util.Scanner;
class Cetvrta
{
	public static void main(String args[]){
        Scanner in = new Scanner(System.in);
	   	int[] x = new int[4];
	   	int[] y = new int[4];
		x[0] = in.nextInt();
		y[0] = in.nextInt();
		x[1] = in.nextInt();
		y[1] = in.nextInt();
		x[2] = in.nextInt();
		y[2] = in.nextInt();
		if(x[0] == x[1]){
			x[3] = x[2];
		} else if (x[0] == x[2]){
			x[3] = x[1];
		} else {
			x[3] = x[0];
		}
		if(y[0] == y[1]){
			y[3] = y[2];
		} else if (y[0] == y[2]){
			y[3] = y[1];
		} else {
			y[3] = y[0];
		}
		System.out.printf("%d %d",x[3], y[3]);
        }
}
