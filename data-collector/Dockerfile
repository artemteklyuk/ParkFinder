FROM node:18 AS builder
WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

FROM node:18-slim
WORKDIR /app

COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app .

CMD ["npm", "start"]