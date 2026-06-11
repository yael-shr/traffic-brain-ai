import json
import time
import random 

def calculate_best_phase(lane_loads):
    
    phase_scores = {
        1: lane_loads[0] + lane_loads[1],  # צפון-דרום ישר
        2: lane_loads[2] + lane_loads[3],  # מזרח-מערב ישר
        3: lane_loads[4] + lane_loads[5],  # צפון-דרום שמאלה
        4: lane_loads[6] + lane_loads[7]   # מזרח-מערב שמאלה
    }
    
    best_phase = max(phase_scores, key=phase_scores.get)
    return best_phase

def update_traffic_file(phase_id):
    
    data = {
        "selected_phase": phase_id,
        "timestamp": int(time.time())
    }
    
    with open("traffic_data.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"[AI Brain] Selected Phase {phase_id}. Saved to JSON.")

if __name__ == "__main__":
    print("Starting Continuous Traffic Brain AI Engine... (Press Ctrl+C to stop)")
    
    try:
        while True:
            simulated_lane_loads = [random.randint(0, 20) for _ in range(8)]
            
            print(f"\nCurrent Lane Loads (0-7): {simulated_lane_loads}")
            
            chosen_phase = calculate_best_phase(simulated_lane_loads)
            update_traffic_file(chosen_phase)
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nTraffic Brain AI Engine stopped by user.")