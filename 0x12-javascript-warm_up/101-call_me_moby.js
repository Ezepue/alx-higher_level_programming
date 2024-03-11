#!/usr/bin/node
exports.callMeMoby = function (no, func) {
	for (let i = 0; i < no; i++) {
	  func();
	}
};
