import React, { useState, Fragment } from 'react'

import { MegadraftEditor, editorStateFromRaw, editorStateToJSON } from 'megadraft'
import 'megadraft/lib/styles/megadraft.scss'

export default function MegadraftController({ initialState, onChange }) {

    let initialStateLazy = () => {
        try {
            console.log(initialState)
            return { editorState: editorStateFromRaw(initialState) }
        } catch {
            // TODO: Provide a raw JSON editor instead of clearing the field
            return { editorState: editorStateFromRaw(null) }
        }
    }

    const [state, setState] = useState(initialStateLazy)

    const changeHandler = (newEditorState) => {
        // Update the internally stored editor state
        setState({ ...state, editorState: newEditorState })
        // Bubble up the new editor state as saveable JSON
        onChange(editorStateToJSON(newEditorState))
    }

    return (
        <MegadraftEditor
            editorState={state.editorState}
            onChange={changeHandler}
        />
    )

}
