import java.util.Scanner;
class AnotherCandies
{
	public static void main(String args[]){
        Scanner in = new Scanner(System.in);
	   	int cases = in.nextInt();
	   	for(int i=0; i<cases; i++){
	   		long remain = 0;
	   		long child = in.nextLong();
	   		for(long j=0; j<child; j++){
				remain = (remain+in.nextLong())%child;
	   		}
	   		if(remain==0){
	   			System.out.printf("YES\n");
	   		} else {
	   			System.out.printf("NO\n");
	   		}
	   	}
	}
}
