String.prototype.toDateFormDatetime = function () {
    var parts = this.split(/[-T:Z]/);
    return parts;
    //return new Date(parts[0], parts[1] - 1 , parts[2], parts[3], parts[4], parts[5]);
};