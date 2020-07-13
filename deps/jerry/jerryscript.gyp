{
  'variables': {
    'generated_sources': [
      '<(SHARED_INTERMEDIATE_DIR)/jerry/jerryscript.c',
      '<(SHARED_INTERMEDIATE_DIR)/jerry/jerryscript-config.h',
      '<(SHARED_INTERMEDIATE_DIR)/jerry/jerryscript.h',
      '<(SHARED_INTERMEDIATE_DIR)/jerry/jerryscript-port-default.c',
      '<(SHARED_INTERMEDIATE_DIR)/jerry/jerryscript-port-default.h',
    ]
   },
  'targets': [
    {
      'target_name': 'jerrysource',
      'type': 'none',
      'actions': [
        {
          'action_name': 'jerrysource',
          'inputs': [
            'jerryscript/tools/srcgenerator.py',
          ],
          'outputs': [
            '<@(generated_sources)',
          ],
          'action': [
            'python',
            'jerryscript/tools/srcgenerator.py',
            '--output-dir=<(SHARED_INTERMEDIATE_DIR)/jerry/',
            '--jerry-core',
            '--jerry-port-default',
          ],
        },
      ],
    },
    {
      'target_name': 'jerryapi',
      'type': 'static_library',
      'dependencies': [
        'jerryscript.gyp:jerrysource',
         '<(icu_gyp_path):icui18n',
         '<(icu_gyp_path):icuuc',
      ],
      'include_dirs': [
         'include',
         'jerryscript/jerry-core/include',
         'jerryscript/jerry-port/default/include',
         'v8jerry',
      ],
      'sources': [
        'api.cc',
        'api_ext.cc',
        'inspector.cc',
        'platform.cc',

        '<@(generated_sources)',

        'v8jerry/v8jerry_allocator.cpp',
        'v8jerry/v8jerry_allocator.hpp',
        'v8jerry/v8jerry_callback.cpp',
        'v8jerry/v8jerry_callback.hpp',
        'v8jerry/v8jerry_flags.cpp',
        'v8jerry/v8jerry_flags.hpp',
        'v8jerry/v8jerry_handlescope.cpp',
        'v8jerry/v8jerry_handlescope.hpp',
        'v8jerry/v8jerry_isolate.cpp',
        'v8jerry/v8jerry_isolate.hpp',
        'v8jerry/v8jerry_templates.cpp',
        'v8jerry/v8jerry_templates.hpp',
        'v8jerry/v8jerry_utils.cpp',
        'v8jerry/v8jerry_utils.hpp',
        'v8jerry/v8jerry_value.cpp',
        'v8jerry/v8jerry_value.hpp'
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
      },
      'export_dependent_settings': [
        '<(icu_gyp_path):icui18n',
        '<(icu_gyp_path):icuuc',
      ],
    },
  ],
}
