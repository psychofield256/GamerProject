package items.items;

import items.edible.Potion;
import perso.Personnage;

public class EmptyPotion extends Potion{

	String nom, description;
	public EmptyPotion() {
		// TODO Auto-generated constructor stub
		nom = "flacon";
		description = "Objet pouvant servir dans l'alchimie";
		regen = 0;
	}
	
	public void use(Personnage p){
		System.out.println("Action impossible");
	}

}
