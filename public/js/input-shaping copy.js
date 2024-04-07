var print_speed = document.getElementById('print_speed');
var x_rings = document.getElementById('x_rings');
var x_measure = document.getElementById('x_measure');
var y_rings = document.getElementById('y_rings');
var y_measure = document.getElementById('y_measure');
var x_freq = document.getElementById('x_freq');
var y_freq = document.getElementById('y_freq');

function isRunner() {
    inputShaper();
}

function inputShaper() {

    let ddf_val = ddf.value;
    let bf_val = bf.value;
    let measured_height_val = measured_height.value;

    let dd_pa_val = ddf_val - measured_height_val;
    let b_pa_val = bf_val - measured_height_val;

    dd_pa.value = dd_pa_val;
    b_pa.value = b_pa_val;

    console.log('DD_PA: ', dd_pa_val);
    console.log('B_PA: ', b_pa_val);

}

function copyRd() {
    console.log('Copy');
    let text = rotational_distance;
    const copyContent = async () => {
        try {
            await navigator.clipboard.writeText(text);
            console.log('Content copied to clipboard');
        } catch (err) {
            console.error('Failed to copy: ', err);
        }
    }
}