package perso;

import items.edible.Potion;
import items.items.EmptyPotion;

public class Personnage {

	int life, lifeMax, mana, manaMax, exp, expMax;
	Stats stats;
	public Personnage(){
		lifeMax = 100;
		life = lifeMax;
		manaMax = 100;
		mana = manaMax;
		exp = 0;
		expMax = 50;
		stats = new Stats();
	}
	
	public void usePotion(Potion p){
		p.use(this);
		if (life > lifeMax){
			//a good rpg character shouldn't have more hp than that
			life = lifeMax;
		}
		//TODO after adding an inventory, delete the potion and create
		//an EmptyPotion
	}
	
	public void tryLevelUp(){
		if (exp >= expMax){
			//remove the exp and keep the extra
			exp -= expMax;
			//the required exp is multiplied by 1.5
			expMax *= 1.5;
		}
	}
	
	//getters
	public int getLife() {
		return life;
	}
	public int getLifeMax() {
		return lifeMax;
	}
	public int getMana() {
		return mana;
	}
	public int getManaMax() {
		return manaMax;
	}
	public int getExp(){
		return exp;
	}
	public int getExpMax(){
		return expMax;
	}
	public int getStr(){
		return stats.str;
	}
	public int getDex(){
		return stats.dex;
	}
	public int getVit(){
		return stats.vit;
	}
	public int getInt(){
		return stats.intel;
	}
	public int getWis(){
		return stats.wis;
	}
	public int getLuck(){
		return stats.luk;
	}
	
	
	
	
	
	//setters
	public void setLife(int life) {
		this.life = life;
	}
	public void setMana(int mana) {
		this.mana = mana;
	}
	public void setExp(int newValue){
		this.exp = newValue;
		this.tryLevelUp();
	}
	
	public void addExp(int newExp){
		this.exp += newExp;
	}



	



	
}
