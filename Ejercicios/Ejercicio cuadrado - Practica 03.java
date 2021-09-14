/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_CUADRADO.java."

import java.io.*;

public class ejercicio_cuadrado {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int lado;
		int peri;
		System.out.println("Ingrese el lado del cuadrado:");
		lado = Integer.parseInt(bufEntrada.readLine());
		peri = lado*4;
		System.out.println("El perimetro del cuadrado es: "+peri);
	}


}

