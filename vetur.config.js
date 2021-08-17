/** @type {import('vls').VeturConfig} */
module.exports = {
	settings: {
	  "vetur.useWorkspaceDependencies": true,
	  "vetur.experimental.templateInterpolationService": true
	},
	// support monorepos
	projects: [
	  './app_vue',
	],
  };
