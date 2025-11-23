# NestJS project structure
the following is the basic nodeJS project structure:

```bash
.
├── eslint.config.mjs
├── nest-cli.json
├── node_modules/
├── package.json
├── package-lock.json
├── src/
├── test/
├── tsconfig.build.json
└── tsconfig.json
```

## Comparing structure with Spring application
### POM
`package.json` is like the POM, it defines the dependencies of the project.
It also include some basic scripts like `start, build, test`.
`package-lock.json` lock the dependencies in a specific version
### Compilation
`tsconfig.json` is used to define typescript configurations.
`tsconfig.build.json` is used specifically for the Compilation.
### application.properties
`nest-cli.json` is the same as `application.properties` of a Spring application.
### code quality
`eslint.config.mjs` is used to check the code quality
### .m2/repository
`node_modules/` is the directory that contains all the installed dependencies like the `.m2/repository` of Spring but local in the directory.
### src and test
The main code and the tests.
## Comparing decorators with Spring application
In the `app.module.ts` are defined some decorators that are conceptually similar to spring ones.

``` typescript
@Module({
  controllers: [UsersController],
  providers: [UsersService],
  exports: [UsersService],
})
```
```
```

`controllers`: `@RestController` HTTP request handlers.
`providers`: `@Service|@Repository|@Component` contains the logic of the application.
`exports`: `@Bean` shared the function that the component providers with the others.
