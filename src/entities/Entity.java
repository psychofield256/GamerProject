package entities;

import perso.Stats;
import perso.Skills;

public interface Entity {

	public void attaquer(Entity e);
	public void defendre();
	public void use(Skill s);
}
