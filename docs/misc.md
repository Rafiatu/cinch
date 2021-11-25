## Docker compose bind mounts

Bind mount make sensewhen what's on the host is expected to overwrite what is in the container and not the other way round

## Docker compose bind mounts environment variables

Though some environment variables (ex. `DEBUG`, `SECRET_KEY` etc) have default values assigned to then in the codes making it unnecessary for us to declared here. However it is important we explicitly declare them here so we know all the required environment variables as we do not have anything like for instance env.sample

## Other Services

For the other services namely `notification`, `payment` and `dspa`, the approach to take in ensuring replacability and maintainability will be discuss when implementations requires them.

## Move commits to production repository

The `cinch-api-dev` respository on the `Decadevs` organization is suppose to be the development codebase where developers work and host to a staging Heroku application. However, codes here are not deployed directly to a production server which may or may not be yet setup.

There is another respository named `cinch-api` on the `DecagonHQ` organization where we are suppose to mode lastest codes from `cinch-api-dev` to before actual deployment to production server.

Moving these codes is currently done manually and locally following the below steps
- Ensure `cinch-api-dev` has been added a remote repo as `dev-origin` on the `cinch-api` local repo
- Ensure to be on the master branch on the `cinch-api` repo
- Run `$ git pull dev-origin main` to pull in latest changes from `cinch-api-dev`
- Then run `$ git push`
- Ensure commit histories are aligned between these repositories, otherwise, there will be conflicts
