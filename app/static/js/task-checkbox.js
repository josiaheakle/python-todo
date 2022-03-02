const onCheckboxClick = async (checkbox) => {
    console.log(`clicked`)
    let strs = checkbox.id.split('-')
    const checkboxId = strs[strs.length - 1]
    let updated = await fetch("/complete-task", {
        headers: {
            'Content-Type': 'application/json'  
        },
        method: "post",
        body: JSON.stringify({checkboxId})
    })
    
    updated = updated.json()
    console.log({updated});
}