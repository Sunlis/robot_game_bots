import rg
import random

class Robot:
	def act(self, game):
		closest = self.findNearestEnemy(game)
		run_to = self.runAwayFrom(closest)
		if run_to == self.location:
			return ['guard']
		else:
			return self.move_to(run_to)

	def runAwayFrom(self, enemy):
		valid_locs = rg.locs_around(self.location, filter_out=('invalid', 'obstacle', 'spawn'))
		farthest = self.location
		farthest_dist = rg.wdist(farthest, enemy.location)
		for loc in valid_locs:
			dist = rg.wdist(loc, enemy.location)
			if dist > farthest_dist:
				farthest = loc
				farthest_dist = dist
		return farthest

	def findNearestEnemy(self, game):
		enemies = self.getEnemies(game)
		closest = enemies[0]
		closestDist = rg.wdist(closest.location, self.location)
		for enemy in enemies[1:]:
			dist = rg.wdist(enemy.location, self.location)
			if dist < closestDist:
				closest = enemy
				closestDist = dist
		return closest
	
	def getEnemies(self, game):
		return [bot for loc, bot in game['robots'].iteritems() if bot.player_id != self.player_id]

	def move_to(self, loc):
		return ['move', loc]
	def move(self, dir):
		return ['move', self.direction(dir)]
	def attach(self, dir):
		return ['attack', self.direction(dir)]
	def guard(self):
		return ['guard']
	def suicide(self):
		return ['suicide']
	def direction(self, dir):
		if dir == "up":
			return (self.location[0], self.location[1]-1)
		elif dir == "down":
			return (self.location[0], self.location[1]+1)
		elif dir == "left":
			return (self.location[0]-1, self.location[1])
		elif dir == "right":
			return (self.location[0]+1, self.location[1])