recorddefs = {
#envelope segments
'STX':  [
	['BOTSID','M',3,'X'],
	['STDS', 'M',
		[
		['STDS1', 'M', 4, 'X'],
		['STDS2', 'M', 1, '9'],
		]],
	['FROM', 'M',
		[
		['FROM.01', 'C', 14, 'X'],
		['FROM.02', 'C', 35, 'X'],
		]],
	['UNTO', 'M',
		[
		['UNTO.01', 'C', 14, 'X'],
		['UNTO.02', 'C', 35, 'X'],
		]],
	['TRDT', 'M',
		[
		['TRDT.01', 'M', (6,6), 'X'],
		['TRDT.02', 'C', (6,6), 'X'],
		]],
	['SNRF', 'M', 14, 'X'],
	['RCRF', 'C', 14, 'X'],
	['APRF', 'C', 14, 'X'],
	['PRCD', 'C', 1, 'X'],
	],
'MHD':  [
	['BOTSID','M',3,'X'],
	['MSRF', 'M', 12, 'X'],
	['TYPE', 'M',
		[
		['TYPE.01', 'M', 6, 'X'],
		['TYPE.02', 'M', 1, 'X'],
		]],
	],
'MTR':  [
	['BOTSID','M',3,'X'],
	['NOSG', 'M', 10, '9'],
	],
'END':  [
	['BOTSID','M',3,'X'],
	['NMST', 'M', 5, '9'],
	],
}
