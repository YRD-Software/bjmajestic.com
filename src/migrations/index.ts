import * as migration_20250531_032934 from './20250531_032934';
import * as migration_20250930_221219 from './20250930_221219';

export const migrations = [
  {
    up: migration_20250531_032934.up,
    down: migration_20250531_032934.down,
    name: '20250531_032934',
  },
  {
    up: migration_20250930_221219.up,
    down: migration_20250930_221219.down,
    name: '20250930_221219'
  },
];
