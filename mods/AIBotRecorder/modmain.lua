local json = GLOBAL.json
local function save_replay(state, action)
    local data = {timestamp = os.date(), state = state, action = action}
    local file = io.open("replays/replay.json", "a")
    file:write(json.encode(data) .. "
")
    file:close()
end

AddPlayerPostInit(function(player)
    player:ListenForEvent("performaction", function(inst, data)
        local state = {
            time = GLOBAL.TheWorld.state.phase,
            inventory = player.components.inventory:GetItems(),
            nearby = GLOBAL.TheSim:FindEntities(player.Transform:GetWorldPosition(), 10)
        }
        local action = {type = data.action, target = data.target}
        save_replay(state, action)
    end)
end)
