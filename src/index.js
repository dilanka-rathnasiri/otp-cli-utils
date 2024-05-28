#!/usr/bin/env node

const {program} = require("commander")

program.command("greet <name>")
.action((name) => {
  console.log(`Hello ${name}!`)
})

program.parse()
