

exports.getEmoji = async (req, res) => {
    res.set('Content-Type', 'application/json');

    // gets
    searchStr = req.query.search;

    emoji = null;
    res.status(200).send(JSON.stringify(emoji));
};