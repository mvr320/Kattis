import java.util.Scanner;
class ANewAlphabet{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		in.useDelimiter("\\n");
		String output = in.next();
		output = output.toLowerCase();
		output = output.replaceAll("a", "@");
		output = output.replaceAll("b", "8");
		output = output.replaceAll("c", "(");
		output = output.replaceAll("d", "|)");
		output = output.replaceAll("e", "3");
		output = output.replaceAll("f", "#");
		output = output.replaceAll("g", "6");
		output = output.replaceAll("h", "[-]");
		output = output.replaceAll("i", "|");
		output = output.replaceAll("j", "_|");
		output = output.replaceAll("k", "|<");
		output = output.replaceAll("l", "1");
		output = output.replaceAll("m", "[]\\\\/[]");
		output = output.replaceAll("n", "[]\\\\[]");
		output = output.replaceAll("o", "0");
		output = output.replaceAll("p", "|D");
		output = output.replaceAll("q", "(,)");
		output = output.replaceAll("r", "|Z");
		output = output.replaceAll("s", "\\$");
		output = output.replaceAll("t", "']['");
		output = output.replaceAll("u", "|_|");
		output = output.replaceAll("v", "\\\\/");
		output = output.replaceAll("w", "\\\\/\\\\/");
		output = output.replaceAll("x", "}{");
		output = output.replaceAll("y", "`/");
		output = output.replaceAll("z", "2");
        System.out.printf("%s", output);
    }
}
