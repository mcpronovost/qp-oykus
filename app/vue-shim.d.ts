import { qpFilters } from "./src/plugins/filters";

declare module "*.vue"
declare module "*.js"
declare module "*.json"

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $f: qpFilters;
  }
}
