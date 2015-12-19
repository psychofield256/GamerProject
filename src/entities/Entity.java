package entities;

import perso.Stats;

public abstract class Entity {

	protected int life, lifeMax, mana, manaMax, level;
	protected Stats stats;
	protected boolean isDefending = false;
	public void attaquer(Entity e){
		int life = e.life;
		int damages = (this.getStr()/2) - (e.getStr()/4);
		
	}
	public void defendre() {
		this.isDefending = true;
		int str = this.getStr();
		str *= 2;
		//TODO setSTR
	};
	/*public void use(Skill s) { }*/
	
	//getters
	public int getStr(){
		return this.stats.getStr();
	}
	public int getDex(){
		return this.stats.getDex();
	}
	public int getVit(){
		return this.stats.getVit();
	}
	public int getInt(){
		return this.stats.getInt();
	}
	public int getWis(){
		return this.stats.getWis();
	}
	public int getLuk(){
		return this.stats.getLuk();
	}
	
}
