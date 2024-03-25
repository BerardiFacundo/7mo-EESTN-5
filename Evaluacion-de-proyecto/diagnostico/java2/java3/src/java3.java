
public class java3 {

}
abstract class NaveEspacial {
    protected String nombre;
    protected int energia;
    protected double posicionX;
    protected double posicionY;

    public NaveEspacial(double posicionX, double posicionY) {
        this.posicionX = posicionX;
        this.posicionY = posicionY;
    }

    // Getters y Setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getEnergia() {
        return energia;
    }

    public void setEnergia(int energia) {
        this.energia = energia;
    }

    public double getPosicionX() {
        return posicionX;
    }

    public void setPosicionX(double posicionX) {
        this.posicionX = posicionX;
    }

    public double getPosicionY() {
        return posicionY;
    }

    public void setPosicionY(double posicionY) {
        this.posicionY = posicionY;
    }

    // Método para mover la nave
    public void mueve(double x, double y) {
        this.posicionX += x;
        this.posicionY += y;
    }

    // Método abstracto para atacar
    public abstract void ataca(NaveEspacial adversario);

    // Método toString
    @Override
    public String toString() {
        return "NaveEspacial{" +
                "nombre='" + nombre + '\'' +
                ", energia=" + energia +
                ", posicionX=" + posicionX +
                ", posicionY=" + posicionY +
                '}';
    }
}

class DestructorEstelar extends NaveEspacial {
    private int cantidadTripulantes;
    private static final int ENERGIA_INICIAL = 1000;

    public DestructorEstelar(double posicionX, double posicionY, int cantidadTripulantes) {
        super(posicionX, posicionY);
        this.cantidadTripulantes = cantidadTripulantes;
        this.energia = ENERGIA_INICIAL;
    }

    // Getters y Setters
    public int getCantidadTripulantes() {
        return cantidadTripulantes;
    }

    public void setCantidadTripulantes(int cantidadTripulantes) {
        this.cantidadTripulantes = cantidadTripulantes;
    }

    // Método para atacar
    @Override
    public void ataca(NaveEspacial adversario) {
        adversario.setEnergia(adversario.getEnergia() - 200);
    }

    // Sobrescribe el método mueve para reducir los incrementos un 50%
    @Override
    public void mueve(double x, double y) {
        this.posicionX += x * 0.5;
        this.posicionY += y * 0.5;
    }

    // Método toString
    @Override
    public String toString() {
        return "DestructorEstelar{" +
                "nombre='" + nombre + '\'' +
                ", energia=" + energia +
                ", posicionX=" + posicionX +
                ", posicionY=" + posicionY +
                ", cantidadTripulantes=" + cantidadTripulantes +
                '}';
    }
}

class CazaLigero extends NaveEspacial {
    private static final int ENERGIA_INICIAL = 500;

    public CazaLigero(double posicionX, double posicionY) {
        super(posicionX, posicionY);
        this.energia = ENERGIA_INICIAL;
    }

    // Método para atacar
    @Override
    public void ataca(NaveEspacial adversario) {
        adversario.setEnergia(adversario.getEnergia() - 50);
    }

    // Método toString
    @Override
    public String toString() {
        return "CazaLigero{" +
                "nombre='" + nombre + '\'' +
                ", energia=" + energia +
                ", posicionX=" + posicionX +
                ", posicionY=" + posicionY +
                '}';
    }
}

public class PruebaNaves {
    public static void main(String[] args) {
        // Crear naves espaciales
        NaveEspacial destructor = new DestructorEstelar(100, 200, 500);
        NaveEspacial caza = new CazaLigero(300, 400);

        // Mostrar información de las naves
        System.out.println("Nave Destructor Estelar:");
        System.out.println(destructor);
        System.out.println("Nave Caza Ligero:");
        System.out.println(caza);

        // Mover las naves
        destructor.mueve(50, 50);
        caza.mueve(20, 20);

        // Mostrar información de las naves después de moverlas
        System.out.println("Nave Destructor Estelar después de moverse:");
        System.out.println(destructor);
        System.out.println("Nave Caza Ligero después de moverse:");
        System.out.println(caza);

        // Atacar con las naves
        System.out.println("Ataque del Nave Destructor Estelar a la Nave Caza Ligero:");
        destructor.ataca(caza);
        System.out.println("Nave Caza Ligero después del ataque:");
        System.out.println(caza);
    }
}
