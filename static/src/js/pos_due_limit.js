odoo.define('due_limit.POSDueLimit', function (require) {
    'use strict';

    var models = require('point_of_sale.models');
    models.load_fields('res.partner', 'pos_due_limit');

    const ProductScreen = require('point_of_sale.ProductScreen')
    const Registries = require('point_of_sale.Registries');
    var rpc =require('web.rpc');

    const POSDueLimit = (ProductScreen) =>
    class extends ProductScreen{
    async _onClickPay() {
    var self = this;
    var flag = 0;
    const currentClient = this.currentOrder.get_client();
            await rpc.query({
                model: 'res.partner',
                method: 'find_due_limit',
                args: [,currentClient.id],
            }).then(function (data) {
            if(data > currentClient.pos_due_limit){
            flag=0;
            }
            else{
            flag=1;
            }
        });
        if(flag==0){
                this.showPopup('ConfirmPopup', {
          title: this.env._t('Due Limit Exceeded'),
          body: this.env._t('Customer Have No Access To Purchase'),
                    });
        }
        else if(flag==1){
                        await super._onClickPay();

        }
    }
    }
    Registries.Component.extend(ProductScreen,POSDueLimit);
    return ProductScreen;
    })
    //console.log("ABCD")
