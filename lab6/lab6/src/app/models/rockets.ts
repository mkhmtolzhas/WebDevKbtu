export interface Rocket {
    id: number;
    active: boolean;
    stages: number;
    boosters: number;
    cost_per_launch: number;
    success_rate_pct: number;
    first_flight: string;
    country: string;
    company: string;
    height: {
        meters: number;
        feet: number;
    };
    diameter: {
        meters: number;
        feet: number;
    };
    mass: {
        kg: number;
        lb: number;
    }
    payload_weights: [
        {
            id: string;
            name: string;
            kg: number;
            lb: number;
        }
    ]
    first_stage: {
        reusable: boolean;
        engines: number;
        fuel_amount_tons: number;
        burn_time_sec: number;
        thrust_sea_level: {
            kN: number;
            lbf: number;
        };
        thrust_vacuum: {
            kN: number;
            lbf: number;
        };
    };
    wikipedia: string;
    description: string;
    rocket_id: string;
    rocket_name: string;
    rocket_type: string;
}
