require.config({
    paths: {
        'jquery': 'libs/jquery-2.1.3.min',
        'bootstrap': 'libs/bootstrap.min', 
        'cledit': 'libs/cledit.min'
    },
    urlArgs: "_=" + Math.round(Math.random() * 10000)
    // shim: {
    //     "bootstrap": {"deps":['jquery']}
    // }
})
