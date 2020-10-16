var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
        var response = this.response;
        var output = response.split("\n");

        var date = [];
        var totalCases = [];
        var newCases = [];
        var totalDeaths = [];
        var newDeaths = [];
        var stringencyIndex = [];
        for (let column = 1; column < output.length; column++) {
            let temp = output[column].split(",");
            date.push(temp[0]);
            totalCases.push(temp[1]);
            newCases.push(temp[2]);
            totalDeaths.push(temp[3]);
            newDeaths.push(temp[4]);
            stringencyIndex.push(temp[5]);
        }

        var topLineOptions = {
            elements: {
                point: {
                    radius: 0
                }
            },
            tooltips: {
                enabled: false,
            },
            hover: {
                mode: null,
            },
            legend: {
                display: false,
            },
            scales: {
                xAxes: [{
                    ticks: {
                        display: false,
                    },
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                }],
                yAxes: [{
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    ticks: {
                        display: false,
                    },
                }]
            }
        }

        var newCasesLine = document.getElementById('newCasesLine').getContext('2d');
        new Chart(newCasesLine, {
            type: 'line',
            data: {
                labels: date,
                datasets: [
                    {
                        data: newCases,
                        borderColor: "#3e95cd",
                        borderWidth: 1,
                        fill: false,
                    }
                ]
            },
            options: topLineOptions
        });

        var activeCasesLine = document.getElementById('activeCasesLine').getContext('2d');
        new Chart(activeCasesLine, {
            type: 'line',
            data: {
                labels: date,
                datasets: [
                    {
                        data: newCases,
                        borderColor: "#3e95cd",
                        borderWidth: 1,
                        fill: false,
                    }
                ]
            },
            options: topLineOptions
        });

        var deceasedCasesLine = document.getElementById('deceasedCasesLine').getContext('2d');
        new Chart(deceasedCasesLine, {
            type: 'line',
            data: {
                labels: date,
                datasets: [
                    {
                        data: newDeaths,
                        borderColor: "#3e95cd",
                        borderWidth: 1,
                        fill: false,
                    }
                ]
            },
            options: topLineOptions
        });

        var dischargedCasesLine = document.getElementById('dischargedCasesLine').getContext('2d');
        new Chart(dischargedCasesLine, {
            type: 'line',
            data: {
                labels: date,
                datasets: [
                    {
                        data: totalDeaths,
                        borderColor: "#3e95cd",
                        borderWidth: 1,
                        fill: false,
                    }
                ]
            },
            options: topLineOptions
        });

        var summaryCasesLine = document.getElementById('summaryCasesLine').getContext('2d');
        new Chart(summaryCasesLine, {
            type: 'bar',
            data: {
                datasets: [{
                    label: 'New Cases',
                    data: newCases,
                    // this dataset is drawn below
                    order: 1,
                    backgroundColor: "#de4545",
                }, {
                    label: 'Stringency Index',
                    data: stringencyIndex,
                    type: 'line',
                    // this dataset is drawn on top
                    order: 2,
                    borderColor: "#3e95cd",
                    borderWidth: 3,
                    fill: false,
                }],
                labels: date
            },
            options: {
                maintainAspectRatio: false,
                elements: {
                    point: {
                        radius: 0
                    }
                },
                title: {
                    display: true,
                    text: 'Control Effectiveness',
                    fontSize: 20
                },
            }
        });

        var breakdownCasesLine = document.getElementById('breakdownCasesLine').getContext('2d');
        new Chart(breakdownCasesLine, {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [5381, 38500, 1, 26],
                    backgroundColor: ["#57c6eb", "#94ed58", "#e65353", "#706c6c"],
                }],

                // These labels appear in the legend and in the tooltips when hovering different arcs
                labels: [
                    'Active',
                    'Recovered',
                    'Critical',
                    'Deceased'
                ]
            },
            options: {
                maintainAspectRatio: false,
                rotation: 10,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                },
                pieceLabel: {
                    render: 'label',
                    arc: true,
                    fontColor: '#000',
                    position: 'outside'
                },
                responsive: true,
                legend: {
                    position: 'bottom',
                },
                title: {
                    display: true,
                    text: 'Breakdown',
                    fontSize: 20
                },
                animation: {
                    animateScale: true,
                    animateRotate: true
                },
                scales: {
                    xAxes: [{
                        ticks: {
                            display: false,
                        },
                        gridLines: {
                            display: false,
                            drawBorder: false
                        },
                    }],
                    yAxes: [{
                        gridLines: {
                            display: false,
                            drawBorder: false
                        },
                        ticks: {
                            display: false,
                        },
                    }]
                }
            }
        });
    }
};
xmlhttp.open("GET", "../Simple_Dashboard/data/coviddata.csv", true);
xmlhttp.send();