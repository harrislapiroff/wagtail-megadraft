import React from 'react'
import ReactDOM from 'react-dom'

import MegadraftController from './MegadraftController'

export default function initEditor(selector, options, currentScript) {
    // document.currentScript is not available in IE11. Use a fallback instead.
    const context = currentScript ? currentScript.parentNode : document.body
    // If the field is not in the current context, look for it in the whole body.
    const field = context.querySelector(selector) || document.body.querySelector(selector)

    const editorWrapper = document.createElement('div')
    editorWrapper.className = 'megadraft-editor__wrapper'

    field.parentNode.appendChild(editorWrapper)

    const changeHandler = (editorState) => {
        field.value = editorState;
    }

    const editor = (
        <MegadraftController
            initialState={JSON.parse(field.value)}
            onChange={changeHandler}
        />
    )

    ReactDOM.render(editor, editorWrapper)
}
