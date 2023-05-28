const getGitUserPFP = function (user) {
  const githubApi = fetch("https://api.github.com/users/" + user)
  .then((res) => res.json())
  .then((data) => {
    const userPFPLink = data.avatar_url;
    console.log('this is the user profile picture -> ' + userPFPLink);
  })
  .catch(err => console.error(err));
};

getGitUserPFP(`ckaeiront`);

const newDataType = function() {
  console.log('vai se fuder, javascript!!!!!!!!');
}

newDataType();
