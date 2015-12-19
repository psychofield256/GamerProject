package items.edible;

import perso.Personnage;

public class LifePotionLVL1 extends Potion{

	public LifePotionLVL1() {
		// TODO Auto-generated constructor stub
		regen = 100;
	}
	
	public void use(Personnage p){
		//heals
		int life = p.getLife();
		p.setLife(life+this.regen);
	}
}
