import hysysopt
from costing import column_cost_function, hx_cost_function

opt = hysysopt.init()

opt.get_params('opt')

opt.optimize_feed_location("Your column name", "Your feed stream name", lb_frac=0, ub_frac=1)

opt.list_params()

opt.attach_cost_function(column_cost_function, optype="columns")
opt.attach_cost_function(hx_cost_function, optype="heatexchangers")

opt.set_column_efficiency("Your column name", 0.7)

opt.display_convergence = True
opt.set_save_location('saved_data.csv')
opt.run(n_iter=20, num=20, save_data=True)

opt.set_to_optimal()
opt.show_individual_costs()
