exports.config = {
    seleniumAddress: 'http://localhost:4444/wd/hub',
    specs: ['todo-spec.js'],
	onPrepare: function() {
	    var webRep = require('jasmine-web-reporter');
	    browser.getProcessedConfig().then(function(config) {
	        var browserName = config.capabilities.browserName;
	        jasmine.getEnv().addReporter(new webRep.WebReporter({
	            projectName:'Protractor',        
	            url: 'https://tutorials.qaconsole.io/testruns',
	            environment : 'Local',
	            apiKey: 'a56f391f-b767-4900-971c-6caa576ccae',
	            info : {
	             "browserName" : config.capabilities.browserName
	            }
	        }));
	    });
    }
  };