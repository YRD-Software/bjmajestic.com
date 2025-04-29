import { withPayload } from '@payloadcms/next/withPayload'

import redirects from './redirects.js'

const NEXT_PUBLIC_SERVER_URL = process.env.VERCEL_PROJECT_PRODUCTION_URL
  ? `https://${process.env.VERCEL_PROJECT_PRODUCTION_URL}`
  : undefined || process.env.NEXT_PUBLIC_SERVER_URL || 'http://localhost:3000'

/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      ...[NEXT_PUBLIC_SERVER_URL /* 'https://example.com' */].map((item) => {
        const url = new URL(item)

        return {
          hostname: url.hostname,
          protocol: url.protocol.replace(':', ''),
        }
      }),
    ],
  },
  reactStrictMode: true,
  redirects,
  webpack: (config, { isServer }) => {
    if (isServer) {
      // Add 'pg-cloudflare' to serverComponentsExternalPackages
      config.externals = [...(config.externals || []), 'pg-cloudflare'];
    }
    
    // Add a fallback for the cloudflare:sockets scheme
    config.resolve.fallback = {
      ...config.resolve.fallback,
      'cloudflare:sockets': false,
    };
    
    return config;
  },
  // Add pg-native to transpilePackages to prevent build issues
  transpilePackages: ['pg', 'pg-cloudflare'],
}

export default withPayload(nextConfig)
