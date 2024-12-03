import html2canvas from 'html2canvas';

export function generateChartData(data) {
  const labels = Object.keys(data);
  const values = Object.values(data);

  const chartData = {
    labels,
    datasets: [
      {
        label: 'Surface Chloride Concentration Over Time',
        backgroundColor: '#c400a7',
        borderWidth: 1,
        borderColor: '#660057',
        pointRadius: 2.5,
        pointBackgroundColor: '#777B7E',
        pointBorderColor: 'transparent',
        data: values,
      },
    ],
  };

  const chartOptions = {
    scales: {
      x: {
        title: {
          display: true,
          text: 'Year',
        },
      },
      y: {
        title: {
          display: true,
          text: 'Chloride Concentration (kg/m^3)',
        },
      },
    },
  };

  return { chartData, chartOptions };
}

export function downloadData(data, longitude, latitude, componentType, saltApplicationRate) {
  const rows = Object.keys(data).map(key => [key, data[key]]);
  const csvContent = 'data:text/csv;charset=utf-8,' + rows.map(e => e.join(',')).join('\n');

  const fileName = `(${longitude}, ${latitude}), ${componentType}, ${saltApplicationRate} rate.csv`;
  const downloadAnchorNode = document.createElement('a');
  downloadAnchorNode.setAttribute('href', encodeURI(csvContent));
  downloadAnchorNode.setAttribute('download', fileName);
  document.body.appendChild(downloadAnchorNode);
  downloadAnchorNode.click();
  downloadAnchorNode.remove();
}

export function downloadJPG(chartWrapper, longitude, latitude, componentType, saltApplicationRate) {
  const fileName = `(${longitude}, ${latitude}), ${componentType}, ${saltApplicationRate} rate.jpg`;

  if (chartWrapper) {
    html2canvas(chartWrapper)
      .then(canvas => {
        const imgData = canvas.toDataURL('image/jpeg');
        const link = document.createElement('a');
        link.href = imgData;
        link.download = fileName;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      })
      .catch(error => {
        console.error('Error capturing chart:', error);
      });
  } else {
    console.error('chartWrapper is not defined');
  }
}