import perso.Personnage;
import items.edible.LifePotionLVL1;

public class GamerProject {

	public static void main(String[] args){
		System.out.println("Quel jeu magnifique !");
		Personnage m = new Personnage();
		m.tryLevelUp();
		LifePotionLVL1 l = new LifePotionLVL1();
		m.usePotion(l);
		m.usePotion(l);
		System.out.println(m.getLife());
		
	}
}
