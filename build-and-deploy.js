const { exec } = require('child_process');
const { exit } = require('process');
const registry = 'longmont.iguzman.com.mx:5000';
const name = 'flowers-store-api';
let branch = '';

const getBranchName = () => {
  return new Promise((res, rej) => {
    exec('git branch --show-current', (err, stdout) => {
      if (err) return rej(err);
      res(stdout.toString());
    });
  });
};

const tagDockerImage = () => {
  return new Promise((res, rej) => {
    console.log('\n========= Tagging Docker Image =========');
    getBranchName()
      .then((data) => {
        branch = data;
        exec(`docker tag ${name} ${registry}/${name}:${branch}`, (err, stdout) => {
          if (err) return rej(err);
          console.log('\nDocker Image tagged!');
          res(stdout);
        });
      })
      .catch((err) => {
        console.log('\nBuild Docker image error:', err);
      });
  });
};

const publishDockerImage = () => {
  return new Promise((res, rej) => {
    console.log('\n========= Publishing Docker Image =========');
    getBranchName()
      .then((branch) => {
        exec(`docker push ${registry}/${name}:${branch}`, (err, stdout) => {
          if (err) return rej(err);
          console.log('\nDocker Image published!');
          res(stdout);
        });
      })
      .catch((err) => {
        console.log('\nBuild Docker image error:', err);
      });
  });
};

const buildDockerImage = () => {
  return new Promise((res, rej) => {
    console.log('\n========= Building Docker Image =========');
    exec(`docker build -t ${name} .`, (err, stdout) => {
      if (err) return rej(err);
      console.log('\nDocker Image built');
      res(stdout);
    });
  });
};

buildDockerImage()
  .then(() => {
    tagDockerImage()
      .then(() => {
        publishDockerImage()
          .then(() => {
            console.log('\nProcess complete!');
            console.log(`\nImage: ${registry}/${name}:${branch}`);
            exit(1);
          })
          .catch((err) => {
            console.log('\Publishing Docker image error:', err);
            exit(1);
          });
      })
      .catch((err) => {
        console.log('\nTagging Docker image error:', err);
        exit(1);
      });
  })
  .catch((err) => {
    console.log('\nBuild Docker image error:', err);
    exit(1);
  });
