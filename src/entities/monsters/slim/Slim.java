package entities.monsters.slim;

import perso.Personnage;
import perso.Stats;

public class Slim {

	int life, lifeMax, mana, manaMax;
	Stats stats;
	public Slim() {
		// TODO Auto-generated constructor stub
		lifeMax = 10;
		life = lifeMax;
		manaMax = 5;
		mana = manaMax;
		stats = new Stats(4, 3, 5, 2, 2, 2);
	}
	
	public void attaquer(Personnage p){
		int life = p.getLife();
		int def = p.getStr();
		int att = this.stats.getStr();
		int damages = att/2 - def/4;
		life -= damages;
		p.setLife(life);
	}

}
