import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/',
    component: ComponentCreator('/', '540'),
    routes: [
      {
        path: '/',
        component: ComponentCreator('/', 'cde'),
        routes: [
          {
            path: '/',
            component: ComponentCreator('/', 'cd7'),
            routes: [
              {
                path: '/humanoid-basics',
                component: ComponentCreator('/humanoid-basics', '641'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/intro',
                component: ComponentCreator('/intro', '9fa'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/movement-dynamics',
                component: ComponentCreator('/movement-dynamics', '55a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-systems',
                component: ComponentCreator('/physical-systems', '4fb'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/programming-core',
                component: ComponentCreator('/programming-core', '9e8'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/robot-ai-integration',
                component: ComponentCreator('/robot-ai-integration', '7e0'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
