$(function () {
    countFalg = 0
    echarts_1();
    echarts_2();
    echarts_3();
    echarts_4();
    echarts_5();

    // top10
    function echarts_1() {
        var myChart = echarts.init(document.getElementById('echart1'));

        option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            grid: {
                right: '3%',
                top: '3%',
            },
            yAxis: {
                type: 'value',
                boundaryGap: [0, 0.01],
                axisLine: {
                    lineStyle: {
                        color: '#ffffff',
                    }

                },
                axisLabel: {
                    formatter: '{value} 万',

                },
            },
            xAxis: {
                type: 'category',
                axisLabel: {interval: 0, rotate: 30},
                data: [],
                axisLine: {
                    lineStyle: {
                        color: '#ffffff',
                    }

                }

            },
            series: [
                {
                    name: '播放次数最多',
                    type: 'bar',
                    data: [],
                    itemStyle: {color: '#50578b'},
                }
            ]
        };

        $.ajax({
            url: 'http://127.0.0.1:8080/get_max_play',
            type: 'GET',
            dataType: 'json',
            async: true,
            success: function (data) {
                myChart.setOption({
                    xAxis: {
                        data: data.name
                    },
                    series: [{
                        data: data.value
                    }
                    ]
                });
            },

        });


        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option, true);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
        countFalg++;
    }
    // 每个月创建歌单的数量
    function echarts_2() {
        var myChart = echarts.init(document.getElementById('echart2'));
        option = {
            tooltip: {
                axisPointer: {type: 'shadow'},
            },

            grid: {
                left: '1%',
                right: '3%',
                top: '3%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: [],
                axisLabel: {
                    fontSize: 13
                },
                axisLine: {
                    lineStyle: {
                        color: '#ffffff',
                    }

                },

            },
            yAxis: {
                type: 'value',
                axisLabel: {
                    fontSize: 13,
                },
                axisLine: {
                    lineStyle: {
                        color: '#ffffff',
                    }

                }
            },
            series: [
                {
                    data: [],
                    type: 'line',
                    areaStyle: {color: '#50578b'},
                    smooth: true,
                }
            ]
        };
        console.log(option.xAxis);
        console.log(option.xAxis[0]);
        $.ajax({
            url: 'http://127.0.0.1:8080/get_per_create',
            type: 'GET',
            dataType: 'json',
            async: true,
            success: function (data) {
                console.log(data);
                myChart.setOption({
                    xAxis: {
                        data: data.data
                    },
                    series: [{
                        data: data.value
                    }
                    ]
                })
            }
        });
        myChart.setOption(option, true);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
        countFalg++;
    }
    // 评论和转发量的结合图
    function echarts_3() {
        var myChart = echarts.init(document.getElementById('echart3'));
        option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    crossStyle: {
                        color: '#999'
                    }
                }
            },
            legend: {
                data: ['评论数', '转发量'],
                textStyle: {
                    color: '#ffffff',
                    fontSize: 16,
                }
            },
            xAxis: [
                {
                    type: 'category',
                    data: [],
                    axisPointer: {
                        type: 'shadow'
                    },
                    axisLabel: {interval: 5, rotate: 30, fontSize: 13},
                    axisLine: {
                        lineStyle: {
                            color: '#ffffff',
                        }

                    }
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    name: '评论数',
                    min: 0,
                    max: 2000,
                    interval: 200,
                    axisLabel: {
                        formatter: '{value} ',

                    },
                    axisLine: {
                        lineStyle: {
                            color: '#ffffff',
                        }

                    }
                },
                {
                    type: 'value',
                    name: '转发量',
                    min: 0,
                    max: 5000,
                    interval: 500,
                    axisLabel: {
                        formatter: '{value} ',

                    },
                    axisLine: {
                        lineStyle: {
                            color: '#ffffff',
                        }

                    }
                }
            ],
            series: [
                {
                    name: '评论数',
                    type: 'bar',
                    data: [],
                },
                {
                    name: '转发量',
                    type: 'line',
                    yAxisIndex: 1,
                    data: []
                }
            ]
        };

        $.ajax({
            url: 'http://127.0.0.1:8080/get_stack_img',
            type: 'GET',
            dataType: 'json',
            async: true,
            success: function (data) {

                myChart.setOption({
                    xAxis: {
                        data: data.zuhe_name
                    },
                    series: [{
                        data: data.pinglun_value
                    },
                        {
                            data: data.transfrom_value
                        }

                    ]
                })

            }
        });
        myChart.setOption(option);
        window.onresize = function () {
            myChart.resize();
        };
        countFalg++;

    }
    //饼图
    function echarts_4()  {
        var myChart = echarts.init(document.getElementById('echart4'));
        console.log(myChart)
        option = {
            tooltip: {
                trigger: 'item'
              },
              series: [
                {
                  type: 'pie',
                  radius: ['0%', '67%'],
                  center: ['52%', '55%'],
                  avoidLabelOverlap: false,
                    itemStyle: {
                    borderRadius: 10,
                    borderWidth: 2
                  },

                  emphasis: {
                    label: {
                      show: true,
                      fontSize: '60',
                      fontWeight: 'bold',
                        color:'#fff',
                    }
                  },
                  data: []
                }
              ]
        };
        $.ajax({
            url: 'http://127.0.0.1:8080/get_rose',
            type: 'GET',
            dataType: 'json',
            async: true,
            success: function (data) {
                myChart.setOption({
                    series: [{
                        data: data.return_data
                    }
                    ]
                })
            }
        });
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
        countFalg++;
    }
    //词云图
    function echarts_5() {
        var data = []
        var myChart = echarts.init(document.getElementById('wordCloud'));
        var maskImage = new Image();
        image1 = "data:image/png;base64,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"
        $.ajax({
            url: 'http://127.0.0.1:8080/get_max_author',
            type: 'GET',
            dataType: 'json',
            async: true,
            success: function (data) {
                myChart.setOption({
                    series: [{
                        data: data.data
                    }
                    ]
                });

            }
        });

        maskImage.src = image1
        var option = {
            tooltip: {

                axisPointer: {type: 'shadow'}
            },
            series: [{
                type: 'wordCloud',
                sizeRange: [10, 50],
                rotationRange: [45, 30],
                gridSize: 2,
                shape: 'square',
                drawOutOfBound: false,
                textStyle: {
                    fontWeight: 'bold',
                    color: function () {
                        return 'rgb(' + [
                            Math.round(Math.random() * 100) + 150,
                            Math.round(Math.random() * 100) + 150,
                            Math.round(Math.random() * 100) + 150
                        ].join(',') + ')';
                    }
                },
                emphasis: {
                    textStyle: {
                        color: '#528'
                    }
                },
                data: [],
            }]
        };
        maskImage.onload = function () {
            myChart.setOption(option);
        }
        window.onresize = function () {
            myChart.resize();
        }
        countFalg++;

    }

    // 获得总的转发量 总的歌曲数 等等
    $.ajax({
        url: 'http://127.0.0.1:8080/get_all_num',
        type: 'GET',
        dataType: 'json',
        async: true,
        success: function (data) {
            console.log(data);
            $(function () {
                $(".count_shouchang").numberRock({
                    lastNumber:data.all_shouchang_num,
                    duration: 5000,
                    easing: 'swing',
                });
                $(".count_transform").numberRock({
                    lastNumber: data.all_transform_num,
                    duration: 5000,
                    easing: 'swing',
                });
                $(".count_pinglun").numberRock({
                    lastNumber: data.all_pinglun_num,
                    duration: 5000,
                    easing: 'swing',
                });
                $(".count_music").numberRock({
                    lastNumber: data.all_music_num,
                    duration: 5000,
                    easing: 'swing',
                });
            });

        }
    });
    // 5个模块都请求成功后全部加载完毕，清除记载动画
    document.getElementById('countFlag').innerText = countFalg;
})



		
		
		


		









