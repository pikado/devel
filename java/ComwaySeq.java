package net.mathematics;

public class ConwaySeq {

	static String lookAndSay(String seq) {
		int k, p, nb;
		k = 0;
		String res = "";
		while (k < seq.length()) {
			p = k + 1;
			nb = 1;
			while (p < seq.length() && seq.charAt(p) == seq.charAt(k)) {
				nb++;
				p++;
			}
			res = res + String.valueOf(nb) + seq.charAt(k);
			k = k + nb;

		}
		return res;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String u[];
		u = new String[30];
		u[0] = "1";
		System.out.println("u(0)=" + u[0]);
		int i = 1;

		while (i < u.length) {
			u[i] = lookAndSay(u[i - 1]);
			System.out.println("u(" + i + ")=" + u[i]);
			i++;
		}

	}
}
