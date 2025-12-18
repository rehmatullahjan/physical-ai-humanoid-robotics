const prism = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI: Humanoid Robotics',
  tagline: 'Learn humanoid robotics from scratch',
  url: 'https://physical-ai-humanoid-robotics.vercel.app', // Will be updated with your actual Vercel URL
  baseUrl: '/',
  organizationName: 'rehmatullahjan',
  projectName: 'physical-ai-humanoid-robotics',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // routeBasePath: '/', // Removed to allow landing page at / and docs at /docs
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Physical AI Robotics',
        logo: {
          alt: 'Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            to: '/docs/intro', // Changed from href localhost to relative link
            label: 'API',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Built for GIAIC Hackathon`,
      },
      prism: {
        theme: prism.themes.dracula,
      },
    }),
};

module.exports = config;
