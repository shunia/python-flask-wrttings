require.config({
    paths: {
        'jquery': 'libs/jquery-2.1.3.min',
        'bootstrap': 'libs/bootstrap.min'
    },
    urlArgs: "_v=" + Math.random()
    // shim: {
    //     "bootstrap": {"deps":['jquery']}
    // }
})
