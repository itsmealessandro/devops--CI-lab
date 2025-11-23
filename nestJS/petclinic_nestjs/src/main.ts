import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';

async function bootstrap() {
  // To create the app
  const app = await NestFactory.create(AppModule);

  // NOTE: configuration for Swagger
  const config = new DocumentBuilder()
    .setTitle('Pet clinic example')
    .setDescription('REST API for a pet clinic')
    .setVersion('1.0')
    .addTag('pets')
    .build()

  // the next lines can be summerized like this:
  // SwaggerModule.setup('api', app, SwaggerModule.createDocument(app, config))
  // this approach reduce the system overhead and some modules can dinamucally coll it again to change it.
  // The factory method is used specifically to generate the Swagger document when you request it.
  const documentFactory = () => SwaggerModule.createDocument(app, config) // store a function in documentFactory
  // This method setups the swagger docs in the specified PATH
  const SWAGGER_DOCS_PATH = "api"
  SwaggerModule.setup(SWAGGER_DOCS_PATH, app, documentFactory)

  // To starts the application
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
