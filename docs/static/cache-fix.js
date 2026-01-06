if (!location.search) location.replace("?" + Date.now());
else history.replaceState(null, "", location.href.replace(location.search, ""));
