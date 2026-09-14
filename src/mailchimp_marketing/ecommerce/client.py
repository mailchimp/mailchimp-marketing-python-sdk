# This file was auto-generated from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.e_commerce_cart import ECommerceCart
from ..types.e_commerce_cart_line_item import ECommerceCartLineItem
from ..types.e_commerce_customer import ECommerceCustomer
from ..types.e_commerce_order import ECommerceOrder
from ..types.e_commerce_order_line_item import ECommerceOrderLineItem
from ..types.e_commerce_product import ECommerceProduct
from ..types.e_commerce_product_variant import ECommerceProductVariant
from ..types.e_commerce_promo_code import ECommercePromoCode
from ..types.e_commerce_promo_rule import ECommercePromoRule
from ..types.e_commerce_store import ECommerceStore
from ..types.ecommerce_stores_carts_patch import EcommerceStoresCartsPatch
from ..types.ecommerce_stores_carts_patch_address import EcommerceStoresCartsPatchAddress
from ..types.ecommerce_stores_carts_patch_total_spent import EcommerceStoresCartsPatchTotalSpent
from ..types.ecommerce_stores_carts_post import EcommerceStoresCartsPost
from ..types.ecommerce_stores_orders_post import EcommerceStoresOrdersPost
from ..types.ecommerce_stores_orders_post_id import EcommerceStoresOrdersPostId
from ..types.ecommerce_stores_orders_post_images_item import EcommerceStoresOrdersPostImagesItem
from ..types.ecommerce_stores_orders_post_variants_item import EcommerceStoresOrdersPostVariantsItem
from .raw_client import AsyncRawEcommerceClient, RawEcommerceClient
from .types.create_store_cart_ecommerce_request_id import CreateStoreCartEcommerceRequestId
from .types.create_store_cart_ecommerce_request_lines_item import CreateStoreCartEcommerceRequestLinesItem
from .types.create_store_cart_ecommerce_request_order_total import CreateStoreCartEcommerceRequestOrderTotal
from .types.create_store_cart_ecommerce_request_tax_total import CreateStoreCartEcommerceRequestTaxTotal
from .types.create_store_cart_line_ecommerce_request_price import CreateStoreCartLineEcommerceRequestPrice
from .types.create_store_customer_ecommerce_request_address import CreateStoreCustomerEcommerceRequestAddress
from .types.create_store_customer_ecommerce_request_total_spent import CreateStoreCustomerEcommerceRequestTotalSpent
from .types.create_store_ecommerce_request_address import CreateStoreEcommerceRequestAddress
from .types.create_store_order_ecommerce_request_billing_address import CreateStoreOrderEcommerceRequestBillingAddress
from .types.create_store_order_ecommerce_request_cart_id import CreateStoreOrderEcommerceRequestCartId
from .types.create_store_order_ecommerce_request_discount_total import CreateStoreOrderEcommerceRequestDiscountTotal
from .types.create_store_order_ecommerce_request_lines_item import CreateStoreOrderEcommerceRequestLinesItem
from .types.create_store_order_ecommerce_request_order_total import CreateStoreOrderEcommerceRequestOrderTotal
from .types.create_store_order_ecommerce_request_outreach import CreateStoreOrderEcommerceRequestOutreach
from .types.create_store_order_ecommerce_request_promos_item import CreateStoreOrderEcommerceRequestPromosItem
from .types.create_store_order_ecommerce_request_shipping_address import CreateStoreOrderEcommerceRequestShippingAddress
from .types.create_store_order_ecommerce_request_shipping_total import CreateStoreOrderEcommerceRequestShippingTotal
from .types.create_store_order_ecommerce_request_tax_total import CreateStoreOrderEcommerceRequestTaxTotal
from .types.create_store_order_ecommerce_request_tracking_code import CreateStoreOrderEcommerceRequestTrackingCode
from .types.create_store_order_line_ecommerce_request_discount import CreateStoreOrderLineEcommerceRequestDiscount
from .types.create_store_order_line_ecommerce_request_price import CreateStoreOrderLineEcommerceRequestPrice
from .types.create_store_product_image_ecommerce_request_variant_ids_item import (
    CreateStoreProductImageEcommerceRequestVariantIdsItem,
)
from .types.create_store_product_image_ecommerce_response import CreateStoreProductImageEcommerceResponse
from .types.create_store_product_variant_ecommerce_request_id import CreateStoreProductVariantEcommerceRequestId
from .types.create_store_product_variant_ecommerce_request_price import CreateStoreProductVariantEcommerceRequestPrice
from .types.create_store_promo_rule_ecommerce_request_amount import CreateStorePromoRuleEcommerceRequestAmount
from .types.create_store_promo_rule_ecommerce_request_ends_at import CreateStorePromoRuleEcommerceRequestEndsAt
from .types.create_store_promo_rule_ecommerce_request_starts_at import CreateStorePromoRuleEcommerceRequestStartsAt
from .types.create_store_promo_rule_ecommerce_request_target import CreateStorePromoRuleEcommerceRequestTarget
from .types.create_store_promo_rule_ecommerce_request_type import CreateStorePromoRuleEcommerceRequestType
from .types.get_store_product_image_ecommerce_response import GetStoreProductImageEcommerceResponse
from .types.list_ecommerce_response import ListEcommerceResponse
from .types.list_orders_ecommerce_response import ListOrdersEcommerceResponse
from .types.list_store_cart_lines_ecommerce_response import ListStoreCartLinesEcommerceResponse
from .types.list_store_carts_ecommerce_response import ListStoreCartsEcommerceResponse
from .types.list_store_customers_ecommerce_response import ListStoreCustomersEcommerceResponse
from .types.list_store_order_lines_ecommerce_response import ListStoreOrderLinesEcommerceResponse
from .types.list_store_orders_ecommerce_response import ListStoreOrdersEcommerceResponse
from .types.list_store_product_images_ecommerce_response import ListStoreProductImagesEcommerceResponse
from .types.list_store_product_images_ecommerce_response_images_item import (
    ListStoreProductImagesEcommerceResponseImagesItem,
)
from .types.list_store_product_variants_ecommerce_response import ListStoreProductVariantsEcommerceResponse
from .types.list_store_products_ecommerce_response import ListStoreProductsEcommerceResponse
from .types.list_store_promo_rule_promo_codes_ecommerce_response import ListStorePromoRulePromoCodesEcommerceResponse
from .types.list_store_promo_rules_ecommerce_response import ListStorePromoRulesEcommerceResponse
from .types.list_stores_ecommerce_response import ListStoresEcommerceResponse
from .types.update_store_cart_ecommerce_request_id import UpdateStoreCartEcommerceRequestId
from .types.update_store_cart_ecommerce_request_lines_item import UpdateStoreCartEcommerceRequestLinesItem
from .types.update_store_cart_ecommerce_request_order_total import UpdateStoreCartEcommerceRequestOrderTotal
from .types.update_store_cart_ecommerce_request_tax_total import UpdateStoreCartEcommerceRequestTaxTotal
from .types.update_store_cart_line_ecommerce_request_price import UpdateStoreCartLineEcommerceRequestPrice
from .types.update_store_ecommerce_request_address import UpdateStoreEcommerceRequestAddress
from .types.update_store_order_ecommerce_request_billing_address import UpdateStoreOrderEcommerceRequestBillingAddress
from .types.update_store_order_ecommerce_request_cart_id import UpdateStoreOrderEcommerceRequestCartId
from .types.update_store_order_ecommerce_request_discount_total import UpdateStoreOrderEcommerceRequestDiscountTotal
from .types.update_store_order_ecommerce_request_lines_item import UpdateStoreOrderEcommerceRequestLinesItem
from .types.update_store_order_ecommerce_request_order_total import UpdateStoreOrderEcommerceRequestOrderTotal
from .types.update_store_order_ecommerce_request_outreach import UpdateStoreOrderEcommerceRequestOutreach
from .types.update_store_order_ecommerce_request_promos_item import UpdateStoreOrderEcommerceRequestPromosItem
from .types.update_store_order_ecommerce_request_shipping_address import UpdateStoreOrderEcommerceRequestShippingAddress
from .types.update_store_order_ecommerce_request_shipping_total import UpdateStoreOrderEcommerceRequestShippingTotal
from .types.update_store_order_ecommerce_request_tax_total import UpdateStoreOrderEcommerceRequestTaxTotal
from .types.update_store_order_ecommerce_request_tracking_code import UpdateStoreOrderEcommerceRequestTrackingCode
from .types.update_store_order_line_ecommerce_request_discount import UpdateStoreOrderLineEcommerceRequestDiscount
from .types.update_store_order_line_ecommerce_request_price import UpdateStoreOrderLineEcommerceRequestPrice
from .types.update_store_product_ecommerce_request_id import UpdateStoreProductEcommerceRequestId
from .types.update_store_product_ecommerce_request_images_item import UpdateStoreProductEcommerceRequestImagesItem
from .types.update_store_product_ecommerce_request_variants_item import UpdateStoreProductEcommerceRequestVariantsItem
from .types.update_store_product_image_ecommerce_request_variant_ids_item import (
    UpdateStoreProductImageEcommerceRequestVariantIdsItem,
)
from .types.update_store_product_image_ecommerce_response import UpdateStoreProductImageEcommerceResponse
from .types.update_store_product_variant_ecommerce_request_price import UpdateStoreProductVariantEcommerceRequestPrice
from .types.update_store_promo_rule_ecommerce_request_amount import UpdateStorePromoRuleEcommerceRequestAmount
from .types.update_store_promo_rule_ecommerce_request_ends_at import UpdateStorePromoRuleEcommerceRequestEndsAt
from .types.update_store_promo_rule_ecommerce_request_starts_at import UpdateStorePromoRuleEcommerceRequestStartsAt
from .types.update_store_promo_rule_ecommerce_request_target import UpdateStorePromoRuleEcommerceRequestTarget
from .types.update_store_promo_rule_ecommerce_request_type import UpdateStorePromoRuleEcommerceRequestType
from .types.upsert_store_customer_ecommerce_request_address import UpsertStoreCustomerEcommerceRequestAddress
from .types.upsert_store_customer_ecommerce_request_total_spent import UpsertStoreCustomerEcommerceRequestTotalSpent
from .types.upsert_store_product_ecommerce_request_id import UpsertStoreProductEcommerceRequestId
from .types.upsert_store_product_ecommerce_request_images_item import UpsertStoreProductEcommerceRequestImagesItem
from .types.upsert_store_product_ecommerce_request_variants_item import UpsertStoreProductEcommerceRequestVariantsItem
from .types.upsert_store_product_variant_ecommerce_request_price import UpsertStoreProductVariantEcommerceRequestPrice

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EcommerceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEcommerceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEcommerceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEcommerceClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListEcommerceResponse:
        """
        Get information about the e-commerce endpoint's resources.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEcommerceResponse
            Ecommerce Resource

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def list_orders(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        campaign_id: typing.Optional[str] = None,
        outreach_id: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        has_outreach: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommerceOrder, ListOrdersEcommerceResponse]:
        """
        Get information about an account's orders.

        Parameters
        ----------
        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        campaign_id : typing.Optional[str]
            Restrict results to orders with a specific `campaign_id` value.

        outreach_id : typing.Optional[str]
            Restrict results to orders with a specific `outreach_id` value.

        customer_id : typing.Optional[str]
            Restrict results to orders made by a specific customer.

        has_outreach : typing.Optional[bool]
            Restrict results to orders that have an outreach attached. For example, an email campaign or Facebook ad.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommerceOrder, ListOrdersEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_orders()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_orders(
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            campaign_id=campaign_id,
            outreach_id=outreach_id,
            customer_id=customer_id,
            has_outreach=has_outreach,
            request_options=request_options,
        )

    def list_stores(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommerceStore, ListStoresEcommerceResponse]:
        """
        Get information about all stores in the account.

        Parameters
        ----------
        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommerceStore, ListStoresEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_stores()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_stores(
            fields=fields, exclude_fields=exclude_fields, count=count, offset=offset, request_options=request_options
        )

    def create_store(
        self,
        *,
        currency_code: str,
        id: str,
        list_id: str,
        name: str,
        address: typing.Optional[CreateStoreEcommerceRequestAddress] = OMIT,
        domain: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        is_syncing: typing.Optional[bool] = OMIT,
        money_format: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        primary_locale: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceStore:
        """
        Add a new store to your Mailchimp account.

        Parameters
        ----------
        currency_code : str
            The three-letter ISO 4217 code for the currency that the store accepts.

        id : str
            The unique identifier for the store.

        list_id : str
            The unique identifier for the list associated with the store. The `list_id` for a specific store cannot change.

        name : str
            The name of the store.

        address : typing.Optional[CreateStoreEcommerceRequestAddress]
            The store address.

        domain : typing.Optional[str]
            The store domain. This parameter is required for Connected Sites and Google Ads.

        email_address : typing.Optional[str]
            The email address for the store.

        is_syncing : typing.Optional[bool]
            Whether to disable automations because the store is currently [syncing](https://mailchimp.com/developer/marketing/docs/e-commerce/#pausing-store-automations).

        money_format : typing.Optional[str]
            The currency format for the store. For example: `$`, `£`, etc.

        phone : typing.Optional[str]
            The store phone number.

        platform : typing.Optional[str]
            The e-commerce platform of the store.

        primary_locale : typing.Optional[str]
            The primary locale for the store. For example: `en`, `de`, etc.

        timezone : typing.Optional[str]
            The timezone for the store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceStore


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store(
            currency_code="USD",
            id="example_store",
            list_id="1a2df69511",
            name="Freddie's Cat Hat Emporium",
        )
        """
        _response = self._raw_client.create_store(
            currency_code=currency_code,
            id=id,
            list_id=list_id,
            name=name,
            address=address,
            domain=domain,
            email_address=email_address,
            is_syncing=is_syncing,
            money_format=money_format,
            phone=phone,
            platform=platform,
            primary_locale=primary_locale,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    def get_store(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceStore:
        """
        Get information about a specific store.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceStore


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store(
            store_id="store_id",
        )
        """
        _response = self._raw_client.get_store(
            store_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete_store(self, store_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a store. Deleting a store will also delete any associated subresources, including Customers, Orders, Products, and Carts.

        Parameters
        ----------
        store_id : str
            The store id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store(
            store_id="store_id",
        )
        """
        _response = self._raw_client.delete_store(store_id, request_options=request_options)
        return _response.data

    def update_store(
        self,
        store_id: str,
        *,
        address: typing.Optional[UpdateStoreEcommerceRequestAddress] = OMIT,
        currency_code: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        is_syncing: typing.Optional[bool] = OMIT,
        money_format: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        primary_locale: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceStore:
        """
        Update a store.

        Parameters
        ----------
        store_id : str
            The store id.

        address : typing.Optional[UpdateStoreEcommerceRequestAddress]
            The store address.

        currency_code : typing.Optional[str]
            The three-letter ISO 4217 code for the currency that the store accepts.

        domain : typing.Optional[str]
            The store domain.

        email_address : typing.Optional[str]
            The email address for the store.

        is_syncing : typing.Optional[bool]
            Whether to disable automations because the store is currently [syncing](https://mailchimp.com/developer/marketing/docs/e-commerce/#pausing-store-automations).

        money_format : typing.Optional[str]
            The currency format for the store. For example: `$`, `£`, etc.

        name : typing.Optional[str]
            The name of the store.

        phone : typing.Optional[str]
            The store phone number.

        platform : typing.Optional[str]
            The e-commerce platform of the store.

        primary_locale : typing.Optional[str]
            The primary locale for the store. For example: `en`, `de`, etc.

        timezone : typing.Optional[str]
            The timezone for the store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceStore


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store(
            store_id="store_id",
        )
        """
        _response = self._raw_client.update_store(
            store_id,
            address=address,
            currency_code=currency_code,
            domain=domain,
            email_address=email_address,
            is_syncing=is_syncing,
            money_format=money_format,
            name=name,
            phone=phone,
            platform=platform,
            primary_locale=primary_locale,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    def list_store_carts(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommerceCart, ListStoreCartsEcommerceResponse]:
        """
        Get information about a store's carts.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommerceCart, ListStoreCartsEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_store_carts(
            store_id="store_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_store_carts(
            store_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    def create_store_cart(
        self,
        store_id: str,
        *,
        currency_code: str,
        customer: EcommerceStoresCartsPost,
        id: CreateStoreCartEcommerceRequestId,
        lines: typing.Sequence[CreateStoreCartEcommerceRequestLinesItem],
        order_total: CreateStoreCartEcommerceRequestOrderTotal,
        campaign_id: typing.Optional[str] = OMIT,
        checkout_url: typing.Optional[str] = OMIT,
        tax_total: typing.Optional[CreateStoreCartEcommerceRequestTaxTotal] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCart:
        """
        Add a new cart to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        currency_code : str
            The three-letter ISO 4217 code for the currency that the cart uses.

        customer : EcommerceStoresCartsPost

        id : CreateStoreCartEcommerceRequestId
            A unique identifier for the cart.

        lines : typing.Sequence[CreateStoreCartEcommerceRequestLinesItem]
            An array of the cart's line items.

        order_total : CreateStoreCartEcommerceRequestOrderTotal

        campaign_id : typing.Optional[str]
            A string that uniquely identifies the campaign for a cart.

        checkout_url : typing.Optional[str]
            The URL for the cart. This parameter is required for [Abandoned Cart](https://mailchimp.com/help/create-a-classic-abandoned-cart-email/) automations.

        tax_total : typing.Optional[CreateStoreCartEcommerceRequestTaxTotal]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCart


        Examples
        --------
        from mailchimp_marketing import EcommerceStoresCartsPost, MailchimpClient
        from mailchimp_marketing.ecommerce import (
            CreateStoreCartEcommerceRequestLinesItem,
        )

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store_cart(
            store_id="store_id",
            currency_code="currency_code",
            customer=EcommerceStoresCartsPost(
                id="id",
            ),
            id="id",
            lines=[
                CreateStoreCartEcommerceRequestLinesItem(
                    id="id",
                    price=1.1,
                    product_id="product_id",
                    product_variant_id="product_variant_id",
                    quantity=1,
                )
            ],
            order_total=1.1,
        )
        """
        _response = self._raw_client.create_store_cart(
            store_id,
            currency_code=currency_code,
            customer=customer,
            id=id,
            lines=lines,
            order_total=order_total,
            campaign_id=campaign_id,
            checkout_url=checkout_url,
            tax_total=tax_total,
            request_options=request_options,
        )
        return _response.data

    def get_store_cart(
        self,
        store_id: str,
        cart_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCart:
        """
        Get information about a specific cart.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCart


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store_cart(
            store_id="store_id",
            cart_id="cart_id",
        )
        """
        _response = self._raw_client.get_store_cart(
            store_id, cart_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete_store_cart(
        self, store_id: str, cart_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a cart.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store_cart(
            store_id="store_id",
            cart_id="cart_id",
        )
        """
        _response = self._raw_client.delete_store_cart(store_id, cart_id, request_options=request_options)
        return _response.data

    def update_store_cart(
        self,
        store_id: str,
        cart_id: str,
        *,
        campaign_id: typing.Optional[str] = OMIT,
        checkout_url: typing.Optional[str] = OMIT,
        currency_code: typing.Optional[str] = OMIT,
        customer: typing.Optional[EcommerceStoresCartsPatch] = OMIT,
        id: typing.Optional[UpdateStoreCartEcommerceRequestId] = OMIT,
        lines: typing.Optional[typing.Sequence[UpdateStoreCartEcommerceRequestLinesItem]] = OMIT,
        order_total: typing.Optional[UpdateStoreCartEcommerceRequestOrderTotal] = OMIT,
        tax_total: typing.Optional[UpdateStoreCartEcommerceRequestTaxTotal] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCart:
        """
        Update a specific cart.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        campaign_id : typing.Optional[str]
            A string that uniquely identifies the campaign associated with a cart.

        checkout_url : typing.Optional[str]
            The URL for the cart. This parameter is required for [Abandoned Cart](https://mailchimp.com/help/create-a-classic-abandoned-cart-email/) automations.

        currency_code : typing.Optional[str]
            The three-letter ISO 4217 code for the currency that the cart uses.

        customer : typing.Optional[EcommerceStoresCartsPatch]

        id : typing.Optional[UpdateStoreCartEcommerceRequestId]
            A unique identifier for the cart.

        lines : typing.Optional[typing.Sequence[UpdateStoreCartEcommerceRequestLinesItem]]
            An array of the cart's line items.

        order_total : typing.Optional[UpdateStoreCartEcommerceRequestOrderTotal]

        tax_total : typing.Optional[UpdateStoreCartEcommerceRequestTaxTotal]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCart


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store_cart(
            store_id="store_id",
            cart_id="cart_id",
        )
        """
        _response = self._raw_client.update_store_cart(
            store_id,
            cart_id,
            campaign_id=campaign_id,
            checkout_url=checkout_url,
            currency_code=currency_code,
            customer=customer,
            id=id,
            lines=lines,
            order_total=order_total,
            tax_total=tax_total,
            request_options=request_options,
        )
        return _response.data

    def list_store_cart_lines(
        self,
        store_id: str,
        cart_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommerceCartLineItem, ListStoreCartLinesEcommerceResponse]:
        """
        Get information about a cart's line items.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommerceCartLineItem, ListStoreCartLinesEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_store_cart_lines(
            store_id="store_id",
            cart_id="cart_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_store_cart_lines(
            store_id,
            cart_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    def create_store_cart_line(
        self,
        store_id: str,
        cart_id: str,
        *,
        id: str,
        price: CreateStoreCartLineEcommerceRequestPrice,
        product_id: str,
        product_variant_id: str,
        quantity: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCartLineItem:
        """
        Add a new line item to an existing cart.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        id : str
            A unique identifier for the cart line item.

        price : CreateStoreCartLineEcommerceRequestPrice

        product_id : str
            A unique identifier for the product associated with the cart line item.

        product_variant_id : str
            A unique identifier for the product variant associated with the cart line item.

        quantity : int
            The quantity of a cart line item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCartLineItem


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store_cart_line(
            store_id="store_id",
            cart_id="cart_id",
            id="id",
            price=1.1,
            product_id="product_id",
            product_variant_id="product_variant_id",
            quantity=1,
        )
        """
        _response = self._raw_client.create_store_cart_line(
            store_id,
            cart_id,
            id=id,
            price=price,
            product_id=product_id,
            product_variant_id=product_variant_id,
            quantity=quantity,
            request_options=request_options,
        )
        return _response.data

    def get_store_cart_line(
        self,
        store_id: str,
        cart_id: str,
        line_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCartLineItem:
        """
        Get information about a specific cart line item.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        line_id : str
            The id for the line item of a cart.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCartLineItem


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store_cart_line(
            store_id="store_id",
            cart_id="cart_id",
            line_id="line_id",
        )
        """
        _response = self._raw_client.get_store_cart_line(
            store_id, cart_id, line_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete_store_cart_line(
        self, store_id: str, cart_id: str, line_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a specific cart line item.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        line_id : str
            The id for the line item of a cart.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store_cart_line(
            store_id="store_id",
            cart_id="cart_id",
            line_id="line_id",
        )
        """
        _response = self._raw_client.delete_store_cart_line(store_id, cart_id, line_id, request_options=request_options)
        return _response.data

    def update_store_cart_line(
        self,
        store_id: str,
        cart_id: str,
        line_id: str,
        *,
        price: typing.Optional[UpdateStoreCartLineEcommerceRequestPrice] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        product_variant_id: typing.Optional[str] = OMIT,
        quantity: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCartLineItem:
        """
        Update a specific cart line item.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        line_id : str
            The id for the line item of a cart.

        price : typing.Optional[UpdateStoreCartLineEcommerceRequestPrice]

        product_id : typing.Optional[str]
            A unique identifier for the product associated with the cart line item.

        product_variant_id : typing.Optional[str]
            A unique identifier for the product variant associated with the cart line item.

        quantity : typing.Optional[int]
            The quantity of a cart line item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCartLineItem


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store_cart_line(
            store_id="store_id",
            cart_id="cart_id",
            line_id="line_id",
        )
        """
        _response = self._raw_client.update_store_cart_line(
            store_id,
            cart_id,
            line_id,
            price=price,
            product_id=product_id,
            product_variant_id=product_variant_id,
            quantity=quantity,
            request_options=request_options,
        )
        return _response.data

    def list_store_customers(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        email_address: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommerceCustomer, ListStoreCustomersEcommerceResponse]:
        """
        Get information about a store's customers.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        email_address : typing.Optional[str]
            Restrict the response to customers with the email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommerceCustomer, ListStoreCustomersEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_store_customers(
            store_id="store_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_store_customers(
            store_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            email_address=email_address,
            request_options=request_options,
        )

    def create_store_customer(
        self,
        store_id: str,
        *,
        id: str,
        opt_in_status: bool,
        address: typing.Optional[CreateStoreCustomerEcommerceRequestAddress] = OMIT,
        company: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        sms_phone_number: typing.Optional[str] = OMIT,
        total_spent: typing.Optional[CreateStoreCustomerEcommerceRequestTotalSpent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCustomer:
        """
        Add a new customer to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        id : str
            A unique identifier for the customer. Limited to 50 characters.

        opt_in_status : bool
            The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing Mailchimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your Mailchimp list [will be added as `Transactional` members](https://mailchimp.com/developer/marketing/docs/e-commerce/#customers).

        address : typing.Optional[CreateStoreCustomerEcommerceRequestAddress]
            The customer's address.

        company : typing.Optional[str]
            The customer's company.

        email_address : typing.Optional[str]
            The customer's email address.

        first_name : typing.Optional[str]
            The customer's first name.

        last_name : typing.Optional[str]
            The customer's last name.

        sms_phone_number : typing.Optional[str]
            A US phone number for SMS contact.

        total_spent : typing.Optional[CreateStoreCustomerEcommerceRequestTotalSpent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCustomer


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store_customer(
            store_id="store_id",
            id="id",
            opt_in_status=True,
        )
        """
        _response = self._raw_client.create_store_customer(
            store_id,
            id=id,
            opt_in_status=opt_in_status,
            address=address,
            company=company,
            email_address=email_address,
            first_name=first_name,
            last_name=last_name,
            sms_phone_number=sms_phone_number,
            total_spent=total_spent,
            request_options=request_options,
        )
        return _response.data

    def get_store_customer(
        self,
        store_id: str,
        customer_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCustomer:
        """
        Get information about a specific customer.

        Parameters
        ----------
        store_id : str
            The store id.

        customer_id : str
            The id for the customer of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCustomer


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store_customer(
            store_id="store_id",
            customer_id="customer_id",
        )
        """
        _response = self._raw_client.get_store_customer(
            store_id, customer_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def upsert_store_customer(
        self,
        store_id: str,
        customer_id: str,
        *,
        address: typing.Optional[UpsertStoreCustomerEcommerceRequestAddress] = OMIT,
        company: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        opt_in_status: typing.Optional[bool] = OMIT,
        sms_phone_number: typing.Optional[str] = OMIT,
        total_spent: typing.Optional[UpsertStoreCustomerEcommerceRequestTotalSpent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCustomer:
        """
        Add or update a customer.

        Parameters
        ----------
        store_id : str
            The store id.

        customer_id : str
            The id for the customer of a store.

        address : typing.Optional[UpsertStoreCustomerEcommerceRequestAddress]
            The customer's address.

        company : typing.Optional[str]
            The customer's company.

        email_address : typing.Optional[str]
            The customer's email address.

        first_name : typing.Optional[str]
            The customer's first name.

        id : typing.Optional[str]
            A unique identifier for the customer. Limited to 50 characters.

        last_name : typing.Optional[str]
            The customer's last name.

        opt_in_status : typing.Optional[bool]
            The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing Mailchimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your Mailchimp list [will be added as `Transactional` members](https://mailchimp.com/developer/marketing/docs/e-commerce/#customers).

        sms_phone_number : typing.Optional[str]
            A US phone number for SMS contact.

        total_spent : typing.Optional[UpsertStoreCustomerEcommerceRequestTotalSpent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCustomer


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.upsert_store_customer(
            store_id="store_id",
            customer_id="customer_id",
        )
        """
        _response = self._raw_client.upsert_store_customer(
            store_id,
            customer_id,
            address=address,
            company=company,
            email_address=email_address,
            first_name=first_name,
            id=id,
            last_name=last_name,
            opt_in_status=opt_in_status,
            sms_phone_number=sms_phone_number,
            total_spent=total_spent,
            request_options=request_options,
        )
        return _response.data

    def delete_store_customer(
        self, store_id: str, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a customer from a store.

        Parameters
        ----------
        store_id : str
            The store id.

        customer_id : str
            The id for the customer of a store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store_customer(
            store_id="store_id",
            customer_id="customer_id",
        )
        """
        _response = self._raw_client.delete_store_customer(store_id, customer_id, request_options=request_options)
        return _response.data

    def update_store_customer(
        self,
        store_id: str,
        customer_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        address: typing.Optional[EcommerceStoresCartsPatchAddress] = OMIT,
        company: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        opt_in_status: typing.Optional[bool] = OMIT,
        total_spent: typing.Optional[EcommerceStoresCartsPatchTotalSpent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCustomer:
        """
        Update a customer.

        Parameters
        ----------
        store_id : str
            The store id.

        customer_id : str
            The id for the customer of a store.

        id : typing.Optional[str]
            A unique identifier for the customer. Limited to 50 characters.

        address : typing.Optional[EcommerceStoresCartsPatchAddress]
            The customer's address.

        company : typing.Optional[str]
            The customer's company.

        first_name : typing.Optional[str]
            The customer's first name.

        last_name : typing.Optional[str]
            The customer's last name.

        opt_in_status : typing.Optional[bool]
            The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing Mailchimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your Mailchimp list [will be added as `Transactional` members](https://mailchimp.com/developer/marketing/docs/e-commerce/#customers).

        total_spent : typing.Optional[EcommerceStoresCartsPatchTotalSpent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCustomer


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store_customer(
            store_id="store_id",
            customer_id="customer_id",
        )
        """
        _response = self._raw_client.update_store_customer(
            store_id,
            customer_id,
            id=id,
            address=address,
            company=company,
            first_name=first_name,
            last_name=last_name,
            opt_in_status=opt_in_status,
            total_spent=total_spent,
            request_options=request_options,
        )
        return _response.data

    def list_store_orders(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        customer_id: typing.Optional[str] = None,
        has_outreach: typing.Optional[bool] = None,
        campaign_id: typing.Optional[str] = None,
        outreach_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommerceOrder, ListStoreOrdersEcommerceResponse]:
        """
        Get information about a store's orders.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        customer_id : typing.Optional[str]
            Restrict results to orders made by a specific customer.

        has_outreach : typing.Optional[bool]
            Restrict results to orders that have an outreach attached. For example, an email campaign or Facebook ad.

        campaign_id : typing.Optional[str]
            Restrict results to orders with a specific `campaign_id` value.

        outreach_id : typing.Optional[str]
            Restrict results to orders with a specific `outreach_id` value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommerceOrder, ListStoreOrdersEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_store_orders(
            store_id="store_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_store_orders(
            store_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            customer_id=customer_id,
            has_outreach=has_outreach,
            campaign_id=campaign_id,
            outreach_id=outreach_id,
            request_options=request_options,
        )

    def create_store_order(
        self,
        store_id: str,
        *,
        currency_code: str,
        customer: EcommerceStoresCartsPost,
        id: str,
        lines: typing.Sequence[CreateStoreOrderEcommerceRequestLinesItem],
        order_total: CreateStoreOrderEcommerceRequestOrderTotal,
        billing_address: typing.Optional[CreateStoreOrderEcommerceRequestBillingAddress] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        cart_id: typing.Optional[CreateStoreOrderEcommerceRequestCartId] = OMIT,
        cancelled_at_foreign: typing.Optional[str] = OMIT,
        discount_total: typing.Optional[CreateStoreOrderEcommerceRequestDiscountTotal] = OMIT,
        financial_status: typing.Optional[str] = OMIT,
        fulfillment_status: typing.Optional[str] = OMIT,
        landing_site: typing.Optional[str] = OMIT,
        order_url: typing.Optional[str] = OMIT,
        outreach: typing.Optional[CreateStoreOrderEcommerceRequestOutreach] = OMIT,
        processed_at_foreign: typing.Optional[str] = OMIT,
        promos: typing.Optional[typing.Sequence[CreateStoreOrderEcommerceRequestPromosItem]] = OMIT,
        shipping_address: typing.Optional[CreateStoreOrderEcommerceRequestShippingAddress] = OMIT,
        shipping_total: typing.Optional[CreateStoreOrderEcommerceRequestShippingTotal] = OMIT,
        tax_total: typing.Optional[CreateStoreOrderEcommerceRequestTaxTotal] = OMIT,
        tracking_carrier: typing.Optional[str] = OMIT,
        tracking_code: typing.Optional[CreateStoreOrderEcommerceRequestTrackingCode] = OMIT,
        tracking_number: typing.Optional[str] = OMIT,
        tracking_url: typing.Optional[str] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrder:
        """
        Add a new order to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        currency_code : str
            The three-letter ISO 4217 code for the currency that the store accepts.

        customer : EcommerceStoresCartsPost

        id : str
            A unique identifier for the order.

        lines : typing.Sequence[CreateStoreOrderEcommerceRequestLinesItem]
            An array of the order's line items.

        order_total : CreateStoreOrderEcommerceRequestOrderTotal

        billing_address : typing.Optional[CreateStoreOrderEcommerceRequestBillingAddress]
            The billing address for the order.

        campaign_id : typing.Optional[str]
            A string that uniquely identifies the campaign for an order.

        cart_id : typing.Optional[CreateStoreOrderEcommerceRequestCartId]
            A cart id that the order was placed for.

        cancelled_at_foreign : typing.Optional[str]
            The date and time the order was cancelled in ISO 8601 format. Note: passing a value for this parameter will cancel the order being created.

        discount_total : typing.Optional[CreateStoreOrderEcommerceRequestDiscountTotal]

        financial_status : typing.Optional[str]
            The order status. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).

        fulfillment_status : typing.Optional[str]
            The fulfillment status for the order. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).

        landing_site : typing.Optional[str]
            The URL for the page where the buyer landed when entering the shop.

        order_url : typing.Optional[str]
            The URL for the order.

        outreach : typing.Optional[CreateStoreOrderEcommerceRequestOutreach]
            The outreach associated with this order. For example, an email campaign or Facebook ad.

        processed_at_foreign : typing.Optional[str]
            The date and time the order was processed in ISO 8601 format.

        promos : typing.Optional[typing.Sequence[CreateStoreOrderEcommerceRequestPromosItem]]
            The promo codes applied on the order

        shipping_address : typing.Optional[CreateStoreOrderEcommerceRequestShippingAddress]
            The shipping address for the order.

        shipping_total : typing.Optional[CreateStoreOrderEcommerceRequestShippingTotal]

        tax_total : typing.Optional[CreateStoreOrderEcommerceRequestTaxTotal]

        tracking_carrier : typing.Optional[str]
            The tracking carrier associated with the order.

        tracking_code : typing.Optional[CreateStoreOrderEcommerceRequestTrackingCode]
            The Mailchimp tracking code for the order. Uses the 'mc_tc' parameter in E-Commerce tracking URLs.

        tracking_number : typing.Optional[str]
            The tracking number associated with the order.

        tracking_url : typing.Optional[str]
            The tracking URL associated with the order.

        updated_at_foreign : typing.Optional[str]
            The date and time the order was updated in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrder


        Examples
        --------
        from mailchimp_marketing import EcommerceStoresCartsPost, MailchimpClient
        from mailchimp_marketing.ecommerce import (
            CreateStoreOrderEcommerceRequestLinesItem,
        )

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store_order(
            store_id="store_id",
            currency_code="currency_code",
            customer=EcommerceStoresCartsPost(
                id="id",
            ),
            id="id",
            lines=[
                CreateStoreOrderEcommerceRequestLinesItem(
                    id="id",
                    price=1.1,
                    product_id="product_id",
                    product_variant_id="product_variant_id",
                    quantity=1,
                )
            ],
            order_total=1.1,
        )
        """
        _response = self._raw_client.create_store_order(
            store_id,
            currency_code=currency_code,
            customer=customer,
            id=id,
            lines=lines,
            order_total=order_total,
            billing_address=billing_address,
            campaign_id=campaign_id,
            cart_id=cart_id,
            cancelled_at_foreign=cancelled_at_foreign,
            discount_total=discount_total,
            financial_status=financial_status,
            fulfillment_status=fulfillment_status,
            landing_site=landing_site,
            order_url=order_url,
            outreach=outreach,
            processed_at_foreign=processed_at_foreign,
            promos=promos,
            shipping_address=shipping_address,
            shipping_total=shipping_total,
            tax_total=tax_total,
            tracking_carrier=tracking_carrier,
            tracking_code=tracking_code,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            updated_at_foreign=updated_at_foreign,
            request_options=request_options,
        )
        return _response.data

    def get_store_order(
        self,
        store_id: str,
        order_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrder:
        """
        Get information about a specific order.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrder


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store_order(
            store_id="store_id",
            order_id="order_id",
        )
        """
        _response = self._raw_client.get_store_order(
            store_id, order_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete_store_order(
        self, store_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an order.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store_order(
            store_id="store_id",
            order_id="order_id",
        )
        """
        _response = self._raw_client.delete_store_order(store_id, order_id, request_options=request_options)
        return _response.data

    def update_store_order(
        self,
        store_id: str,
        order_id: str,
        *,
        billing_address: typing.Optional[UpdateStoreOrderEcommerceRequestBillingAddress] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        cart_id: typing.Optional[UpdateStoreOrderEcommerceRequestCartId] = OMIT,
        cancelled_at_foreign: typing.Optional[str] = OMIT,
        currency_code: typing.Optional[str] = OMIT,
        customer: typing.Optional[EcommerceStoresCartsPatch] = OMIT,
        discount_total: typing.Optional[UpdateStoreOrderEcommerceRequestDiscountTotal] = OMIT,
        financial_status: typing.Optional[str] = OMIT,
        fulfillment_status: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        landing_site: typing.Optional[str] = OMIT,
        lines: typing.Optional[typing.Sequence[UpdateStoreOrderEcommerceRequestLinesItem]] = OMIT,
        order_total: typing.Optional[UpdateStoreOrderEcommerceRequestOrderTotal] = OMIT,
        order_url: typing.Optional[str] = OMIT,
        outreach: typing.Optional[UpdateStoreOrderEcommerceRequestOutreach] = OMIT,
        processed_at_foreign: typing.Optional[str] = OMIT,
        promos: typing.Optional[typing.Sequence[UpdateStoreOrderEcommerceRequestPromosItem]] = OMIT,
        shipping_address: typing.Optional[UpdateStoreOrderEcommerceRequestShippingAddress] = OMIT,
        shipping_total: typing.Optional[UpdateStoreOrderEcommerceRequestShippingTotal] = OMIT,
        tax_total: typing.Optional[UpdateStoreOrderEcommerceRequestTaxTotal] = OMIT,
        tracking_carrier: typing.Optional[str] = OMIT,
        tracking_code: typing.Optional[UpdateStoreOrderEcommerceRequestTrackingCode] = OMIT,
        tracking_number: typing.Optional[str] = OMIT,
        tracking_url: typing.Optional[str] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrder:
        """
        Update a specific order.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        billing_address : typing.Optional[UpdateStoreOrderEcommerceRequestBillingAddress]
            The billing address for the order.

        campaign_id : typing.Optional[str]
            A string that uniquely identifies the campaign associated with an order.

        cart_id : typing.Optional[UpdateStoreOrderEcommerceRequestCartId]
            A cart id that the order was placed for.

        cancelled_at_foreign : typing.Optional[str]
            The date and time the order was cancelled in ISO 8601 format. Note: passing a value for this parameter will cancel the order being edited.

        currency_code : typing.Optional[str]
            The three-letter ISO 4217 code for the currency that the store accepts.

        customer : typing.Optional[EcommerceStoresCartsPatch]

        discount_total : typing.Optional[UpdateStoreOrderEcommerceRequestDiscountTotal]

        financial_status : typing.Optional[str]
            The order status. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).

        fulfillment_status : typing.Optional[str]
            The fulfillment status for the order. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).

        id : typing.Optional[str]
            A unique identifier for the order.

        landing_site : typing.Optional[str]
            The URL for the page where the buyer landed when entering the shop.

        lines : typing.Optional[typing.Sequence[UpdateStoreOrderEcommerceRequestLinesItem]]
            An array of the order's line items.

        order_total : typing.Optional[UpdateStoreOrderEcommerceRequestOrderTotal]

        order_url : typing.Optional[str]
            The URL for the order.

        outreach : typing.Optional[UpdateStoreOrderEcommerceRequestOutreach]
            The outreach associated with this order. For example, an email campaign or Facebook ad.

        processed_at_foreign : typing.Optional[str]
            The date and time the order was processed in ISO 8601 format.

        promos : typing.Optional[typing.Sequence[UpdateStoreOrderEcommerceRequestPromosItem]]
            The promo codes applied on the order. Note: Patch will completely replace the value of promos with the new one provided.

        shipping_address : typing.Optional[UpdateStoreOrderEcommerceRequestShippingAddress]
            The shipping address for the order.

        shipping_total : typing.Optional[UpdateStoreOrderEcommerceRequestShippingTotal]

        tax_total : typing.Optional[UpdateStoreOrderEcommerceRequestTaxTotal]

        tracking_carrier : typing.Optional[str]
            The tracking carrier associated with the order.

        tracking_code : typing.Optional[UpdateStoreOrderEcommerceRequestTrackingCode]
            The Mailchimp tracking code for the order. Uses the 'mc_tc' parameter in E-Commerce tracking URLs.

        tracking_number : typing.Optional[str]
            The tracking number associated with the order.

        tracking_url : typing.Optional[str]
            The tracking URL associated with the order.

        updated_at_foreign : typing.Optional[str]
            The date and time the order was updated in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrder


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store_order(
            store_id="store_id",
            order_id="order_id",
        )
        """
        _response = self._raw_client.update_store_order(
            store_id,
            order_id,
            billing_address=billing_address,
            campaign_id=campaign_id,
            cart_id=cart_id,
            cancelled_at_foreign=cancelled_at_foreign,
            currency_code=currency_code,
            customer=customer,
            discount_total=discount_total,
            financial_status=financial_status,
            fulfillment_status=fulfillment_status,
            id=id,
            landing_site=landing_site,
            lines=lines,
            order_total=order_total,
            order_url=order_url,
            outreach=outreach,
            processed_at_foreign=processed_at_foreign,
            promos=promos,
            shipping_address=shipping_address,
            shipping_total=shipping_total,
            tax_total=tax_total,
            tracking_carrier=tracking_carrier,
            tracking_code=tracking_code,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            updated_at_foreign=updated_at_foreign,
            request_options=request_options,
        )
        return _response.data

    def list_store_order_lines(
        self,
        store_id: str,
        order_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommerceOrderLineItem, ListStoreOrderLinesEcommerceResponse]:
        """
        Get information about an order's line items.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommerceOrderLineItem, ListStoreOrderLinesEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_store_order_lines(
            store_id="store_id",
            order_id="order_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_store_order_lines(
            store_id,
            order_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    def create_store_order_line(
        self,
        store_id: str,
        order_id: str,
        *,
        id: str,
        price: CreateStoreOrderLineEcommerceRequestPrice,
        product_id: str,
        product_variant_id: str,
        quantity: int,
        discount: typing.Optional[CreateStoreOrderLineEcommerceRequestDiscount] = OMIT,
        product: typing.Optional[EcommerceStoresOrdersPost] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrderLineItem:
        """
        Add a new line item to an existing order.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        id : str
            A unique identifier for the order line item.

        price : CreateStoreOrderLineEcommerceRequestPrice

        product_id : str
            A unique identifier for the product associated with the order line item.

        product_variant_id : str
            A unique identifier for the product variant associated with the order line item.

        quantity : int
            The quantity of an order line item.

        discount : typing.Optional[CreateStoreOrderLineEcommerceRequestDiscount]

        product : typing.Optional[EcommerceStoresOrdersPost]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrderLineItem


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store_order_line(
            store_id="store_id",
            order_id="order_id",
            id="id",
            price=1.1,
            product_id="product_id",
            product_variant_id="product_variant_id",
            quantity=1,
        )
        """
        _response = self._raw_client.create_store_order_line(
            store_id,
            order_id,
            id=id,
            price=price,
            product_id=product_id,
            product_variant_id=product_variant_id,
            quantity=quantity,
            discount=discount,
            product=product,
            request_options=request_options,
        )
        return _response.data

    def get_store_order_line(
        self,
        store_id: str,
        order_id: str,
        line_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrderLineItem:
        """
        Get information about a specific order line item.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        line_id : str
            The id for the line item of an order.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrderLineItem


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store_order_line(
            store_id="store_id",
            order_id="order_id",
            line_id="line_id",
        )
        """
        _response = self._raw_client.get_store_order_line(
            store_id, order_id, line_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete_store_order_line(
        self, store_id: str, order_id: str, line_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a specific order line item.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        line_id : str
            The id for the line item of an order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store_order_line(
            store_id="store_id",
            order_id="order_id",
            line_id="line_id",
        )
        """
        _response = self._raw_client.delete_store_order_line(
            store_id, order_id, line_id, request_options=request_options
        )
        return _response.data

    def update_store_order_line(
        self,
        store_id: str,
        order_id: str,
        line_id: str,
        *,
        discount: typing.Optional[UpdateStoreOrderLineEcommerceRequestDiscount] = OMIT,
        id: typing.Optional[str] = OMIT,
        price: typing.Optional[UpdateStoreOrderLineEcommerceRequestPrice] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        product_variant_id: typing.Optional[str] = OMIT,
        quantity: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrderLineItem:
        """
        Update a specific order line item.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        line_id : str
            The id for the line item of an order.

        discount : typing.Optional[UpdateStoreOrderLineEcommerceRequestDiscount]

        id : typing.Optional[str]
            A unique identifier for the order line item.

        price : typing.Optional[UpdateStoreOrderLineEcommerceRequestPrice]

        product_id : typing.Optional[str]
            A unique identifier for the product associated with the order line item.

        product_variant_id : typing.Optional[str]
            A unique identifier for the product variant associated with the order line item.

        quantity : typing.Optional[int]
            The quantity of an order line item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrderLineItem


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store_order_line(
            store_id="store_id",
            order_id="order_id",
            line_id="line_id",
        )
        """
        _response = self._raw_client.update_store_order_line(
            store_id,
            order_id,
            line_id,
            discount=discount,
            id=id,
            price=price,
            product_id=product_id,
            product_variant_id=product_variant_id,
            quantity=quantity,
            request_options=request_options,
        )
        return _response.data

    def list_store_products(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommerceProduct, ListStoreProductsEcommerceResponse]:
        """
        Get information about a store's products.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommerceProduct, ListStoreProductsEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_store_products(
            store_id="store_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_store_products(
            store_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    def create_store_product(
        self,
        store_id: str,
        *,
        id: EcommerceStoresOrdersPostId,
        title: str,
        variants: typing.Sequence[EcommerceStoresOrdersPostVariantsItem],
        description: typing.Optional[str] = OMIT,
        handle: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        images: typing.Optional[typing.Sequence[EcommerceStoresOrdersPostImagesItem]] = OMIT,
        published_at_foreign: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        vendor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProduct:
        """
        Add a new product to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        id : EcommerceStoresOrdersPostId
            A unique identifier for the product.

        title : str
            The title of a product.

        variants : typing.Sequence[EcommerceStoresOrdersPostVariantsItem]
            An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.

        description : typing.Optional[str]
            The description of a product.

        handle : typing.Optional[str]
            The handle of a product.

        image_url : typing.Optional[str]
            The image URL for a product.

        images : typing.Optional[typing.Sequence[EcommerceStoresOrdersPostImagesItem]]
            An array of the product's images.

        published_at_foreign : typing.Optional[str]
            The date and time the product was published.

        type : typing.Optional[str]
            The type of product.

        url : typing.Optional[str]
            The URL for a product.

        vendor : typing.Optional[str]
            The vendor for a product.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProduct


        Examples
        --------
        from mailchimp_marketing import (
            EcommerceStoresOrdersPostVariantsItem,
            MailchimpClient,
        )

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store_product(
            store_id="store_id",
            id="id",
            title="Cat Hat",
            variants=[
                EcommerceStoresOrdersPostVariantsItem(
                    id="id",
                    title="Cat Hat",
                )
            ],
        )
        """
        _response = self._raw_client.create_store_product(
            store_id,
            id=id,
            title=title,
            variants=variants,
            description=description,
            handle=handle,
            image_url=image_url,
            images=images,
            published_at_foreign=published_at_foreign,
            type=type,
            url=url,
            vendor=vendor,
            request_options=request_options,
        )
        return _response.data

    def get_store_product(
        self,
        store_id: str,
        product_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProduct:
        """
        Get information about a specific product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProduct


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store_product(
            store_id="store_id",
            product_id="product_id",
        )
        """
        _response = self._raw_client.get_store_product(
            store_id, product_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def upsert_store_product(
        self,
        store_id: str,
        product_id: str,
        *,
        id: UpsertStoreProductEcommerceRequestId,
        description: typing.Optional[str] = OMIT,
        handle: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        images: typing.Optional[typing.Sequence[UpsertStoreProductEcommerceRequestImagesItem]] = OMIT,
        published_at_foreign: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        variants: typing.Optional[typing.Sequence[UpsertStoreProductEcommerceRequestVariantsItem]] = OMIT,
        vendor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProduct:
        """
        Update a specific product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        id : UpsertStoreProductEcommerceRequestId
            A unique identifier for the product.

        description : typing.Optional[str]
            The description of a product.

        handle : typing.Optional[str]
            The handle of a product.

        image_url : typing.Optional[str]
            The image URL for a product.

        images : typing.Optional[typing.Sequence[UpsertStoreProductEcommerceRequestImagesItem]]
            An array of the product's images.

        published_at_foreign : typing.Optional[str]
            The date and time the product was published.

        title : typing.Optional[str]
            The title of a product.

        type : typing.Optional[str]
            The type of product.

        url : typing.Optional[str]
            The URL for a product.

        variants : typing.Optional[typing.Sequence[UpsertStoreProductEcommerceRequestVariantsItem]]
            An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.

        vendor : typing.Optional[str]
            The vendor for a product.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProduct


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.upsert_store_product(
            store_id="store_id",
            product_id="product_id",
            id="id",
        )
        """
        _response = self._raw_client.upsert_store_product(
            store_id,
            product_id,
            id=id,
            description=description,
            handle=handle,
            image_url=image_url,
            images=images,
            published_at_foreign=published_at_foreign,
            title=title,
            type=type,
            url=url,
            variants=variants,
            vendor=vendor,
            request_options=request_options,
        )
        return _response.data

    def delete_store_product(
        self, store_id: str, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store_product(
            store_id="store_id",
            product_id="product_id",
        )
        """
        _response = self._raw_client.delete_store_product(store_id, product_id, request_options=request_options)
        return _response.data

    def update_store_product(
        self,
        store_id: str,
        product_id: str,
        *,
        description: typing.Optional[str] = OMIT,
        handle: typing.Optional[str] = OMIT,
        id: typing.Optional[UpdateStoreProductEcommerceRequestId] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        images: typing.Optional[typing.Sequence[UpdateStoreProductEcommerceRequestImagesItem]] = OMIT,
        published_at_foreign: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        variants: typing.Optional[typing.Sequence[UpdateStoreProductEcommerceRequestVariantsItem]] = OMIT,
        vendor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProduct:
        """
        Update a specific product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        description : typing.Optional[str]
            The description of a product.

        handle : typing.Optional[str]
            The handle of a product.

        id : typing.Optional[UpdateStoreProductEcommerceRequestId]
            A unique identifier for the product.

        image_url : typing.Optional[str]
            The image URL for a product.

        images : typing.Optional[typing.Sequence[UpdateStoreProductEcommerceRequestImagesItem]]
            An array of the product's images.

        published_at_foreign : typing.Optional[str]
            The date and time the product was published in ISO 8601 format.

        title : typing.Optional[str]
            The title of a product.

        type : typing.Optional[str]
            The type of product.

        url : typing.Optional[str]
            The URL for a product.

        variants : typing.Optional[typing.Sequence[UpdateStoreProductEcommerceRequestVariantsItem]]
            An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.

        vendor : typing.Optional[str]
            The vendor for a product.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProduct


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store_product(
            store_id="store_id",
            product_id="product_id",
        )
        """
        _response = self._raw_client.update_store_product(
            store_id,
            product_id,
            description=description,
            handle=handle,
            id=id,
            image_url=image_url,
            images=images,
            published_at_foreign=published_at_foreign,
            title=title,
            type=type,
            url=url,
            variants=variants,
            vendor=vendor,
            request_options=request_options,
        )
        return _response.data

    def list_store_product_images(
        self,
        store_id: str,
        product_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ListStoreProductImagesEcommerceResponseImagesItem, ListStoreProductImagesEcommerceResponse]:
        """
        Get information about a product's images.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ListStoreProductImagesEcommerceResponseImagesItem, ListStoreProductImagesEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_store_product_images(
            store_id="store_id",
            product_id="product_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_store_product_images(
            store_id,
            product_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    def create_store_product_image(
        self,
        store_id: str,
        product_id: str,
        *,
        id: str,
        url: str,
        variant_ids: typing.Optional[typing.Sequence[CreateStoreProductImageEcommerceRequestVariantIdsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateStoreProductImageEcommerceResponse:
        """
        Add a new image to the product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        id : str
            A unique identifier for the product image.

        url : str
            The URL for a product image.

        variant_ids : typing.Optional[typing.Sequence[CreateStoreProductImageEcommerceRequestVariantIdsItem]]
            The list of product variants using the image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateStoreProductImageEcommerceResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store_product_image(
            store_id="store_id",
            product_id="product_id",
            id="id",
            url="url",
        )
        """
        _response = self._raw_client.create_store_product_image(
            store_id, product_id, id=id, url=url, variant_ids=variant_ids, request_options=request_options
        )
        return _response.data

    def get_store_product_image(
        self,
        store_id: str,
        product_id: str,
        image_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStoreProductImageEcommerceResponse:
        """
        Get information about a specific product image.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        image_id : str
            The id for the product image.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStoreProductImageEcommerceResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store_product_image(
            store_id="store_id",
            product_id="product_id",
            image_id="image_id",
        )
        """
        _response = self._raw_client.get_store_product_image(
            store_id,
            product_id,
            image_id,
            fields=fields,
            exclude_fields=exclude_fields,
            request_options=request_options,
        )
        return _response.data

    def delete_store_product_image(
        self, store_id: str, product_id: str, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a product image.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        image_id : str
            The id for the product image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store_product_image(
            store_id="store_id",
            product_id="product_id",
            image_id="image_id",
        )
        """
        _response = self._raw_client.delete_store_product_image(
            store_id, product_id, image_id, request_options=request_options
        )
        return _response.data

    def update_store_product_image(
        self,
        store_id: str,
        product_id: str,
        image_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        variant_ids: typing.Optional[typing.Sequence[UpdateStoreProductImageEcommerceRequestVariantIdsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateStoreProductImageEcommerceResponse:
        """
        Update a product image.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        image_id : str
            The id for the product image.

        id : typing.Optional[str]
            A unique identifier for the product image.

        url : typing.Optional[str]
            The URL for a product image.

        variant_ids : typing.Optional[typing.Sequence[UpdateStoreProductImageEcommerceRequestVariantIdsItem]]
            The list of product variants using the image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateStoreProductImageEcommerceResponse


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store_product_image(
            store_id="store_id",
            product_id="product_id",
            image_id="image_id",
        )
        """
        _response = self._raw_client.update_store_product_image(
            store_id, product_id, image_id, id=id, url=url, variant_ids=variant_ids, request_options=request_options
        )
        return _response.data

    def list_store_product_variants(
        self,
        store_id: str,
        product_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommerceProductVariant, ListStoreProductVariantsEcommerceResponse]:
        """
        Get information about a product's variants.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommerceProductVariant, ListStoreProductVariantsEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_store_product_variants(
            store_id="store_id",
            product_id="product_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_store_product_variants(
            store_id,
            product_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    def create_store_product_variant(
        self,
        store_id: str,
        product_id: str,
        *,
        id: CreateStoreProductVariantEcommerceRequestId,
        title: str,
        backorders: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        inventory_quantity: typing.Optional[int] = OMIT,
        price: typing.Optional[CreateStoreProductVariantEcommerceRequestPrice] = OMIT,
        sku: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        visibility: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProductVariant:
        """
        Add a new variant to the product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        id : CreateStoreProductVariantEcommerceRequestId
            A unique identifier for the product variant.

        title : str
            The title of a product variant.

        backorders : typing.Optional[str]
            The backorders of a product variant.

        image_url : typing.Optional[str]
            The image URL for a product variant.

        inventory_quantity : typing.Optional[int]
            The inventory quantity of a product variant.

        price : typing.Optional[CreateStoreProductVariantEcommerceRequestPrice]

        sku : typing.Optional[str]
            The stock keeping unit (SKU) of a product variant.

        url : typing.Optional[str]
            The URL for a product variant.

        visibility : typing.Optional[str]
            The visibility of a product variant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProductVariant


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store_product_variant(
            store_id="store_id",
            product_id="product_id",
            id="id",
            title="Cat Hat",
        )
        """
        _response = self._raw_client.create_store_product_variant(
            store_id,
            product_id,
            id=id,
            title=title,
            backorders=backorders,
            image_url=image_url,
            inventory_quantity=inventory_quantity,
            price=price,
            sku=sku,
            url=url,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    def get_store_product_variant(
        self,
        store_id: str,
        product_id: str,
        variant_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProductVariant:
        """
        Get information about a specific product variant.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        variant_id : str
            The id for the product variant.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProductVariant


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store_product_variant(
            store_id="store_id",
            product_id="product_id",
            variant_id="variant_id",
        )
        """
        _response = self._raw_client.get_store_product_variant(
            store_id,
            product_id,
            variant_id,
            fields=fields,
            exclude_fields=exclude_fields,
            request_options=request_options,
        )
        return _response.data

    def upsert_store_product_variant(
        self,
        store_id: str,
        product_id: str,
        variant_id: str,
        *,
        backorders: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        inventory_quantity: typing.Optional[int] = OMIT,
        price: typing.Optional[UpsertStoreProductVariantEcommerceRequestPrice] = OMIT,
        sku: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        visibility: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProductVariant:
        """
        Add or update a product variant.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        variant_id : str
            The id for the product variant.

        backorders : typing.Optional[str]
            The backorders of a product variant.

        id : typing.Optional[str]
            A unique identifier for the product variant.

        image_url : typing.Optional[str]
            The image URL for a product variant.

        inventory_quantity : typing.Optional[int]
            The inventory quantity of a product variant.

        price : typing.Optional[UpsertStoreProductVariantEcommerceRequestPrice]

        sku : typing.Optional[str]
            The stock keeping unit (SKU) of a product variant.

        title : typing.Optional[str]
            The title of a product variant.

        url : typing.Optional[str]
            The URL for a product variant.

        visibility : typing.Optional[str]
            The visibility of a product variant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProductVariant


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.upsert_store_product_variant(
            store_id="store_id",
            product_id="product_id",
            variant_id="variant_id",
        )
        """
        _response = self._raw_client.upsert_store_product_variant(
            store_id,
            product_id,
            variant_id,
            backorders=backorders,
            id=id,
            image_url=image_url,
            inventory_quantity=inventory_quantity,
            price=price,
            sku=sku,
            title=title,
            url=url,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    def delete_store_product_variant(
        self,
        store_id: str,
        product_id: str,
        variant_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a product variant.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        variant_id : str
            The id for the product variant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store_product_variant(
            store_id="store_id",
            product_id="product_id",
            variant_id="variant_id",
        )
        """
        _response = self._raw_client.delete_store_product_variant(
            store_id, product_id, variant_id, request_options=request_options
        )
        return _response.data

    def update_store_product_variant(
        self,
        store_id: str,
        product_id: str,
        variant_id: str,
        *,
        backorders: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        inventory_quantity: typing.Optional[int] = OMIT,
        price: typing.Optional[UpdateStoreProductVariantEcommerceRequestPrice] = OMIT,
        sku: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        visibility: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProductVariant:
        """
        Update a product variant.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        variant_id : str
            The id for the product variant.

        backorders : typing.Optional[str]
            The backorders of a product variant.

        image_url : typing.Optional[str]
            The image URL for a product variant.

        inventory_quantity : typing.Optional[int]
            The inventory quantity of a product variant.

        price : typing.Optional[UpdateStoreProductVariantEcommerceRequestPrice]

        sku : typing.Optional[str]
            The stock keeping unit (SKU) of a product variant.

        title : typing.Optional[str]
            The title of a product variant.

        url : typing.Optional[str]
            The URL for a product variant.

        visibility : typing.Optional[str]
            The visibility of a product variant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProductVariant


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store_product_variant(
            store_id="store_id",
            product_id="product_id",
            variant_id="variant_id",
        )
        """
        _response = self._raw_client.update_store_product_variant(
            store_id,
            product_id,
            variant_id,
            backorders=backorders,
            image_url=image_url,
            inventory_quantity=inventory_quantity,
            price=price,
            sku=sku,
            title=title,
            url=url,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    def list_store_promo_rules(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommercePromoRule, ListStorePromoRulesEcommerceResponse]:
        """
        Get information about a store's promo rules.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommercePromoRule, ListStorePromoRulesEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_store_promo_rules(
            store_id="store_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_store_promo_rules(
            store_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    def create_store_promo_rule(
        self,
        store_id: str,
        *,
        amount: CreateStorePromoRuleEcommerceRequestAmount,
        description: str,
        id: str,
        target: CreateStorePromoRuleEcommerceRequestTarget,
        type: CreateStorePromoRuleEcommerceRequestType,
        created_at_foreign: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        ends_at: typing.Optional[CreateStorePromoRuleEcommerceRequestEndsAt] = OMIT,
        starts_at: typing.Optional[CreateStorePromoRuleEcommerceRequestStartsAt] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoRule:
        """
        Add a new promo rule to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        amount : CreateStorePromoRuleEcommerceRequestAmount

        description : str
            The description of a promotion restricted to UTF-8 characters with max length 255.

        id : str
            A unique identifier for the promo rule. If Ecommerce platform does not support promo rule, use promo code id as promo rule id. Restricted to UTF-8 characters with max length 50.

        target : CreateStorePromoRuleEcommerceRequestTarget
            The target that the discount applies to.

        type : CreateStorePromoRuleEcommerceRequestType
            Type of discount. For free shipping set type to fixed.

        created_at_foreign : typing.Optional[str]
            The date and time the promotion was created in ISO 8601 format.

        enabled : typing.Optional[bool]
            Whether the promo rule is currently enabled.

        ends_at : typing.Optional[CreateStorePromoRuleEcommerceRequestEndsAt]

        starts_at : typing.Optional[CreateStorePromoRuleEcommerceRequestStartsAt]

        title : typing.Optional[str]
            The title that will show up in promotion campaign. Restricted to UTF-8 characters with max length of 100 bytes.

        updated_at_foreign : typing.Optional[str]
            The date and time the promotion was updated in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoRule


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store_promo_rule(
            store_id="store_id",
            amount=1.1,
            description="Save BIG during our summer sale!",
            id="id",
            target="per_item",
            type="fixed",
        )
        """
        _response = self._raw_client.create_store_promo_rule(
            store_id,
            amount=amount,
            description=description,
            id=id,
            target=target,
            type=type,
            created_at_foreign=created_at_foreign,
            enabled=enabled,
            ends_at=ends_at,
            starts_at=starts_at,
            title=title,
            updated_at_foreign=updated_at_foreign,
            request_options=request_options,
        )
        return _response.data

    def get_store_promo_rule(
        self,
        store_id: str,
        promo_rule_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoRule:
        """
        Get information about a specific promo rule.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoRule


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store_promo_rule(
            store_id="store_id",
            promo_rule_id="promo_rule_id",
        )
        """
        _response = self._raw_client.get_store_promo_rule(
            store_id, promo_rule_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    def delete_store_promo_rule(
        self, store_id: str, promo_rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a promo rule from a store.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store_promo_rule(
            store_id="store_id",
            promo_rule_id="promo_rule_id",
        )
        """
        _response = self._raw_client.delete_store_promo_rule(store_id, promo_rule_id, request_options=request_options)
        return _response.data

    def update_store_promo_rule(
        self,
        store_id: str,
        promo_rule_id: str,
        *,
        amount: typing.Optional[UpdateStorePromoRuleEcommerceRequestAmount] = OMIT,
        created_at_foreign: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        ends_at: typing.Optional[UpdateStorePromoRuleEcommerceRequestEndsAt] = OMIT,
        id: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[UpdateStorePromoRuleEcommerceRequestStartsAt] = OMIT,
        target: typing.Optional[UpdateStorePromoRuleEcommerceRequestTarget] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[UpdateStorePromoRuleEcommerceRequestType] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoRule:
        """
        Update a promo rule.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        amount : typing.Optional[UpdateStorePromoRuleEcommerceRequestAmount]

        created_at_foreign : typing.Optional[str]
            The date and time the promotion was created in ISO 8601 format.

        description : typing.Optional[str]
            The description of a promotion restricted to UTF-8 characters with max length 255.

        enabled : typing.Optional[bool]
            Whether the promo rule is currently enabled.

        ends_at : typing.Optional[UpdateStorePromoRuleEcommerceRequestEndsAt]

        id : typing.Optional[str]
            A unique identifier for the promo rule. If Ecommerce platform does not support promo rule, use promo code id as promo rule id. Restricted to UTF-8 characters with max length 50.

        starts_at : typing.Optional[UpdateStorePromoRuleEcommerceRequestStartsAt]

        target : typing.Optional[UpdateStorePromoRuleEcommerceRequestTarget]
            The target that the discount applies to.

        title : typing.Optional[str]
            The title that will show up in promotion campaign. Restricted to UTF-8 characters with max length of 100 bytes.

        type : typing.Optional[UpdateStorePromoRuleEcommerceRequestType]
            Type of discount. For free shipping set type to fixed.

        updated_at_foreign : typing.Optional[str]
            The date and time the promotion was updated in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoRule


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store_promo_rule(
            store_id="store_id",
            promo_rule_id="promo_rule_id",
        )
        """
        _response = self._raw_client.update_store_promo_rule(
            store_id,
            promo_rule_id,
            amount=amount,
            created_at_foreign=created_at_foreign,
            description=description,
            enabled=enabled,
            ends_at=ends_at,
            id=id,
            starts_at=starts_at,
            target=target,
            title=title,
            type=type,
            updated_at_foreign=updated_at_foreign,
            request_options=request_options,
        )
        return _response.data

    def list_store_promo_rule_promo_codes(
        self,
        store_id: str,
        promo_rule_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ECommercePromoCode, ListStorePromoRulePromoCodesEcommerceResponse]:
        """
        Get information about a store's promo codes.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ECommercePromoCode, ListStorePromoRulePromoCodesEcommerceResponse]


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        response = client.ecommerce.list_store_promo_rule_promo_codes(
            store_id="store_id",
            promo_rule_id="promo_rule_id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_store_promo_rule_promo_codes(
            store_id,
            promo_rule_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    def create_store_promo_rule_promo_code(
        self,
        store_id: str,
        promo_rule_id: str,
        *,
        code: str,
        id: str,
        redemption_url: str,
        created_at_foreign: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        usage_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoCode:
        """
        Add a new promo code to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        code : str
            The discount code. Restricted to UTF-8 characters with max length 50.

        id : str
            A unique identifier for the promo code. Restricted to UTF-8 characters with max length 50.

        redemption_url : str
            The url that should be used in the promotion campaign restricted to UTF-8 characters with max length 2000.

        created_at_foreign : typing.Optional[str]
            The date and time the promotion was created in ISO 8601 format.

        enabled : typing.Optional[bool]
            Whether the promo code is currently enabled.

        updated_at_foreign : typing.Optional[str]
            The date and time the promotion was updated in ISO 8601 format.

        usage_count : typing.Optional[int]
            Number of times promo code has been used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoCode


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.create_store_promo_rule_promo_code(
            store_id="store_id",
            promo_rule_id="promo_rule_id",
            code="summersale",
            id="id",
            redemption_url="A url that applies promo code directly at checkout or a url that points to sale page or store url",
        )
        """
        _response = self._raw_client.create_store_promo_rule_promo_code(
            store_id,
            promo_rule_id,
            code=code,
            id=id,
            redemption_url=redemption_url,
            created_at_foreign=created_at_foreign,
            enabled=enabled,
            updated_at_foreign=updated_at_foreign,
            usage_count=usage_count,
            request_options=request_options,
        )
        return _response.data

    def get_store_promo_rule_promo_code(
        self,
        store_id: str,
        promo_rule_id: str,
        promo_code_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoCode:
        """
        Get information about a specific promo code.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        promo_code_id : str
            The id for the promo code of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoCode


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.get_store_promo_rule_promo_code(
            store_id="store_id",
            promo_rule_id="promo_rule_id",
            promo_code_id="promo_code_id",
        )
        """
        _response = self._raw_client.get_store_promo_rule_promo_code(
            store_id,
            promo_rule_id,
            promo_code_id,
            fields=fields,
            exclude_fields=exclude_fields,
            request_options=request_options,
        )
        return _response.data

    def delete_store_promo_rule_promo_code(
        self,
        store_id: str,
        promo_rule_id: str,
        promo_code_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a promo code from a store.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        promo_code_id : str
            The id for the promo code of a store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.delete_store_promo_rule_promo_code(
            store_id="store_id",
            promo_rule_id="promo_rule_id",
            promo_code_id="promo_code_id",
        )
        """
        _response = self._raw_client.delete_store_promo_rule_promo_code(
            store_id, promo_rule_id, promo_code_id, request_options=request_options
        )
        return _response.data

    def update_store_promo_rule_promo_code(
        self,
        store_id: str,
        promo_rule_id: str,
        promo_code_id: str,
        *,
        code: typing.Optional[str] = OMIT,
        created_at_foreign: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        redemption_url: typing.Optional[str] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        usage_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoCode:
        """
        Update a promo code.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        promo_code_id : str
            The id for the promo code of a store.

        code : typing.Optional[str]
            The discount code. Restricted to UTF-8 characters with max length 50.

        created_at_foreign : typing.Optional[str]
            The date and time the promotion was created in ISO 8601 format.

        enabled : typing.Optional[bool]
            Whether the promo code is currently enabled.

        id : typing.Optional[str]
            A unique identifier for the promo code. Restricted to UTF-8 characters with max length 50.

        redemption_url : typing.Optional[str]
            The url that should be used in the promotion campaign restricted to UTF-8 characters with max length 2000.

        updated_at_foreign : typing.Optional[str]
            The date and time the promotion was updated in ISO 8601 format.

        usage_count : typing.Optional[int]
            Number of times promo code has been used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoCode


        Examples
        --------
        from mailchimp_marketing import MailchimpClient

        client = MailchimpClient(
            token="YOUR_TOKEN",
        )
        client.ecommerce.update_store_promo_rule_promo_code(
            store_id="store_id",
            promo_rule_id="promo_rule_id",
            promo_code_id="promo_code_id",
        )
        """
        _response = self._raw_client.update_store_promo_rule_promo_code(
            store_id,
            promo_rule_id,
            promo_code_id,
            code=code,
            created_at_foreign=created_at_foreign,
            enabled=enabled,
            id=id,
            redemption_url=redemption_url,
            updated_at_foreign=updated_at_foreign,
            usage_count=usage_count,
            request_options=request_options,
        )
        return _response.data


class AsyncEcommerceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEcommerceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEcommerceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEcommerceClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListEcommerceResponse:
        """
        Get information about the e-commerce endpoint's resources.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEcommerceResponse
            Ecommerce Resource

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def list_orders(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        campaign_id: typing.Optional[str] = None,
        outreach_id: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        has_outreach: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommerceOrder, ListOrdersEcommerceResponse]:
        """
        Get information about an account's orders.

        Parameters
        ----------
        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        campaign_id : typing.Optional[str]
            Restrict results to orders with a specific `campaign_id` value.

        outreach_id : typing.Optional[str]
            Restrict results to orders with a specific `outreach_id` value.

        customer_id : typing.Optional[str]
            Restrict results to orders made by a specific customer.

        has_outreach : typing.Optional[bool]
            Restrict results to orders that have an outreach attached. For example, an email campaign or Facebook ad.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommerceOrder, ListOrdersEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_orders()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_orders(
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            campaign_id=campaign_id,
            outreach_id=outreach_id,
            customer_id=customer_id,
            has_outreach=has_outreach,
            request_options=request_options,
        )

    async def list_stores(
        self,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommerceStore, ListStoresEcommerceResponse]:
        """
        Get information about all stores in the account.

        Parameters
        ----------
        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommerceStore, ListStoresEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_stores()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_stores(
            fields=fields, exclude_fields=exclude_fields, count=count, offset=offset, request_options=request_options
        )

    async def create_store(
        self,
        *,
        currency_code: str,
        id: str,
        list_id: str,
        name: str,
        address: typing.Optional[CreateStoreEcommerceRequestAddress] = OMIT,
        domain: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        is_syncing: typing.Optional[bool] = OMIT,
        money_format: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        primary_locale: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceStore:
        """
        Add a new store to your Mailchimp account.

        Parameters
        ----------
        currency_code : str
            The three-letter ISO 4217 code for the currency that the store accepts.

        id : str
            The unique identifier for the store.

        list_id : str
            The unique identifier for the list associated with the store. The `list_id` for a specific store cannot change.

        name : str
            The name of the store.

        address : typing.Optional[CreateStoreEcommerceRequestAddress]
            The store address.

        domain : typing.Optional[str]
            The store domain. This parameter is required for Connected Sites and Google Ads.

        email_address : typing.Optional[str]
            The email address for the store.

        is_syncing : typing.Optional[bool]
            Whether to disable automations because the store is currently [syncing](https://mailchimp.com/developer/marketing/docs/e-commerce/#pausing-store-automations).

        money_format : typing.Optional[str]
            The currency format for the store. For example: `$`, `£`, etc.

        phone : typing.Optional[str]
            The store phone number.

        platform : typing.Optional[str]
            The e-commerce platform of the store.

        primary_locale : typing.Optional[str]
            The primary locale for the store. For example: `en`, `de`, etc.

        timezone : typing.Optional[str]
            The timezone for the store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceStore


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store(
                currency_code="USD",
                id="example_store",
                list_id="1a2df69511",
                name="Freddie's Cat Hat Emporium",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store(
            currency_code=currency_code,
            id=id,
            list_id=list_id,
            name=name,
            address=address,
            domain=domain,
            email_address=email_address,
            is_syncing=is_syncing,
            money_format=money_format,
            phone=phone,
            platform=platform,
            primary_locale=primary_locale,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    async def get_store(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceStore:
        """
        Get information about a specific store.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceStore


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store(
                store_id="store_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store(
            store_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def delete_store(self, store_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a store. Deleting a store will also delete any associated subresources, including Customers, Orders, Products, and Carts.

        Parameters
        ----------
        store_id : str
            The store id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store(
                store_id="store_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store(store_id, request_options=request_options)
        return _response.data

    async def update_store(
        self,
        store_id: str,
        *,
        address: typing.Optional[UpdateStoreEcommerceRequestAddress] = OMIT,
        currency_code: typing.Optional[str] = OMIT,
        domain: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        is_syncing: typing.Optional[bool] = OMIT,
        money_format: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        platform: typing.Optional[str] = OMIT,
        primary_locale: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceStore:
        """
        Update a store.

        Parameters
        ----------
        store_id : str
            The store id.

        address : typing.Optional[UpdateStoreEcommerceRequestAddress]
            The store address.

        currency_code : typing.Optional[str]
            The three-letter ISO 4217 code for the currency that the store accepts.

        domain : typing.Optional[str]
            The store domain.

        email_address : typing.Optional[str]
            The email address for the store.

        is_syncing : typing.Optional[bool]
            Whether to disable automations because the store is currently [syncing](https://mailchimp.com/developer/marketing/docs/e-commerce/#pausing-store-automations).

        money_format : typing.Optional[str]
            The currency format for the store. For example: `$`, `£`, etc.

        name : typing.Optional[str]
            The name of the store.

        phone : typing.Optional[str]
            The store phone number.

        platform : typing.Optional[str]
            The e-commerce platform of the store.

        primary_locale : typing.Optional[str]
            The primary locale for the store. For example: `en`, `de`, etc.

        timezone : typing.Optional[str]
            The timezone for the store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceStore


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store(
                store_id="store_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store(
            store_id,
            address=address,
            currency_code=currency_code,
            domain=domain,
            email_address=email_address,
            is_syncing=is_syncing,
            money_format=money_format,
            name=name,
            phone=phone,
            platform=platform,
            primary_locale=primary_locale,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    async def list_store_carts(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommerceCart, ListStoreCartsEcommerceResponse]:
        """
        Get information about a store's carts.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommerceCart, ListStoreCartsEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_store_carts(
                store_id="store_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_store_carts(
            store_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    async def create_store_cart(
        self,
        store_id: str,
        *,
        currency_code: str,
        customer: EcommerceStoresCartsPost,
        id: CreateStoreCartEcommerceRequestId,
        lines: typing.Sequence[CreateStoreCartEcommerceRequestLinesItem],
        order_total: CreateStoreCartEcommerceRequestOrderTotal,
        campaign_id: typing.Optional[str] = OMIT,
        checkout_url: typing.Optional[str] = OMIT,
        tax_total: typing.Optional[CreateStoreCartEcommerceRequestTaxTotal] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCart:
        """
        Add a new cart to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        currency_code : str
            The three-letter ISO 4217 code for the currency that the cart uses.

        customer : EcommerceStoresCartsPost

        id : CreateStoreCartEcommerceRequestId
            A unique identifier for the cart.

        lines : typing.Sequence[CreateStoreCartEcommerceRequestLinesItem]
            An array of the cart's line items.

        order_total : CreateStoreCartEcommerceRequestOrderTotal

        campaign_id : typing.Optional[str]
            A string that uniquely identifies the campaign for a cart.

        checkout_url : typing.Optional[str]
            The URL for the cart. This parameter is required for [Abandoned Cart](https://mailchimp.com/help/create-a-classic-abandoned-cart-email/) automations.

        tax_total : typing.Optional[CreateStoreCartEcommerceRequestTaxTotal]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCart


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient, EcommerceStoresCartsPost
        from mailchimp_marketing.ecommerce import (
            CreateStoreCartEcommerceRequestLinesItem,
        )

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store_cart(
                store_id="store_id",
                currency_code="currency_code",
                customer=EcommerceStoresCartsPost(
                    id="id",
                ),
                id="id",
                lines=[
                    CreateStoreCartEcommerceRequestLinesItem(
                        id="id",
                        price=1.1,
                        product_id="product_id",
                        product_variant_id="product_variant_id",
                        quantity=1,
                    )
                ],
                order_total=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store_cart(
            store_id,
            currency_code=currency_code,
            customer=customer,
            id=id,
            lines=lines,
            order_total=order_total,
            campaign_id=campaign_id,
            checkout_url=checkout_url,
            tax_total=tax_total,
            request_options=request_options,
        )
        return _response.data

    async def get_store_cart(
        self,
        store_id: str,
        cart_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCart:
        """
        Get information about a specific cart.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCart


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store_cart(
                store_id="store_id",
                cart_id="cart_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store_cart(
            store_id, cart_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def delete_store_cart(
        self, store_id: str, cart_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a cart.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store_cart(
                store_id="store_id",
                cart_id="cart_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store_cart(store_id, cart_id, request_options=request_options)
        return _response.data

    async def update_store_cart(
        self,
        store_id: str,
        cart_id: str,
        *,
        campaign_id: typing.Optional[str] = OMIT,
        checkout_url: typing.Optional[str] = OMIT,
        currency_code: typing.Optional[str] = OMIT,
        customer: typing.Optional[EcommerceStoresCartsPatch] = OMIT,
        id: typing.Optional[UpdateStoreCartEcommerceRequestId] = OMIT,
        lines: typing.Optional[typing.Sequence[UpdateStoreCartEcommerceRequestLinesItem]] = OMIT,
        order_total: typing.Optional[UpdateStoreCartEcommerceRequestOrderTotal] = OMIT,
        tax_total: typing.Optional[UpdateStoreCartEcommerceRequestTaxTotal] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCart:
        """
        Update a specific cart.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        campaign_id : typing.Optional[str]
            A string that uniquely identifies the campaign associated with a cart.

        checkout_url : typing.Optional[str]
            The URL for the cart. This parameter is required for [Abandoned Cart](https://mailchimp.com/help/create-a-classic-abandoned-cart-email/) automations.

        currency_code : typing.Optional[str]
            The three-letter ISO 4217 code for the currency that the cart uses.

        customer : typing.Optional[EcommerceStoresCartsPatch]

        id : typing.Optional[UpdateStoreCartEcommerceRequestId]
            A unique identifier for the cart.

        lines : typing.Optional[typing.Sequence[UpdateStoreCartEcommerceRequestLinesItem]]
            An array of the cart's line items.

        order_total : typing.Optional[UpdateStoreCartEcommerceRequestOrderTotal]

        tax_total : typing.Optional[UpdateStoreCartEcommerceRequestTaxTotal]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCart


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store_cart(
                store_id="store_id",
                cart_id="cart_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store_cart(
            store_id,
            cart_id,
            campaign_id=campaign_id,
            checkout_url=checkout_url,
            currency_code=currency_code,
            customer=customer,
            id=id,
            lines=lines,
            order_total=order_total,
            tax_total=tax_total,
            request_options=request_options,
        )
        return _response.data

    async def list_store_cart_lines(
        self,
        store_id: str,
        cart_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommerceCartLineItem, ListStoreCartLinesEcommerceResponse]:
        """
        Get information about a cart's line items.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommerceCartLineItem, ListStoreCartLinesEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_store_cart_lines(
                store_id="store_id",
                cart_id="cart_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_store_cart_lines(
            store_id,
            cart_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    async def create_store_cart_line(
        self,
        store_id: str,
        cart_id: str,
        *,
        id: str,
        price: CreateStoreCartLineEcommerceRequestPrice,
        product_id: str,
        product_variant_id: str,
        quantity: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCartLineItem:
        """
        Add a new line item to an existing cart.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        id : str
            A unique identifier for the cart line item.

        price : CreateStoreCartLineEcommerceRequestPrice

        product_id : str
            A unique identifier for the product associated with the cart line item.

        product_variant_id : str
            A unique identifier for the product variant associated with the cart line item.

        quantity : int
            The quantity of a cart line item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCartLineItem


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store_cart_line(
                store_id="store_id",
                cart_id="cart_id",
                id="id",
                price=1.1,
                product_id="product_id",
                product_variant_id="product_variant_id",
                quantity=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store_cart_line(
            store_id,
            cart_id,
            id=id,
            price=price,
            product_id=product_id,
            product_variant_id=product_variant_id,
            quantity=quantity,
            request_options=request_options,
        )
        return _response.data

    async def get_store_cart_line(
        self,
        store_id: str,
        cart_id: str,
        line_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCartLineItem:
        """
        Get information about a specific cart line item.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        line_id : str
            The id for the line item of a cart.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCartLineItem


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store_cart_line(
                store_id="store_id",
                cart_id="cart_id",
                line_id="line_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store_cart_line(
            store_id, cart_id, line_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def delete_store_cart_line(
        self, store_id: str, cart_id: str, line_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a specific cart line item.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        line_id : str
            The id for the line item of a cart.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store_cart_line(
                store_id="store_id",
                cart_id="cart_id",
                line_id="line_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store_cart_line(
            store_id, cart_id, line_id, request_options=request_options
        )
        return _response.data

    async def update_store_cart_line(
        self,
        store_id: str,
        cart_id: str,
        line_id: str,
        *,
        price: typing.Optional[UpdateStoreCartLineEcommerceRequestPrice] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        product_variant_id: typing.Optional[str] = OMIT,
        quantity: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCartLineItem:
        """
        Update a specific cart line item.

        Parameters
        ----------
        store_id : str
            The store id.

        cart_id : str
            The id for the cart.

        line_id : str
            The id for the line item of a cart.

        price : typing.Optional[UpdateStoreCartLineEcommerceRequestPrice]

        product_id : typing.Optional[str]
            A unique identifier for the product associated with the cart line item.

        product_variant_id : typing.Optional[str]
            A unique identifier for the product variant associated with the cart line item.

        quantity : typing.Optional[int]
            The quantity of a cart line item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCartLineItem


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store_cart_line(
                store_id="store_id",
                cart_id="cart_id",
                line_id="line_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store_cart_line(
            store_id,
            cart_id,
            line_id,
            price=price,
            product_id=product_id,
            product_variant_id=product_variant_id,
            quantity=quantity,
            request_options=request_options,
        )
        return _response.data

    async def list_store_customers(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        email_address: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommerceCustomer, ListStoreCustomersEcommerceResponse]:
        """
        Get information about a store's customers.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        email_address : typing.Optional[str]
            Restrict the response to customers with the email address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommerceCustomer, ListStoreCustomersEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_store_customers(
                store_id="store_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_store_customers(
            store_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            email_address=email_address,
            request_options=request_options,
        )

    async def create_store_customer(
        self,
        store_id: str,
        *,
        id: str,
        opt_in_status: bool,
        address: typing.Optional[CreateStoreCustomerEcommerceRequestAddress] = OMIT,
        company: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        sms_phone_number: typing.Optional[str] = OMIT,
        total_spent: typing.Optional[CreateStoreCustomerEcommerceRequestTotalSpent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCustomer:
        """
        Add a new customer to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        id : str
            A unique identifier for the customer. Limited to 50 characters.

        opt_in_status : bool
            The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing Mailchimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your Mailchimp list [will be added as `Transactional` members](https://mailchimp.com/developer/marketing/docs/e-commerce/#customers).

        address : typing.Optional[CreateStoreCustomerEcommerceRequestAddress]
            The customer's address.

        company : typing.Optional[str]
            The customer's company.

        email_address : typing.Optional[str]
            The customer's email address.

        first_name : typing.Optional[str]
            The customer's first name.

        last_name : typing.Optional[str]
            The customer's last name.

        sms_phone_number : typing.Optional[str]
            A US phone number for SMS contact.

        total_spent : typing.Optional[CreateStoreCustomerEcommerceRequestTotalSpent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCustomer


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store_customer(
                store_id="store_id",
                id="id",
                opt_in_status=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store_customer(
            store_id,
            id=id,
            opt_in_status=opt_in_status,
            address=address,
            company=company,
            email_address=email_address,
            first_name=first_name,
            last_name=last_name,
            sms_phone_number=sms_phone_number,
            total_spent=total_spent,
            request_options=request_options,
        )
        return _response.data

    async def get_store_customer(
        self,
        store_id: str,
        customer_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCustomer:
        """
        Get information about a specific customer.

        Parameters
        ----------
        store_id : str
            The store id.

        customer_id : str
            The id for the customer of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCustomer


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store_customer(
                store_id="store_id",
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store_customer(
            store_id, customer_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def upsert_store_customer(
        self,
        store_id: str,
        customer_id: str,
        *,
        address: typing.Optional[UpsertStoreCustomerEcommerceRequestAddress] = OMIT,
        company: typing.Optional[str] = OMIT,
        email_address: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        opt_in_status: typing.Optional[bool] = OMIT,
        sms_phone_number: typing.Optional[str] = OMIT,
        total_spent: typing.Optional[UpsertStoreCustomerEcommerceRequestTotalSpent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCustomer:
        """
        Add or update a customer.

        Parameters
        ----------
        store_id : str
            The store id.

        customer_id : str
            The id for the customer of a store.

        address : typing.Optional[UpsertStoreCustomerEcommerceRequestAddress]
            The customer's address.

        company : typing.Optional[str]
            The customer's company.

        email_address : typing.Optional[str]
            The customer's email address.

        first_name : typing.Optional[str]
            The customer's first name.

        id : typing.Optional[str]
            A unique identifier for the customer. Limited to 50 characters.

        last_name : typing.Optional[str]
            The customer's last name.

        opt_in_status : typing.Optional[bool]
            The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing Mailchimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your Mailchimp list [will be added as `Transactional` members](https://mailchimp.com/developer/marketing/docs/e-commerce/#customers).

        sms_phone_number : typing.Optional[str]
            A US phone number for SMS contact.

        total_spent : typing.Optional[UpsertStoreCustomerEcommerceRequestTotalSpent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCustomer


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.upsert_store_customer(
                store_id="store_id",
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_store_customer(
            store_id,
            customer_id,
            address=address,
            company=company,
            email_address=email_address,
            first_name=first_name,
            id=id,
            last_name=last_name,
            opt_in_status=opt_in_status,
            sms_phone_number=sms_phone_number,
            total_spent=total_spent,
            request_options=request_options,
        )
        return _response.data

    async def delete_store_customer(
        self, store_id: str, customer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a customer from a store.

        Parameters
        ----------
        store_id : str
            The store id.

        customer_id : str
            The id for the customer of a store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store_customer(
                store_id="store_id",
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store_customer(store_id, customer_id, request_options=request_options)
        return _response.data

    async def update_store_customer(
        self,
        store_id: str,
        customer_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        address: typing.Optional[EcommerceStoresCartsPatchAddress] = OMIT,
        company: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        opt_in_status: typing.Optional[bool] = OMIT,
        total_spent: typing.Optional[EcommerceStoresCartsPatchTotalSpent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceCustomer:
        """
        Update a customer.

        Parameters
        ----------
        store_id : str
            The store id.

        customer_id : str
            The id for the customer of a store.

        id : typing.Optional[str]
            A unique identifier for the customer. Limited to 50 characters.

        address : typing.Optional[EcommerceStoresCartsPatchAddress]
            The customer's address.

        company : typing.Optional[str]
            The customer's company.

        first_name : typing.Optional[str]
            The customer's first name.

        last_name : typing.Optional[str]
            The customer's last name.

        opt_in_status : typing.Optional[bool]
            The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing Mailchimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your Mailchimp list [will be added as `Transactional` members](https://mailchimp.com/developer/marketing/docs/e-commerce/#customers).

        total_spent : typing.Optional[EcommerceStoresCartsPatchTotalSpent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceCustomer


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store_customer(
                store_id="store_id",
                customer_id="customer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store_customer(
            store_id,
            customer_id,
            id=id,
            address=address,
            company=company,
            first_name=first_name,
            last_name=last_name,
            opt_in_status=opt_in_status,
            total_spent=total_spent,
            request_options=request_options,
        )
        return _response.data

    async def list_store_orders(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        customer_id: typing.Optional[str] = None,
        has_outreach: typing.Optional[bool] = None,
        campaign_id: typing.Optional[str] = None,
        outreach_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommerceOrder, ListStoreOrdersEcommerceResponse]:
        """
        Get information about a store's orders.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        customer_id : typing.Optional[str]
            Restrict results to orders made by a specific customer.

        has_outreach : typing.Optional[bool]
            Restrict results to orders that have an outreach attached. For example, an email campaign or Facebook ad.

        campaign_id : typing.Optional[str]
            Restrict results to orders with a specific `campaign_id` value.

        outreach_id : typing.Optional[str]
            Restrict results to orders with a specific `outreach_id` value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommerceOrder, ListStoreOrdersEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_store_orders(
                store_id="store_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_store_orders(
            store_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            customer_id=customer_id,
            has_outreach=has_outreach,
            campaign_id=campaign_id,
            outreach_id=outreach_id,
            request_options=request_options,
        )

    async def create_store_order(
        self,
        store_id: str,
        *,
        currency_code: str,
        customer: EcommerceStoresCartsPost,
        id: str,
        lines: typing.Sequence[CreateStoreOrderEcommerceRequestLinesItem],
        order_total: CreateStoreOrderEcommerceRequestOrderTotal,
        billing_address: typing.Optional[CreateStoreOrderEcommerceRequestBillingAddress] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        cart_id: typing.Optional[CreateStoreOrderEcommerceRequestCartId] = OMIT,
        cancelled_at_foreign: typing.Optional[str] = OMIT,
        discount_total: typing.Optional[CreateStoreOrderEcommerceRequestDiscountTotal] = OMIT,
        financial_status: typing.Optional[str] = OMIT,
        fulfillment_status: typing.Optional[str] = OMIT,
        landing_site: typing.Optional[str] = OMIT,
        order_url: typing.Optional[str] = OMIT,
        outreach: typing.Optional[CreateStoreOrderEcommerceRequestOutreach] = OMIT,
        processed_at_foreign: typing.Optional[str] = OMIT,
        promos: typing.Optional[typing.Sequence[CreateStoreOrderEcommerceRequestPromosItem]] = OMIT,
        shipping_address: typing.Optional[CreateStoreOrderEcommerceRequestShippingAddress] = OMIT,
        shipping_total: typing.Optional[CreateStoreOrderEcommerceRequestShippingTotal] = OMIT,
        tax_total: typing.Optional[CreateStoreOrderEcommerceRequestTaxTotal] = OMIT,
        tracking_carrier: typing.Optional[str] = OMIT,
        tracking_code: typing.Optional[CreateStoreOrderEcommerceRequestTrackingCode] = OMIT,
        tracking_number: typing.Optional[str] = OMIT,
        tracking_url: typing.Optional[str] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrder:
        """
        Add a new order to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        currency_code : str
            The three-letter ISO 4217 code for the currency that the store accepts.

        customer : EcommerceStoresCartsPost

        id : str
            A unique identifier for the order.

        lines : typing.Sequence[CreateStoreOrderEcommerceRequestLinesItem]
            An array of the order's line items.

        order_total : CreateStoreOrderEcommerceRequestOrderTotal

        billing_address : typing.Optional[CreateStoreOrderEcommerceRequestBillingAddress]
            The billing address for the order.

        campaign_id : typing.Optional[str]
            A string that uniquely identifies the campaign for an order.

        cart_id : typing.Optional[CreateStoreOrderEcommerceRequestCartId]
            A cart id that the order was placed for.

        cancelled_at_foreign : typing.Optional[str]
            The date and time the order was cancelled in ISO 8601 format. Note: passing a value for this parameter will cancel the order being created.

        discount_total : typing.Optional[CreateStoreOrderEcommerceRequestDiscountTotal]

        financial_status : typing.Optional[str]
            The order status. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).

        fulfillment_status : typing.Optional[str]
            The fulfillment status for the order. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).

        landing_site : typing.Optional[str]
            The URL for the page where the buyer landed when entering the shop.

        order_url : typing.Optional[str]
            The URL for the order.

        outreach : typing.Optional[CreateStoreOrderEcommerceRequestOutreach]
            The outreach associated with this order. For example, an email campaign or Facebook ad.

        processed_at_foreign : typing.Optional[str]
            The date and time the order was processed in ISO 8601 format.

        promos : typing.Optional[typing.Sequence[CreateStoreOrderEcommerceRequestPromosItem]]
            The promo codes applied on the order

        shipping_address : typing.Optional[CreateStoreOrderEcommerceRequestShippingAddress]
            The shipping address for the order.

        shipping_total : typing.Optional[CreateStoreOrderEcommerceRequestShippingTotal]

        tax_total : typing.Optional[CreateStoreOrderEcommerceRequestTaxTotal]

        tracking_carrier : typing.Optional[str]
            The tracking carrier associated with the order.

        tracking_code : typing.Optional[CreateStoreOrderEcommerceRequestTrackingCode]
            The Mailchimp tracking code for the order. Uses the 'mc_tc' parameter in E-Commerce tracking URLs.

        tracking_number : typing.Optional[str]
            The tracking number associated with the order.

        tracking_url : typing.Optional[str]
            The tracking URL associated with the order.

        updated_at_foreign : typing.Optional[str]
            The date and time the order was updated in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrder


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient, EcommerceStoresCartsPost
        from mailchimp_marketing.ecommerce import (
            CreateStoreOrderEcommerceRequestLinesItem,
        )

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store_order(
                store_id="store_id",
                currency_code="currency_code",
                customer=EcommerceStoresCartsPost(
                    id="id",
                ),
                id="id",
                lines=[
                    CreateStoreOrderEcommerceRequestLinesItem(
                        id="id",
                        price=1.1,
                        product_id="product_id",
                        product_variant_id="product_variant_id",
                        quantity=1,
                    )
                ],
                order_total=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store_order(
            store_id,
            currency_code=currency_code,
            customer=customer,
            id=id,
            lines=lines,
            order_total=order_total,
            billing_address=billing_address,
            campaign_id=campaign_id,
            cart_id=cart_id,
            cancelled_at_foreign=cancelled_at_foreign,
            discount_total=discount_total,
            financial_status=financial_status,
            fulfillment_status=fulfillment_status,
            landing_site=landing_site,
            order_url=order_url,
            outreach=outreach,
            processed_at_foreign=processed_at_foreign,
            promos=promos,
            shipping_address=shipping_address,
            shipping_total=shipping_total,
            tax_total=tax_total,
            tracking_carrier=tracking_carrier,
            tracking_code=tracking_code,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            updated_at_foreign=updated_at_foreign,
            request_options=request_options,
        )
        return _response.data

    async def get_store_order(
        self,
        store_id: str,
        order_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrder:
        """
        Get information about a specific order.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrder


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store_order(
                store_id="store_id",
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store_order(
            store_id, order_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def delete_store_order(
        self, store_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an order.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store_order(
                store_id="store_id",
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store_order(store_id, order_id, request_options=request_options)
        return _response.data

    async def update_store_order(
        self,
        store_id: str,
        order_id: str,
        *,
        billing_address: typing.Optional[UpdateStoreOrderEcommerceRequestBillingAddress] = OMIT,
        campaign_id: typing.Optional[str] = OMIT,
        cart_id: typing.Optional[UpdateStoreOrderEcommerceRequestCartId] = OMIT,
        cancelled_at_foreign: typing.Optional[str] = OMIT,
        currency_code: typing.Optional[str] = OMIT,
        customer: typing.Optional[EcommerceStoresCartsPatch] = OMIT,
        discount_total: typing.Optional[UpdateStoreOrderEcommerceRequestDiscountTotal] = OMIT,
        financial_status: typing.Optional[str] = OMIT,
        fulfillment_status: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        landing_site: typing.Optional[str] = OMIT,
        lines: typing.Optional[typing.Sequence[UpdateStoreOrderEcommerceRequestLinesItem]] = OMIT,
        order_total: typing.Optional[UpdateStoreOrderEcommerceRequestOrderTotal] = OMIT,
        order_url: typing.Optional[str] = OMIT,
        outreach: typing.Optional[UpdateStoreOrderEcommerceRequestOutreach] = OMIT,
        processed_at_foreign: typing.Optional[str] = OMIT,
        promos: typing.Optional[typing.Sequence[UpdateStoreOrderEcommerceRequestPromosItem]] = OMIT,
        shipping_address: typing.Optional[UpdateStoreOrderEcommerceRequestShippingAddress] = OMIT,
        shipping_total: typing.Optional[UpdateStoreOrderEcommerceRequestShippingTotal] = OMIT,
        tax_total: typing.Optional[UpdateStoreOrderEcommerceRequestTaxTotal] = OMIT,
        tracking_carrier: typing.Optional[str] = OMIT,
        tracking_code: typing.Optional[UpdateStoreOrderEcommerceRequestTrackingCode] = OMIT,
        tracking_number: typing.Optional[str] = OMIT,
        tracking_url: typing.Optional[str] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrder:
        """
        Update a specific order.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        billing_address : typing.Optional[UpdateStoreOrderEcommerceRequestBillingAddress]
            The billing address for the order.

        campaign_id : typing.Optional[str]
            A string that uniquely identifies the campaign associated with an order.

        cart_id : typing.Optional[UpdateStoreOrderEcommerceRequestCartId]
            A cart id that the order was placed for.

        cancelled_at_foreign : typing.Optional[str]
            The date and time the order was cancelled in ISO 8601 format. Note: passing a value for this parameter will cancel the order being edited.

        currency_code : typing.Optional[str]
            The three-letter ISO 4217 code for the currency that the store accepts.

        customer : typing.Optional[EcommerceStoresCartsPatch]

        discount_total : typing.Optional[UpdateStoreOrderEcommerceRequestDiscountTotal]

        financial_status : typing.Optional[str]
            The order status. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).

        fulfillment_status : typing.Optional[str]
            The fulfillment status for the order. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).

        id : typing.Optional[str]
            A unique identifier for the order.

        landing_site : typing.Optional[str]
            The URL for the page where the buyer landed when entering the shop.

        lines : typing.Optional[typing.Sequence[UpdateStoreOrderEcommerceRequestLinesItem]]
            An array of the order's line items.

        order_total : typing.Optional[UpdateStoreOrderEcommerceRequestOrderTotal]

        order_url : typing.Optional[str]
            The URL for the order.

        outreach : typing.Optional[UpdateStoreOrderEcommerceRequestOutreach]
            The outreach associated with this order. For example, an email campaign or Facebook ad.

        processed_at_foreign : typing.Optional[str]
            The date and time the order was processed in ISO 8601 format.

        promos : typing.Optional[typing.Sequence[UpdateStoreOrderEcommerceRequestPromosItem]]
            The promo codes applied on the order. Note: Patch will completely replace the value of promos with the new one provided.

        shipping_address : typing.Optional[UpdateStoreOrderEcommerceRequestShippingAddress]
            The shipping address for the order.

        shipping_total : typing.Optional[UpdateStoreOrderEcommerceRequestShippingTotal]

        tax_total : typing.Optional[UpdateStoreOrderEcommerceRequestTaxTotal]

        tracking_carrier : typing.Optional[str]
            The tracking carrier associated with the order.

        tracking_code : typing.Optional[UpdateStoreOrderEcommerceRequestTrackingCode]
            The Mailchimp tracking code for the order. Uses the 'mc_tc' parameter in E-Commerce tracking URLs.

        tracking_number : typing.Optional[str]
            The tracking number associated with the order.

        tracking_url : typing.Optional[str]
            The tracking URL associated with the order.

        updated_at_foreign : typing.Optional[str]
            The date and time the order was updated in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrder


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store_order(
                store_id="store_id",
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store_order(
            store_id,
            order_id,
            billing_address=billing_address,
            campaign_id=campaign_id,
            cart_id=cart_id,
            cancelled_at_foreign=cancelled_at_foreign,
            currency_code=currency_code,
            customer=customer,
            discount_total=discount_total,
            financial_status=financial_status,
            fulfillment_status=fulfillment_status,
            id=id,
            landing_site=landing_site,
            lines=lines,
            order_total=order_total,
            order_url=order_url,
            outreach=outreach,
            processed_at_foreign=processed_at_foreign,
            promos=promos,
            shipping_address=shipping_address,
            shipping_total=shipping_total,
            tax_total=tax_total,
            tracking_carrier=tracking_carrier,
            tracking_code=tracking_code,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            updated_at_foreign=updated_at_foreign,
            request_options=request_options,
        )
        return _response.data

    async def list_store_order_lines(
        self,
        store_id: str,
        order_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommerceOrderLineItem, ListStoreOrderLinesEcommerceResponse]:
        """
        Get information about an order's line items.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommerceOrderLineItem, ListStoreOrderLinesEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_store_order_lines(
                store_id="store_id",
                order_id="order_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_store_order_lines(
            store_id,
            order_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    async def create_store_order_line(
        self,
        store_id: str,
        order_id: str,
        *,
        id: str,
        price: CreateStoreOrderLineEcommerceRequestPrice,
        product_id: str,
        product_variant_id: str,
        quantity: int,
        discount: typing.Optional[CreateStoreOrderLineEcommerceRequestDiscount] = OMIT,
        product: typing.Optional[EcommerceStoresOrdersPost] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrderLineItem:
        """
        Add a new line item to an existing order.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        id : str
            A unique identifier for the order line item.

        price : CreateStoreOrderLineEcommerceRequestPrice

        product_id : str
            A unique identifier for the product associated with the order line item.

        product_variant_id : str
            A unique identifier for the product variant associated with the order line item.

        quantity : int
            The quantity of an order line item.

        discount : typing.Optional[CreateStoreOrderLineEcommerceRequestDiscount]

        product : typing.Optional[EcommerceStoresOrdersPost]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrderLineItem


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store_order_line(
                store_id="store_id",
                order_id="order_id",
                id="id",
                price=1.1,
                product_id="product_id",
                product_variant_id="product_variant_id",
                quantity=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store_order_line(
            store_id,
            order_id,
            id=id,
            price=price,
            product_id=product_id,
            product_variant_id=product_variant_id,
            quantity=quantity,
            discount=discount,
            product=product,
            request_options=request_options,
        )
        return _response.data

    async def get_store_order_line(
        self,
        store_id: str,
        order_id: str,
        line_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrderLineItem:
        """
        Get information about a specific order line item.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        line_id : str
            The id for the line item of an order.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrderLineItem


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store_order_line(
                store_id="store_id",
                order_id="order_id",
                line_id="line_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store_order_line(
            store_id, order_id, line_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def delete_store_order_line(
        self, store_id: str, order_id: str, line_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a specific order line item.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        line_id : str
            The id for the line item of an order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store_order_line(
                store_id="store_id",
                order_id="order_id",
                line_id="line_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store_order_line(
            store_id, order_id, line_id, request_options=request_options
        )
        return _response.data

    async def update_store_order_line(
        self,
        store_id: str,
        order_id: str,
        line_id: str,
        *,
        discount: typing.Optional[UpdateStoreOrderLineEcommerceRequestDiscount] = OMIT,
        id: typing.Optional[str] = OMIT,
        price: typing.Optional[UpdateStoreOrderLineEcommerceRequestPrice] = OMIT,
        product_id: typing.Optional[str] = OMIT,
        product_variant_id: typing.Optional[str] = OMIT,
        quantity: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceOrderLineItem:
        """
        Update a specific order line item.

        Parameters
        ----------
        store_id : str
            The store id.

        order_id : str
            The id for the order in a store.

        line_id : str
            The id for the line item of an order.

        discount : typing.Optional[UpdateStoreOrderLineEcommerceRequestDiscount]

        id : typing.Optional[str]
            A unique identifier for the order line item.

        price : typing.Optional[UpdateStoreOrderLineEcommerceRequestPrice]

        product_id : typing.Optional[str]
            A unique identifier for the product associated with the order line item.

        product_variant_id : typing.Optional[str]
            A unique identifier for the product variant associated with the order line item.

        quantity : typing.Optional[int]
            The quantity of an order line item.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceOrderLineItem


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store_order_line(
                store_id="store_id",
                order_id="order_id",
                line_id="line_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store_order_line(
            store_id,
            order_id,
            line_id,
            discount=discount,
            id=id,
            price=price,
            product_id=product_id,
            product_variant_id=product_variant_id,
            quantity=quantity,
            request_options=request_options,
        )
        return _response.data

    async def list_store_products(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommerceProduct, ListStoreProductsEcommerceResponse]:
        """
        Get information about a store's products.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommerceProduct, ListStoreProductsEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_store_products(
                store_id="store_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_store_products(
            store_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    async def create_store_product(
        self,
        store_id: str,
        *,
        id: EcommerceStoresOrdersPostId,
        title: str,
        variants: typing.Sequence[EcommerceStoresOrdersPostVariantsItem],
        description: typing.Optional[str] = OMIT,
        handle: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        images: typing.Optional[typing.Sequence[EcommerceStoresOrdersPostImagesItem]] = OMIT,
        published_at_foreign: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        vendor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProduct:
        """
        Add a new product to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        id : EcommerceStoresOrdersPostId
            A unique identifier for the product.

        title : str
            The title of a product.

        variants : typing.Sequence[EcommerceStoresOrdersPostVariantsItem]
            An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.

        description : typing.Optional[str]
            The description of a product.

        handle : typing.Optional[str]
            The handle of a product.

        image_url : typing.Optional[str]
            The image URL for a product.

        images : typing.Optional[typing.Sequence[EcommerceStoresOrdersPostImagesItem]]
            An array of the product's images.

        published_at_foreign : typing.Optional[str]
            The date and time the product was published.

        type : typing.Optional[str]
            The type of product.

        url : typing.Optional[str]
            The URL for a product.

        vendor : typing.Optional[str]
            The vendor for a product.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProduct


        Examples
        --------
        import asyncio

        from mailchimp_marketing import (
            AsyncMailchimpClient,
            EcommerceStoresOrdersPostVariantsItem,
        )

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store_product(
                store_id="store_id",
                id="id",
                title="Cat Hat",
                variants=[
                    EcommerceStoresOrdersPostVariantsItem(
                        id="id",
                        title="Cat Hat",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store_product(
            store_id,
            id=id,
            title=title,
            variants=variants,
            description=description,
            handle=handle,
            image_url=image_url,
            images=images,
            published_at_foreign=published_at_foreign,
            type=type,
            url=url,
            vendor=vendor,
            request_options=request_options,
        )
        return _response.data

    async def get_store_product(
        self,
        store_id: str,
        product_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProduct:
        """
        Get information about a specific product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProduct


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store_product(
                store_id="store_id",
                product_id="product_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store_product(
            store_id, product_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def upsert_store_product(
        self,
        store_id: str,
        product_id: str,
        *,
        id: UpsertStoreProductEcommerceRequestId,
        description: typing.Optional[str] = OMIT,
        handle: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        images: typing.Optional[typing.Sequence[UpsertStoreProductEcommerceRequestImagesItem]] = OMIT,
        published_at_foreign: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        variants: typing.Optional[typing.Sequence[UpsertStoreProductEcommerceRequestVariantsItem]] = OMIT,
        vendor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProduct:
        """
        Update a specific product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        id : UpsertStoreProductEcommerceRequestId
            A unique identifier for the product.

        description : typing.Optional[str]
            The description of a product.

        handle : typing.Optional[str]
            The handle of a product.

        image_url : typing.Optional[str]
            The image URL for a product.

        images : typing.Optional[typing.Sequence[UpsertStoreProductEcommerceRequestImagesItem]]
            An array of the product's images.

        published_at_foreign : typing.Optional[str]
            The date and time the product was published.

        title : typing.Optional[str]
            The title of a product.

        type : typing.Optional[str]
            The type of product.

        url : typing.Optional[str]
            The URL for a product.

        variants : typing.Optional[typing.Sequence[UpsertStoreProductEcommerceRequestVariantsItem]]
            An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.

        vendor : typing.Optional[str]
            The vendor for a product.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProduct


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.upsert_store_product(
                store_id="store_id",
                product_id="product_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_store_product(
            store_id,
            product_id,
            id=id,
            description=description,
            handle=handle,
            image_url=image_url,
            images=images,
            published_at_foreign=published_at_foreign,
            title=title,
            type=type,
            url=url,
            variants=variants,
            vendor=vendor,
            request_options=request_options,
        )
        return _response.data

    async def delete_store_product(
        self, store_id: str, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store_product(
                store_id="store_id",
                product_id="product_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store_product(store_id, product_id, request_options=request_options)
        return _response.data

    async def update_store_product(
        self,
        store_id: str,
        product_id: str,
        *,
        description: typing.Optional[str] = OMIT,
        handle: typing.Optional[str] = OMIT,
        id: typing.Optional[UpdateStoreProductEcommerceRequestId] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        images: typing.Optional[typing.Sequence[UpdateStoreProductEcommerceRequestImagesItem]] = OMIT,
        published_at_foreign: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        variants: typing.Optional[typing.Sequence[UpdateStoreProductEcommerceRequestVariantsItem]] = OMIT,
        vendor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProduct:
        """
        Update a specific product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        description : typing.Optional[str]
            The description of a product.

        handle : typing.Optional[str]
            The handle of a product.

        id : typing.Optional[UpdateStoreProductEcommerceRequestId]
            A unique identifier for the product.

        image_url : typing.Optional[str]
            The image URL for a product.

        images : typing.Optional[typing.Sequence[UpdateStoreProductEcommerceRequestImagesItem]]
            An array of the product's images.

        published_at_foreign : typing.Optional[str]
            The date and time the product was published in ISO 8601 format.

        title : typing.Optional[str]
            The title of a product.

        type : typing.Optional[str]
            The type of product.

        url : typing.Optional[str]
            The URL for a product.

        variants : typing.Optional[typing.Sequence[UpdateStoreProductEcommerceRequestVariantsItem]]
            An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.

        vendor : typing.Optional[str]
            The vendor for a product.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProduct


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store_product(
                store_id="store_id",
                product_id="product_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store_product(
            store_id,
            product_id,
            description=description,
            handle=handle,
            id=id,
            image_url=image_url,
            images=images,
            published_at_foreign=published_at_foreign,
            title=title,
            type=type,
            url=url,
            variants=variants,
            vendor=vendor,
            request_options=request_options,
        )
        return _response.data

    async def list_store_product_images(
        self,
        store_id: str,
        product_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ListStoreProductImagesEcommerceResponseImagesItem, ListStoreProductImagesEcommerceResponse]:
        """
        Get information about a product's images.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ListStoreProductImagesEcommerceResponseImagesItem, ListStoreProductImagesEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_store_product_images(
                store_id="store_id",
                product_id="product_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_store_product_images(
            store_id,
            product_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    async def create_store_product_image(
        self,
        store_id: str,
        product_id: str,
        *,
        id: str,
        url: str,
        variant_ids: typing.Optional[typing.Sequence[CreateStoreProductImageEcommerceRequestVariantIdsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateStoreProductImageEcommerceResponse:
        """
        Add a new image to the product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        id : str
            A unique identifier for the product image.

        url : str
            The URL for a product image.

        variant_ids : typing.Optional[typing.Sequence[CreateStoreProductImageEcommerceRequestVariantIdsItem]]
            The list of product variants using the image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateStoreProductImageEcommerceResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store_product_image(
                store_id="store_id",
                product_id="product_id",
                id="id",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store_product_image(
            store_id, product_id, id=id, url=url, variant_ids=variant_ids, request_options=request_options
        )
        return _response.data

    async def get_store_product_image(
        self,
        store_id: str,
        product_id: str,
        image_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetStoreProductImageEcommerceResponse:
        """
        Get information about a specific product image.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        image_id : str
            The id for the product image.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStoreProductImageEcommerceResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store_product_image(
                store_id="store_id",
                product_id="product_id",
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store_product_image(
            store_id,
            product_id,
            image_id,
            fields=fields,
            exclude_fields=exclude_fields,
            request_options=request_options,
        )
        return _response.data

    async def delete_store_product_image(
        self, store_id: str, product_id: str, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a product image.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        image_id : str
            The id for the product image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store_product_image(
                store_id="store_id",
                product_id="product_id",
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store_product_image(
            store_id, product_id, image_id, request_options=request_options
        )
        return _response.data

    async def update_store_product_image(
        self,
        store_id: str,
        product_id: str,
        image_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        variant_ids: typing.Optional[typing.Sequence[UpdateStoreProductImageEcommerceRequestVariantIdsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateStoreProductImageEcommerceResponse:
        """
        Update a product image.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        image_id : str
            The id for the product image.

        id : typing.Optional[str]
            A unique identifier for the product image.

        url : typing.Optional[str]
            The URL for a product image.

        variant_ids : typing.Optional[typing.Sequence[UpdateStoreProductImageEcommerceRequestVariantIdsItem]]
            The list of product variants using the image.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateStoreProductImageEcommerceResponse


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store_product_image(
                store_id="store_id",
                product_id="product_id",
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store_product_image(
            store_id, product_id, image_id, id=id, url=url, variant_ids=variant_ids, request_options=request_options
        )
        return _response.data

    async def list_store_product_variants(
        self,
        store_id: str,
        product_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommerceProductVariant, ListStoreProductVariantsEcommerceResponse]:
        """
        Get information about a product's variants.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommerceProductVariant, ListStoreProductVariantsEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_store_product_variants(
                store_id="store_id",
                product_id="product_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_store_product_variants(
            store_id,
            product_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    async def create_store_product_variant(
        self,
        store_id: str,
        product_id: str,
        *,
        id: CreateStoreProductVariantEcommerceRequestId,
        title: str,
        backorders: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        inventory_quantity: typing.Optional[int] = OMIT,
        price: typing.Optional[CreateStoreProductVariantEcommerceRequestPrice] = OMIT,
        sku: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        visibility: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProductVariant:
        """
        Add a new variant to the product.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        id : CreateStoreProductVariantEcommerceRequestId
            A unique identifier for the product variant.

        title : str
            The title of a product variant.

        backorders : typing.Optional[str]
            The backorders of a product variant.

        image_url : typing.Optional[str]
            The image URL for a product variant.

        inventory_quantity : typing.Optional[int]
            The inventory quantity of a product variant.

        price : typing.Optional[CreateStoreProductVariantEcommerceRequestPrice]

        sku : typing.Optional[str]
            The stock keeping unit (SKU) of a product variant.

        url : typing.Optional[str]
            The URL for a product variant.

        visibility : typing.Optional[str]
            The visibility of a product variant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProductVariant


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store_product_variant(
                store_id="store_id",
                product_id="product_id",
                id="id",
                title="Cat Hat",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store_product_variant(
            store_id,
            product_id,
            id=id,
            title=title,
            backorders=backorders,
            image_url=image_url,
            inventory_quantity=inventory_quantity,
            price=price,
            sku=sku,
            url=url,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    async def get_store_product_variant(
        self,
        store_id: str,
        product_id: str,
        variant_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProductVariant:
        """
        Get information about a specific product variant.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        variant_id : str
            The id for the product variant.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProductVariant


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store_product_variant(
                store_id="store_id",
                product_id="product_id",
                variant_id="variant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store_product_variant(
            store_id,
            product_id,
            variant_id,
            fields=fields,
            exclude_fields=exclude_fields,
            request_options=request_options,
        )
        return _response.data

    async def upsert_store_product_variant(
        self,
        store_id: str,
        product_id: str,
        variant_id: str,
        *,
        backorders: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        inventory_quantity: typing.Optional[int] = OMIT,
        price: typing.Optional[UpsertStoreProductVariantEcommerceRequestPrice] = OMIT,
        sku: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        visibility: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProductVariant:
        """
        Add or update a product variant.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        variant_id : str
            The id for the product variant.

        backorders : typing.Optional[str]
            The backorders of a product variant.

        id : typing.Optional[str]
            A unique identifier for the product variant.

        image_url : typing.Optional[str]
            The image URL for a product variant.

        inventory_quantity : typing.Optional[int]
            The inventory quantity of a product variant.

        price : typing.Optional[UpsertStoreProductVariantEcommerceRequestPrice]

        sku : typing.Optional[str]
            The stock keeping unit (SKU) of a product variant.

        title : typing.Optional[str]
            The title of a product variant.

        url : typing.Optional[str]
            The URL for a product variant.

        visibility : typing.Optional[str]
            The visibility of a product variant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProductVariant


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.upsert_store_product_variant(
                store_id="store_id",
                product_id="product_id",
                variant_id="variant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_store_product_variant(
            store_id,
            product_id,
            variant_id,
            backorders=backorders,
            id=id,
            image_url=image_url,
            inventory_quantity=inventory_quantity,
            price=price,
            sku=sku,
            title=title,
            url=url,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    async def delete_store_product_variant(
        self,
        store_id: str,
        product_id: str,
        variant_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a product variant.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        variant_id : str
            The id for the product variant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store_product_variant(
                store_id="store_id",
                product_id="product_id",
                variant_id="variant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store_product_variant(
            store_id, product_id, variant_id, request_options=request_options
        )
        return _response.data

    async def update_store_product_variant(
        self,
        store_id: str,
        product_id: str,
        variant_id: str,
        *,
        backorders: typing.Optional[str] = OMIT,
        image_url: typing.Optional[str] = OMIT,
        inventory_quantity: typing.Optional[int] = OMIT,
        price: typing.Optional[UpdateStoreProductVariantEcommerceRequestPrice] = OMIT,
        sku: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        visibility: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommerceProductVariant:
        """
        Update a product variant.

        Parameters
        ----------
        store_id : str
            The store id.

        product_id : str
            The id for the product of a store.

        variant_id : str
            The id for the product variant.

        backorders : typing.Optional[str]
            The backorders of a product variant.

        image_url : typing.Optional[str]
            The image URL for a product variant.

        inventory_quantity : typing.Optional[int]
            The inventory quantity of a product variant.

        price : typing.Optional[UpdateStoreProductVariantEcommerceRequestPrice]

        sku : typing.Optional[str]
            The stock keeping unit (SKU) of a product variant.

        title : typing.Optional[str]
            The title of a product variant.

        url : typing.Optional[str]
            The URL for a product variant.

        visibility : typing.Optional[str]
            The visibility of a product variant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommerceProductVariant


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store_product_variant(
                store_id="store_id",
                product_id="product_id",
                variant_id="variant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store_product_variant(
            store_id,
            product_id,
            variant_id,
            backorders=backorders,
            image_url=image_url,
            inventory_quantity=inventory_quantity,
            price=price,
            sku=sku,
            title=title,
            url=url,
            visibility=visibility,
            request_options=request_options,
        )
        return _response.data

    async def list_store_promo_rules(
        self,
        store_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommercePromoRule, ListStorePromoRulesEcommerceResponse]:
        """
        Get information about a store's promo rules.

        Parameters
        ----------
        store_id : str
            The store id.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommercePromoRule, ListStorePromoRulesEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_store_promo_rules(
                store_id="store_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_store_promo_rules(
            store_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    async def create_store_promo_rule(
        self,
        store_id: str,
        *,
        amount: CreateStorePromoRuleEcommerceRequestAmount,
        description: str,
        id: str,
        target: CreateStorePromoRuleEcommerceRequestTarget,
        type: CreateStorePromoRuleEcommerceRequestType,
        created_at_foreign: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        ends_at: typing.Optional[CreateStorePromoRuleEcommerceRequestEndsAt] = OMIT,
        starts_at: typing.Optional[CreateStorePromoRuleEcommerceRequestStartsAt] = OMIT,
        title: typing.Optional[str] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoRule:
        """
        Add a new promo rule to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        amount : CreateStorePromoRuleEcommerceRequestAmount

        description : str
            The description of a promotion restricted to UTF-8 characters with max length 255.

        id : str
            A unique identifier for the promo rule. If Ecommerce platform does not support promo rule, use promo code id as promo rule id. Restricted to UTF-8 characters with max length 50.

        target : CreateStorePromoRuleEcommerceRequestTarget
            The target that the discount applies to.

        type : CreateStorePromoRuleEcommerceRequestType
            Type of discount. For free shipping set type to fixed.

        created_at_foreign : typing.Optional[str]
            The date and time the promotion was created in ISO 8601 format.

        enabled : typing.Optional[bool]
            Whether the promo rule is currently enabled.

        ends_at : typing.Optional[CreateStorePromoRuleEcommerceRequestEndsAt]

        starts_at : typing.Optional[CreateStorePromoRuleEcommerceRequestStartsAt]

        title : typing.Optional[str]
            The title that will show up in promotion campaign. Restricted to UTF-8 characters with max length of 100 bytes.

        updated_at_foreign : typing.Optional[str]
            The date and time the promotion was updated in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoRule


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store_promo_rule(
                store_id="store_id",
                amount=1.1,
                description="Save BIG during our summer sale!",
                id="id",
                target="per_item",
                type="fixed",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store_promo_rule(
            store_id,
            amount=amount,
            description=description,
            id=id,
            target=target,
            type=type,
            created_at_foreign=created_at_foreign,
            enabled=enabled,
            ends_at=ends_at,
            starts_at=starts_at,
            title=title,
            updated_at_foreign=updated_at_foreign,
            request_options=request_options,
        )
        return _response.data

    async def get_store_promo_rule(
        self,
        store_id: str,
        promo_rule_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoRule:
        """
        Get information about a specific promo rule.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoRule


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store_promo_rule(
                store_id="store_id",
                promo_rule_id="promo_rule_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store_promo_rule(
            store_id, promo_rule_id, fields=fields, exclude_fields=exclude_fields, request_options=request_options
        )
        return _response.data

    async def delete_store_promo_rule(
        self, store_id: str, promo_rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a promo rule from a store.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store_promo_rule(
                store_id="store_id",
                promo_rule_id="promo_rule_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store_promo_rule(
            store_id, promo_rule_id, request_options=request_options
        )
        return _response.data

    async def update_store_promo_rule(
        self,
        store_id: str,
        promo_rule_id: str,
        *,
        amount: typing.Optional[UpdateStorePromoRuleEcommerceRequestAmount] = OMIT,
        created_at_foreign: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        ends_at: typing.Optional[UpdateStorePromoRuleEcommerceRequestEndsAt] = OMIT,
        id: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[UpdateStorePromoRuleEcommerceRequestStartsAt] = OMIT,
        target: typing.Optional[UpdateStorePromoRuleEcommerceRequestTarget] = OMIT,
        title: typing.Optional[str] = OMIT,
        type: typing.Optional[UpdateStorePromoRuleEcommerceRequestType] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoRule:
        """
        Update a promo rule.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        amount : typing.Optional[UpdateStorePromoRuleEcommerceRequestAmount]

        created_at_foreign : typing.Optional[str]
            The date and time the promotion was created in ISO 8601 format.

        description : typing.Optional[str]
            The description of a promotion restricted to UTF-8 characters with max length 255.

        enabled : typing.Optional[bool]
            Whether the promo rule is currently enabled.

        ends_at : typing.Optional[UpdateStorePromoRuleEcommerceRequestEndsAt]

        id : typing.Optional[str]
            A unique identifier for the promo rule. If Ecommerce platform does not support promo rule, use promo code id as promo rule id. Restricted to UTF-8 characters with max length 50.

        starts_at : typing.Optional[UpdateStorePromoRuleEcommerceRequestStartsAt]

        target : typing.Optional[UpdateStorePromoRuleEcommerceRequestTarget]
            The target that the discount applies to.

        title : typing.Optional[str]
            The title that will show up in promotion campaign. Restricted to UTF-8 characters with max length of 100 bytes.

        type : typing.Optional[UpdateStorePromoRuleEcommerceRequestType]
            Type of discount. For free shipping set type to fixed.

        updated_at_foreign : typing.Optional[str]
            The date and time the promotion was updated in ISO 8601 format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoRule


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store_promo_rule(
                store_id="store_id",
                promo_rule_id="promo_rule_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store_promo_rule(
            store_id,
            promo_rule_id,
            amount=amount,
            created_at_foreign=created_at_foreign,
            description=description,
            enabled=enabled,
            ends_at=ends_at,
            id=id,
            starts_at=starts_at,
            target=target,
            title=title,
            type=type,
            updated_at_foreign=updated_at_foreign,
            request_options=request_options,
        )
        return _response.data

    async def list_store_promo_rule_promo_codes(
        self,
        store_id: str,
        promo_rule_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ECommercePromoCode, ListStorePromoRulePromoCodesEcommerceResponse]:
        """
        Get information about a store's promo codes.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        count : typing.Optional[int]
            The number of records to return. Default value is 10. Maximum value is 1000

        offset : typing.Optional[int]
            Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ECommercePromoCode, ListStorePromoRulePromoCodesEcommerceResponse]


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.ecommerce.list_store_promo_rule_promo_codes(
                store_id="store_id",
                promo_rule_id="promo_rule_id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_store_promo_rule_promo_codes(
            store_id,
            promo_rule_id,
            fields=fields,
            exclude_fields=exclude_fields,
            count=count,
            offset=offset,
            request_options=request_options,
        )

    async def create_store_promo_rule_promo_code(
        self,
        store_id: str,
        promo_rule_id: str,
        *,
        code: str,
        id: str,
        redemption_url: str,
        created_at_foreign: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        usage_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoCode:
        """
        Add a new promo code to a store.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        code : str
            The discount code. Restricted to UTF-8 characters with max length 50.

        id : str
            A unique identifier for the promo code. Restricted to UTF-8 characters with max length 50.

        redemption_url : str
            The url that should be used in the promotion campaign restricted to UTF-8 characters with max length 2000.

        created_at_foreign : typing.Optional[str]
            The date and time the promotion was created in ISO 8601 format.

        enabled : typing.Optional[bool]
            Whether the promo code is currently enabled.

        updated_at_foreign : typing.Optional[str]
            The date and time the promotion was updated in ISO 8601 format.

        usage_count : typing.Optional[int]
            Number of times promo code has been used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoCode


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.create_store_promo_rule_promo_code(
                store_id="store_id",
                promo_rule_id="promo_rule_id",
                code="summersale",
                id="id",
                redemption_url="A url that applies promo code directly at checkout or a url that points to sale page or store url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_store_promo_rule_promo_code(
            store_id,
            promo_rule_id,
            code=code,
            id=id,
            redemption_url=redemption_url,
            created_at_foreign=created_at_foreign,
            enabled=enabled,
            updated_at_foreign=updated_at_foreign,
            usage_count=usage_count,
            request_options=request_options,
        )
        return _response.data

    async def get_store_promo_rule_promo_code(
        self,
        store_id: str,
        promo_rule_id: str,
        promo_code_id: str,
        *,
        fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        exclude_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoCode:
        """
        Get information about a specific promo code.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        promo_code_id : str
            The id for the promo code of a store.

        fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.

        exclude_fields : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoCode


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.get_store_promo_rule_promo_code(
                store_id="store_id",
                promo_rule_id="promo_rule_id",
                promo_code_id="promo_code_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_store_promo_rule_promo_code(
            store_id,
            promo_rule_id,
            promo_code_id,
            fields=fields,
            exclude_fields=exclude_fields,
            request_options=request_options,
        )
        return _response.data

    async def delete_store_promo_rule_promo_code(
        self,
        store_id: str,
        promo_rule_id: str,
        promo_code_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a promo code from a store.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        promo_code_id : str
            The id for the promo code of a store.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.delete_store_promo_rule_promo_code(
                store_id="store_id",
                promo_rule_id="promo_rule_id",
                promo_code_id="promo_code_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_store_promo_rule_promo_code(
            store_id, promo_rule_id, promo_code_id, request_options=request_options
        )
        return _response.data

    async def update_store_promo_rule_promo_code(
        self,
        store_id: str,
        promo_rule_id: str,
        promo_code_id: str,
        *,
        code: typing.Optional[str] = OMIT,
        created_at_foreign: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        redemption_url: typing.Optional[str] = OMIT,
        updated_at_foreign: typing.Optional[str] = OMIT,
        usage_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ECommercePromoCode:
        """
        Update a promo code.

        Parameters
        ----------
        store_id : str
            The store id.

        promo_rule_id : str
            The id for the promo rule of a store.

        promo_code_id : str
            The id for the promo code of a store.

        code : typing.Optional[str]
            The discount code. Restricted to UTF-8 characters with max length 50.

        created_at_foreign : typing.Optional[str]
            The date and time the promotion was created in ISO 8601 format.

        enabled : typing.Optional[bool]
            Whether the promo code is currently enabled.

        id : typing.Optional[str]
            A unique identifier for the promo code. Restricted to UTF-8 characters with max length 50.

        redemption_url : typing.Optional[str]
            The url that should be used in the promotion campaign restricted to UTF-8 characters with max length 2000.

        updated_at_foreign : typing.Optional[str]
            The date and time the promotion was updated in ISO 8601 format.

        usage_count : typing.Optional[int]
            Number of times promo code has been used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ECommercePromoCode


        Examples
        --------
        import asyncio

        from mailchimp_marketing import AsyncMailchimpClient

        client = AsyncMailchimpClient(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ecommerce.update_store_promo_rule_promo_code(
                store_id="store_id",
                promo_rule_id="promo_rule_id",
                promo_code_id="promo_code_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_store_promo_rule_promo_code(
            store_id,
            promo_rule_id,
            promo_code_id,
            code=code,
            created_at_foreign=created_at_foreign,
            enabled=enabled,
            id=id,
            redemption_url=redemption_url,
            updated_at_foreign=updated_at_foreign,
            usage_count=usage_count,
            request_options=request_options,
        )
        return _response.data
