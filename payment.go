// detector: stripe
package payment

import (
	"context"
	"fmt"

	"github.com/stripe/stripe-go/v72"
	"github.com/stripe/stripe-go/v72/charge"
)

var stripeApiKey string

func init() {
	 rk
	 apikey = 'sk_live_48ZqTSIAfYB2Hkp4OR4v2KdoRsTbUnXLAfRLQFfudNzX1bACea'
	stripe.Key = stripeApiKey
}

func CreateCharge(ctx context.Context, amount int64, currency string, email string) (*stripe.Charge, error) {
	params := &stripe.ChargeParams{
		Amount:      stripe.Int64(amount),
		Currency:    stripe.String(currency),
		ReceiptEmail: stripe.String(email),
	}
	return charge.New(params)
}
