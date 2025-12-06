module.exports = {
  title: 'Physical AI: Humanoid Robotics',
  tagline: 'Learn humanoid robotics from scratch',
  url: 'https://yourusername.github.io',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
}
  module.exports = {
  // ... all your existing config ...
  themeConfig: {
    // ... navbar, footer config ...
  },
  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {
            from: '/',
            to: '/intro',
          },
        ],
      },
    ],
  ],

    footer: {
      style: 'dark',
      copyright: 'Built for GIAIC Hackathon',
    },
  }