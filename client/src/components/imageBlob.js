import React from 'react'

function imageBlob () {

    const handleChange=(e)=> {
    console.log(e.target.files)
    }
  return (
    <div>
      <input type="file" onChange={handleChange}/>
    </div>
  )
}

export default imageBlob
