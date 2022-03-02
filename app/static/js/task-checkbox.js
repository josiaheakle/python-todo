const onCheckboxClick = async (checkbox) => {
    let strs = checkbox.id.split('-')
    const checkboxId = strs[strs.length - 1]
    await fetch("/complete-task", {
        headers: {
            'Content-Type': 'application/json'  
        },
        method: "post",
        body: JSON.stringify({checkboxId})
    })
}