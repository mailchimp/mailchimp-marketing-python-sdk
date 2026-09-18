# Reference
## root
<details><summary><code>client.root.<a href="src/mailchimp_marketing/root/client.py">list</a>(...) -> ListRootResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get links to all other resources available in the API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.root.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AccountExports
<details><summary><code>client.account_exports.<a href="src/mailchimp_marketing/account_exports/client.py">list</a>(...) -> ListAccountExportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of account exports for a given account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.account_exports.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_exports.<a href="src/mailchimp_marketing/account_exports/client.py">create</a>(...) -> CreateAccountExportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new account export in your Mailchimp account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.account_exports.create(
    include_stages=[
        "audiences",
        "gallery_files"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**include_stages:** `typing.List[CreateAccountExportsRequestIncludeStagesItem]` — The stages of an account export to include.
    
</dd>
</dl>

<dl>
<dd>

**since_timestamp:** `typing.Optional[datetime.datetime]` — An ISO 8601 date that will limit the export to only records created after a given time. For instance, the reports stage will contain any campaign sent after the given timestamp. Audiences, however, are excluded from this limit.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account_exports.<a href="src/mailchimp_marketing/account_exports/client.py">get</a>(...) -> GetAccountExportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific account export.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.account_exports.get(
    export_id="export_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**export_id:** `str` — The unique id for the account export.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ActivityFeed
<details><summary><code>client.activity_feed.<a href="src/mailchimp_marketing/activity_feed/client.py">list</a>() -> typing.List[ListActivityFeedResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about the activity feed endpoint's resources.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.activity_feed.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.activity_feed.<a href="src/mailchimp_marketing/activity_feed/client.py">list_chimp_chatter</a>(...) -> ListChimpChatterActivityFeedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the Chimp Chatter for this account ordered by most recent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.activity_feed.list_chimp_chatter()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Audiences
<details><summary><code>client.audiences.<a href="src/mailchimp_marketing/audiences/client.py">get_audience_contact_list</a>(...) -> GetAudienceContactListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of omni-channel contacts for a given audience.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.audiences.get_audience_contact_list(
    audience_id="audience_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audience_id:** `str` — The unique ID for the audience.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Paginate through a collection of records by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request. Default value fetches the first "page" of results.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[datetime.datetime]` — Restricts the response to contacts created at or before the specified time (inclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**created_since:** `typing.Optional[datetime.datetime]` — Restricts the response to contacts created after the specified time (exclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**updated_before:** `typing.Optional[datetime.datetime]` — Restricts the response to contacts updated at or before the specified time (inclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**updated_since:** `typing.Optional[datetime.datetime]` — Restricts the response to contacts updated after the specified time (exclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[GetAudienceContactListRequestSortField]` — Specifies the field to sort the returned contacts by.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[GetAudienceContactListRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audiences.<a href="src/mailchimp_marketing/audiences/client.py">create_audience_contact</a>(...) -> AudiencesContact</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new omni-channel contact for an audience.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.audiences.create_audience_contact(
    audience_id="audience_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audience_id:** `str` — The unique ID for the audience.
    
</dd>
</dl>

<dl>
<dd>

**merge_field_validation_mode:** `typing.Optional[CreateAudienceContactRequestMergeFieldValidationMode]` — Defines how merge field validation is handled. When set to `ignore_required_checks`, the API does not raise an error if required merge fields are missing from the request. When set to `strict`, the API enforces validation and returns an error if any required merge field is not provided. If this setting is omitted, `strict` is applied by default.
    
</dd>
</dl>

<dl>
<dd>

**data_mode:** `typing.Optional[CreateAudienceContactRequestDataMode]` — Indicates the data processing mode. In `historical` mode, contact data changes do not trigger automations or webhooks. In `live mode`, such changes do trigger them.
    
</dd>
</dl>

<dl>
<dd>

**email_channel:** `typing.Optional[CreateAudienceContactRequestEmailChannel]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The contact's detected language.
    
</dd>
</dl>

<dl>
<dd>

**merge_fields:** `typing.Optional[typing.Dict[str, CreateAudienceContactRequestMergeFieldsValue]]` — A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.
    
</dd>
</dl>

<dl>
<dd>

**sms_channel:** `typing.Optional[CreateAudienceContactRequestSmsChannel]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[CreateAudienceContactRequestTagsItem]]` — An array of tags to add to the contact. Accepts tag name strings or objects with name and status. This operation is append-only; existing tags will be preserved, and only new tags from this array will be added.
    
</dd>
</dl>

<dl>
<dd>

**update_existing:** `typing.Optional[bool]` — If a contact already exists, update them instead of returning a conflict error. When `true` and a matching contact is found (by email or phone), the existing contact is updated with the provided channel data. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audiences.<a href="src/mailchimp_marketing/audiences/client.py">get_audience_contact</a>(...) -> AudiencesContact</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific omni-channel contact in an audience.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.audiences.get_audience_contact(
    audience_id="audience_id",
    contact_id="contact_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audience_id:** `str` — The unique ID for the audience.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `str` — A unique identifier for the contact, which can be a Mailchimp contact ID or a channel hash. A channel hash must follow the format email:[md5_hash] (where the hash is the MD5 of the lowercased email address) or sms:[sha256_hash] (where the hash is the SHA256 of the E.164-formatted phone number).
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audiences.<a href="src/mailchimp_marketing/audiences/client.py">patch_audience_contact</a>(...) -> AudiencesContact</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing omni-channel contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.audiences.patch_audience_contact(
    audience_id="audience_id",
    contact_id="contact_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audience_id:** `str` — The unique ID for the audience.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `str` — The unique id for the contact.
    
</dd>
</dl>

<dl>
<dd>

**merge_field_validation_mode:** `typing.Optional[PatchAudienceContactRequestMergeFieldValidationMode]` — Defines how merge field validation is handled. When set to `ignore_required_checks`, the API does not raise an error if required merge fields are missing from the request. When set to `strict`, the API enforces validation and returns an error if any required merge field is not provided. If this setting is omitted, `strict` is applied by default.
    
</dd>
</dl>

<dl>
<dd>

**data_mode:** `typing.Optional[PatchAudienceContactRequestDataMode]` — Indicates the data processing mode. In `historical` mode, contact data changes do not trigger automations or webhooks. In `live mode`, such changes do trigger them.
    
</dd>
</dl>

<dl>
<dd>

**email_channel:** `typing.Optional[PatchAudienceContactRequestEmailChannel]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — The contact's detected language.
    
</dd>
</dl>

<dl>
<dd>

**merge_fields:** `typing.Optional[typing.Dict[str, PatchAudienceContactRequestMergeFieldsValue]]` — A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.
    
</dd>
</dl>

<dl>
<dd>

**sms_channel:** `typing.Optional[PatchAudienceContactRequestSmsChannel]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[PatchAudienceContactRequestTagsItem]]` — An array of tags to add to the contact. Accepts tag name strings or objects with name and status. This operation is append-only; existing tags will be preserved, and only new tags from this array will be added.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audiences.<a href="src/mailchimp_marketing/audiences/client.py">post_audiences_contacts_actions_archive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archives a Contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.audiences.post_audiences_contacts_actions_archive(
    audience_id="audience_id",
    contact_id="contact_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audience_id:** `str` — The unique ID for the audience.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `str` — The unique id for the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audiences.<a href="src/mailchimp_marketing/audiences/client.py">post_audiences_contacts_actions_forget</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forgets a Contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.audiences.post_audiences_contacts_actions_forget(
    audience_id="audience_id",
    contact_id="contact_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**audience_id:** `str` — The unique ID for the audience.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `str` — The unique id for the contact.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AuthorizedApps
<details><summary><code>client.authorized_apps.<a href="src/mailchimp_marketing/authorized_apps/client.py">list</a>(...) -> ListAuthorizedAppsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of an account's registered, connected applications.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.authorized_apps.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.authorized_apps.<a href="src/mailchimp_marketing/authorized_apps/client.py">get</a>(...) -> GetAuthorizedAppsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific authorized application.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.authorized_apps.get(
    app_id="app_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**app_id:** `str` — The unique id for the connected authorized application.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## automations
<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">list</a>(...) -> ListAutomationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a summary of an account's classic automations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**before_create_time:** `typing.Optional[datetime.datetime]` — Restrict the response to automations created before this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_create_time:** `typing.Optional[datetime.datetime]` — Restrict the response to automations created after this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**before_start_time:** `typing.Optional[datetime.datetime]` — Restrict the response to automations started before this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_start_time:** `typing.Optional[datetime.datetime]` — Restrict the response to automations started after this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListAutomationsRequestStatus]` — Restrict the results to automations with the specified status.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">create</a>(...) -> AutomationWorkflow</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new classic automation in your Mailchimp account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment
from mailchimp_marketing.automations import CreateAutomationsRequestRecipients, CreateAutomationsRequestTriggerSettings

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.create(
    recipients=CreateAutomationsRequestRecipients(),
    trigger_settings=CreateAutomationsRequestTriggerSettings(
        workflow_type="abandonedBrowse",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recipients:** `CreateAutomationsRequestRecipients` — List settings for the Automation.
    
</dd>
</dl>

<dl>
<dd>

**trigger_settings:** `CreateAutomationsRequestTriggerSettings` — Trigger settings for the Automation.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[CreateAutomationsRequestSettings]` — The settings for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">get</a>(...) -> AutomationWorkflow</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a summary of an individual classic automation workflow's settings and content. The `trigger_settings` object returns information for the first email in the workflow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.get(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">create_action_archive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archiving will permanently end your automation and keep the report data. You’ll be able to replicate your archived automation, but you can’t restart it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.create_action_archive(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">create_action_pause_all_email</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pause all emails in a specific classic automation workflow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.create_action_pause_all_email(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">create_action_start_all_email</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start all emails in a classic automation workflow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.create_action_start_all_email(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">list_emails</a>(...) -> ListEmailsAutomationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a summary of the emails in a classic automation workflow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.list_emails(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">get_email</a>(...) -> AutomationWorkflowEmail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about an individual classic automation workflow email.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.get_email(
    workflow_id="workflow_id",
    workflow_email_id="workflow_email_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**workflow_email_id:** `str` — The unique id for the Automation workflow email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">delete_email</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes an individual classic automation workflow email. Emails from certain workflow types, including the Abandoned Cart Email (abandonedCart) and Product Retargeting Email (abandonedBrowse) Workflows, cannot be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.delete_email(
    workflow_id="workflow_id",
    workflow_email_id="workflow_email_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**workflow_email_id:** `str` — The unique id for the Automation workflow email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">update_email</a>(...) -> AutomationWorkflowEmail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update settings for a classic automation workflow email.  Only works with workflows of type: abandonedBrowse, abandonedCart, emailFollowup, or singleWelcome.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.update_email(
    workflow_id="workflow_id",
    workflow_email_id="workflow_email_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**workflow_email_id:** `str` — The unique id for the Automation workflow email.
    
</dd>
</dl>

<dl>
<dd>

**delay:** `typing.Optional[UpdateEmailAutomationsRequestDelay]` — The delay settings for an automation email.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[UpdateEmailAutomationsRequestSettings]` — Settings for the campaign including the email subject, from name, and from email address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">create_email_action_pause</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pause an automated email.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.create_email_action_pause(
    workflow_id="workflow_id",
    workflow_email_id="workflow_email_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**workflow_email_id:** `str` — The unique id for the Automation workflow email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">create_email_action_start</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start an automated email.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.create_email_action_start(
    workflow_id="workflow_id",
    workflow_email_id="workflow_email_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**workflow_email_id:** `str` — The unique id for the Automation workflow email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">list_email_queue</a>(...) -> ListEmailQueueAutomationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a classic automation email queue.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.list_email_queue(
    workflow_id="workflow_id",
    workflow_email_id="workflow_email_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**workflow_email_id:** `str` — The unique id for the Automation workflow email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">create_email_queue</a>(...) -> SubscriberInAutomationQueue</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Manually add a subscriber to a workflow, bypassing the default trigger settings. You can also use this endpoint to trigger a series of automated emails in an API 3.0 workflow type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.create_email_queue(
    workflow_id="workflow_id",
    workflow_email_id="workflow_email_id",
    email_address="email_address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**workflow_email_id:** `str` — The unique id for the Automation workflow email.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `str` — The list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">get_email_queue</a>(...) -> SubscriberInAutomationQueue</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific subscriber in a classic automation email queue.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.get_email_queue(
    workflow_id="workflow_id",
    workflow_email_id="workflow_email_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**workflow_email_id:** `str` — The unique id for the Automation workflow email.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">list_removed_subscribers</a>(...) -> ListRemovedSubscribersAutomationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about subscribers who were removed from a classic automation workflow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.list_removed_subscribers(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">create_removed_subscriber</a>(...) -> SubscriberRemovedFromAutomationWorkflow</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a subscriber from a specific classic automation workflow. You can remove a subscriber at any point in an automation workflow, regardless of how many emails they've been sent from that workflow. Once they're removed, they can never be added back to the same workflow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.create_removed_subscriber(
    workflow_id="workflow_id",
    email_address="email_address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `str` — The list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/mailchimp_marketing/automations/client.py">get_removed_subscriber</a>(...) -> SubscriberRemovedFromAutomationWorkflow</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific subscriber who was removed from a classic automation workflow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.automations.get_removed_subscriber(
    workflow_id="workflow_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The unique id for the Automation workflow.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BatchWebhooks
<details><summary><code>client.batch_webhooks.<a href="src/mailchimp_marketing/batch_webhooks/client.py">list</a>(...) -> ListBatchWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all webhooks that have been configured for batches.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.batch_webhooks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_webhooks.<a href="src/mailchimp_marketing/batch_webhooks/client.py">create</a>(...) -> CreateBatchWebhooksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configure a webhook that will fire whenever any batch request completes processing.  You may only have a maximum of 20 batch webhooks.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.batch_webhooks.create(
    url="http://yourdomain.com/webhook",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**url:** `str` — A valid URL for the Webhook.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the webhook receives requests or not.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_webhooks.<a href="src/mailchimp_marketing/batch_webhooks/client.py">get</a>(...) -> BatchWebhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific batch webhook.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.batch_webhooks.get(
    batch_webhook_id="batch_webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_webhook_id:** `str` — The unique id for the batch webhook.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_webhooks.<a href="src/mailchimp_marketing/batch_webhooks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a batch webhook. Webhooks will no longer be sent to the given URL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.batch_webhooks.delete(
    batch_webhook_id="batch_webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_webhook_id:** `str` — The unique id for the batch webhook.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch_webhooks.<a href="src/mailchimp_marketing/batch_webhooks/client.py">update</a>(...) -> BatchWebhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a webhook that will fire whenever any batch request completes processing.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.batch_webhooks.update(
    batch_webhook_id="batch_webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_webhook_id:** `str` — The unique id for the batch webhook.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the webhook receives requests or not.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — A valid URL for the Webhook.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## batches
<details><summary><code>client.batches.<a href="src/mailchimp_marketing/batches/client.py">list</a>(...) -> ListBatchesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a summary of batch requests that have been made.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.batches.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batches.<a href="src/mailchimp_marketing/batches/client.py">create</a>(...) -> Batch</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Begin processing a batch operations request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment
from mailchimp_marketing.batches import CreateBatchesRequestOperationsItem

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.batches.create(
    operations=[
        CreateBatchesRequestOperationsItem(
            method="GET",
            path="/lists",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**operations:** `typing.List[CreateBatchesRequestOperationsItem]` — An array of objects that describes operations to perform.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batches.<a href="src/mailchimp_marketing/batches/client.py">get</a>(...) -> Batch</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a batch request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.batches.get(
    batch_id="batch_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `str` — The unique id for the batch operation.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batches.<a href="src/mailchimp_marketing/batches/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stops a batch request from running. Since only one batch request is run at a time, this can be used to cancel a long running request. The results of any completed operations will not be available after this call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.batches.delete(
    batch_id="batch_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `str` — The unique id for the batch operation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CampaignFolders
<details><summary><code>client.campaign_folders.<a href="src/mailchimp_marketing/campaign_folders/client.py">list</a>(...) -> CampaignFolders</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all folders used to organize campaigns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaign_folders.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaign_folders.<a href="src/mailchimp_marketing/campaign_folders/client.py">create</a>(...) -> CampaignFolders</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new campaign folder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaign_folders.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name to associate with the folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaign_folders.<a href="src/mailchimp_marketing/campaign_folders/client.py">get</a>(...) -> GetCampaignFoldersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific folder used to organize campaigns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaign_folders.get(
    folder_id="folder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — The unique id for the campaign folder.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaign_folders.<a href="src/mailchimp_marketing/campaign_folders/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific campaign folder, and mark all the campaigns in the folder as 'unfiled'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaign_folders.delete(
    folder_id="folder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — The unique id for the campaign folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaign_folders.<a href="src/mailchimp_marketing/campaign_folders/client.py">update</a>(...) -> UpdateCampaignFoldersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific folder used to organize campaigns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaign_folders.update(
    folder_id="folder_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — The unique id for the campaign folder.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Name to associate with the folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## campaigns
<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">list</a>(...) -> ListCampaignsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all campaigns in an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListCampaignsRequestType]` — The campaign type.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListCampaignsRequestStatus]` — The status of the campaign.
    
</dd>
</dl>

<dl>
<dd>

**before_send_time:** `typing.Optional[datetime.datetime]` — Restrict the response to campaigns sent before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_send_time:** `typing.Optional[datetime.datetime]` — Restrict the response to campaigns sent after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**before_create_time:** `typing.Optional[datetime.datetime]` — Restrict the response to campaigns created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_create_time:** `typing.Optional[datetime.datetime]` — Restrict the response to campaigns created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `typing.Optional[str]` — The unique id for the list.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — The unique folder id.
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `typing.Optional[str]` — Retrieve campaigns sent to a particular list member. Member ID is The MD5 hash of the lowercase version of the list member’s email address.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListCampaignsRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListCampaignsRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**include_resend_shortcut_eligibility:** `typing.Optional[bool]` — Return the `resend_shortcut_eligibility` field in the response, which tells you if the campaign is eligible for the various Campaign Resend Shortcuts offered.
    
</dd>
</dl>

<dl>
<dd>

**include_resend_shortcut_usage:** `typing.Optional[bool]` — Return the `resend_shortcut_usage` field in the response.  This includes information about campaigns related by a shortcut.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Mailchimp campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create(
    type="regular",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `CreateCampaignsRequestType` — There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) you can create in Mailchimp. A/B Split campaigns have been deprecated and variate campaigns should be used instead.
    
</dd>
</dl>

<dl>
<dd>

**content_type:** `typing.Optional[CreateCampaignsRequestContentType]` — How the campaign's content is put together. The old drag and drop editor uses 'template' while the new editor uses 'multichannel'. Defaults to template.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[CreateCampaignsRequestRecipients]` — List settings for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**rss_opts:** `typing.Optional[CreateCampaignsRequestRssOpts]` — [RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options, specific to an RSS campaign.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[CreateCampaignsRequestSettings]` — The settings for your campaign, including subject, from name, reply-to address, and more.
    
</dd>
</dl>

<dl>
<dd>

**social_card:** `typing.Optional[CreateCampaignsRequestSocialCard]` — The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more](https://mailchimp.com/help/enable-and-customize-social-cards/).
    
</dd>
</dl>

<dl>
<dd>

**tracking:** `typing.Optional[CampaignTrackingOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**variate_settings:** `typing.Optional[CreateCampaignsRequestVariateSettings]` — The settings specific to A/B test campaigns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">get</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.get(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**include_resend_shortcut_eligibility:** `typing.Optional[bool]` — Return the `resend_shortcut_eligibility` field in the response, which tells you if the campaign is eligible for the various Campaign Resend Shortcuts offered.
    
</dd>
</dl>

<dl>
<dd>

**include_resend_shortcut_usage:** `typing.Optional[bool]` — Return the `resend_shortcut_usage` field in the response.  This includes information about campaigns related by a shortcut.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a campaign from your Mailchimp account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.delete(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">update</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update some or all of the settings for a specific campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.update(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[UpdateCampaignsRequestRecipients]` — List settings for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**rss_opts:** `typing.Optional[UpdateCampaignsRequestRssOpts]` — [RSS](https://mailchimp.com/help/share-your-blog-posts-with-mailchimp/) options for a campaign.
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Optional[UpdateCampaignsRequestSettings]` — The settings for your campaign, including subject, from name, reply-to address, and more.
    
</dd>
</dl>

<dl>
<dd>

**social_card:** `typing.Optional[UpdateCampaignsRequestSocialCard]` — The preview for the campaign, rendered by social networks like Facebook and Twitter. [Learn more](https://mailchimp.com/help/enable-and-customize-social-cards/).
    
</dd>
</dl>

<dl>
<dd>

**tracking:** `typing.Optional[CampaignTrackingOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**variate_settings:** `typing.Optional[UpdateCampaignsRequestVariateSettings]` — The settings specific to A/B test campaigns.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create_action_cancel_send</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a Regular or Plain-Text Campaign after you send, before all of your recipients receive it. This feature is included with Mailchimp Pro.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create_action_cancel_send(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create_action_create_resend</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the guesswork for resending a campaign to certain segments. You can use this endpoint as a shortcut to replicate a campaign and resend it to common segments, such as those who didn't open the campaign, or any new subscribers since it was sent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create_action_create_resend(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**shortcut_type:** `typing.Optional[CreateActionCreateResendCampaignsRequestShortcutType]` — Which campaign resend shortcut to use. Default is `to_non_openers`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create_action_pause</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pause an RSS-Driven campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create_action_pause(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create_action_replicate</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replicate a campaign in saved or send status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create_action_replicate(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create_action_resume</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resume an RSS-Driven campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create_action_resume(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create_action_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedule a campaign for delivery. If you're using Multivariate Campaigns to test send times or sending RSS Campaigns, use the send action instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment
import datetime

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create_action_schedule(
    campaign_id="campaign_id",
    schedule_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**schedule_time:** `datetime.datetime` — The UTC date and time to schedule the campaign for delivery in ISO 8601 format. Campaigns may only be scheduled to send on the quarter-hour (:00, :15, :30, :45).
    
</dd>
</dl>

<dl>
<dd>

**batch_delivery:** `typing.Optional[CreateActionScheduleCampaignsRequestBatchDelivery]` — Choose whether the campaign should use [Batch Delivery](https://mailchimp.com/help/schedule-batch-delivery/). Cannot be set to `true` for campaigns using [Timewarp](https://mailchimp.com/help/use-timewarp/).
    
</dd>
</dl>

<dl>
<dd>

**timewarp:** `typing.Optional[bool]` — Choose whether the campaign should use [Timewarp](https://mailchimp.com/help/use-timewarp/) when sending. Campaigns scheduled with Timewarp are localized based on the recipients' time zones. For example, a Timewarp campaign with a `schedule_time` of 13:00 will be sent to each recipient at 1:00pm in their local time. Cannot be set to `true` for campaigns using [Batch Delivery](https://mailchimp.com/help/schedule-batch-delivery/).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create_action_send</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a Mailchimp campaign. For RSS Campaigns, the campaign will send according to its schedule. All other campaigns will send immediately.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create_action_send(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create_action_test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a test email.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create_action_test(
    campaign_id="campaign_id",
    send_type="html",
    test_emails=[
        "test_emails"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**send_type:** `CreateActionTestCampaignsRequestSendType` — Choose the type of test email to send.
    
</dd>
</dl>

<dl>
<dd>

**test_emails:** `typing.List[str]` — An array of email addresses to send the test email to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create_action_unschedule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unschedule a scheduled campaign that hasn't started sending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create_action_unschedule(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">get_content</a>(...) -> CampaignContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the the HTML and plain-text content for a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.get_content(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">upsert_content</a>(...) -> CampaignContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the content for a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.upsert_content(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CampaignContent` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">list_feedback</a>(...) -> ListFeedbackCampaignsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get team feedback while you're working together on a Mailchimp campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.list_feedback(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">create_feedback</a>(...) -> CreateFeedbackCampaignsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add feedback on a specific campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.create_feedback(
    campaign_id="campaign_id",
    message="message",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**message:** `str` — The content of the feedback.
    
</dd>
</dl>

<dl>
<dd>

**block_id:** `typing.Optional[int]` — The block id for the editable block that the feedback addresses.
    
</dd>
</dl>

<dl>
<dd>

**is_complete:** `typing.Optional[bool]` — The status of feedback.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">get_feedback</a>(...) -> CampaignFeedback</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific feedback message from a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.get_feedback(
    campaign_id="campaign_id",
    feedback_id="feedback_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**feedback_id:** `str` — The unique id for the feedback message.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">delete_feedback</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a specific feedback message for a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.delete_feedback(
    campaign_id="campaign_id",
    feedback_id="feedback_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**feedback_id:** `str` — The unique id for the feedback message.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">update_feedback</a>(...) -> CampaignFeedback</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific feedback message for a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.update_feedback(
    campaign_id="campaign_id",
    feedback_id="feedback_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**feedback_id:** `str` — The unique id for the feedback message.
    
</dd>
</dl>

<dl>
<dd>

**block_id:** `typing.Optional[int]` — The block id for the editable block that the feedback addresses.
    
</dd>
</dl>

<dl>
<dd>

**is_complete:** `typing.Optional[bool]` — The status of feedback.
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` — The content of the feedback.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.campaigns.<a href="src/mailchimp_marketing/campaigns/client.py">list_send_checklist</a>(...) -> ListSendChecklistCampaignsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Review the send checklist for a campaign, and resolve any issues before sending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.campaigns.list_send_checklist(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ConnectedSites
<details><summary><code>client.connected_sites.<a href="src/mailchimp_marketing/connected_sites/client.py">list</a>(...) -> ListConnectedSitesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all connected sites in an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.connected_sites.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connected_sites.<a href="src/mailchimp_marketing/connected_sites/client.py">create</a>(...) -> ConnectedSite</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new Mailchimp connected site.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.connected_sites.create(
    domain="example.com",
    foreign_id="MC001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — The connected site domain.
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — The unique identifier for the site.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connected_sites.<a href="src/mailchimp_marketing/connected_sites/client.py">get</a>(...) -> ConnectedSite</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific connected site.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.connected_sites.get(
    connected_site_id="connected_site_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connected_site_id:** `str` — The unique identifier for the site.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connected_sites.<a href="src/mailchimp_marketing/connected_sites/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a connected site from your Mailchimp account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.connected_sites.delete(
    connected_site_id="connected_site_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connected_site_id:** `str` — The unique identifier for the site.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connected_sites.<a href="src/mailchimp_marketing/connected_sites/client.py">create_action_verify_script_installation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify that the connected sites script has been installed, either via the script URL or fragment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.connected_sites.create_action_verify_script_installation(
    connected_site_id="connected_site_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connected_site_id:** `str` — The unique identifier for the site.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## conversations
<details><summary><code>client.conversations.<a href="src/mailchimp_marketing/conversations/client.py">list</a>(...) -> ListConversationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of conversations for the account. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.conversations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**has_unread_messages:** `typing.Optional[ListConversationsRequestHasUnreadMessages]` — Whether the conversation has any unread messages.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `typing.Optional[str]` — The unique id for the list.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/mailchimp_marketing/conversations/client.py">get</a>(...) -> Conversation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about an individual conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.conversations.get(
    conversation_id="conversation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The unique id for the conversation.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/mailchimp_marketing/conversations/client.py">list_messages</a>(...) -> ListMessagesConversationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get messages from a specific conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.conversations.list_messages(
    conversation_id="conversation_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The unique id for the conversation.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**is_read:** `typing.Optional[ListMessagesConversationsRequestIsRead]` — Whether a conversation message has been marked as read.
    
</dd>
</dl>

<dl>
<dd>

**before_timestamp:** `typing.Optional[datetime.datetime]` — Restrict the response to messages created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_timestamp:** `typing.Optional[datetime.datetime]` — Restrict the response to messages created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conversations.<a href="src/mailchimp_marketing/conversations/client.py">get_message</a>(...) -> ConversationMessage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an individual message in a conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.conversations.get_message(
    conversation_id="conversation_id",
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**conversation_id:** `str` — The unique id for the conversation.
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` — The unique id for the conversation message.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomerJourneys
<details><summary><code>client.customer_journeys.<a href="src/mailchimp_marketing/customer_journeys/client.py">create_journey_step_action_trigger</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A step trigger in an Automation flow. To use it, create a starting point or step from the Automation flow builder in the app using the Customer Journeys API condition. We’ll provide a url during the process that includes the {journey_id} and {step_id}. You’ll then be able to use this endpoint to trigger the condition for the posted contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.customer_journeys.create_journey_step_action_trigger(
    journey_id=1,
    step_id=1,
    email_address="email_address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**journey_id:** `int` — The id for the flow.
    
</dd>
</dl>

<dl>
<dd>

**step_id:** `int` — The id for the Step.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `str` — The list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ecommerce
<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list</a>() -> ListEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about the e-commerce endpoint's resources.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_orders</a>(...) -> ListOrdersEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about an account's orders.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_orders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — Restrict results to orders with a specific `campaign_id` value.
    
</dd>
</dl>

<dl>
<dd>

**outreach_id:** `typing.Optional[str]` — Restrict results to orders with a specific `outreach_id` value.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Restrict results to orders made by a specific customer.
    
</dd>
</dl>

<dl>
<dd>

**has_outreach:** `typing.Optional[bool]` — Restrict results to orders that have an outreach attached. For example, an email campaign or Facebook ad.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_stores</a>(...) -> ListStoresEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about all stores in the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_stores()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store</a>(...) -> ECommerceStore</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new store to your Mailchimp account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.create_store(
    currency_code="USD",
    id="example_store",
    list_id="1a2df69511",
    name="Freddie\'s Cat Hat Emporium",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**currency_code:** `str` — The three-letter ISO 4217 code for the currency that the store accepts.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The unique identifier for the store.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `str` — The unique identifier for the list associated with the store. The `list_id` for a specific store cannot change.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the store.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[CreateStoreEcommerceRequestAddress]` — The store address.
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — The store domain. This parameter is required for Connected Sites and Google Ads.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` — The email address for the store.
    
</dd>
</dl>

<dl>
<dd>

**is_syncing:** `typing.Optional[bool]` — Whether to disable automations because the store is currently [syncing](https://mailchimp.com/developer/marketing/docs/e-commerce/#pausing-store-automations).
    
</dd>
</dl>

<dl>
<dd>

**money_format:** `typing.Optional[str]` — The currency format for the store. For example: `$`, `£`, etc.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The store phone number.
    
</dd>
</dl>

<dl>
<dd>

**platform:** `typing.Optional[str]` — The e-commerce platform of the store.
    
</dd>
</dl>

<dl>
<dd>

**primary_locale:** `typing.Optional[str]` — The primary locale for the store. For example: `en`, `de`, etc.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — The timezone for the store.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store</a>(...) -> ECommerceStore</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store(
    store_id="store_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a store. Deleting a store will also delete any associated subresources, including Customers, Orders, Products, and Carts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store(
    store_id="store_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store</a>(...) -> ECommerceStore</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store(
    store_id="store_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[UpdateStoreEcommerceRequestAddress]` — The store address.
    
</dd>
</dl>

<dl>
<dd>

**currency_code:** `typing.Optional[str]` — The three-letter ISO 4217 code for the currency that the store accepts.
    
</dd>
</dl>

<dl>
<dd>

**domain:** `typing.Optional[str]` — The store domain.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` — The email address for the store.
    
</dd>
</dl>

<dl>
<dd>

**is_syncing:** `typing.Optional[bool]` — Whether to disable automations because the store is currently [syncing](https://mailchimp.com/developer/marketing/docs/e-commerce/#pausing-store-automations).
    
</dd>
</dl>

<dl>
<dd>

**money_format:** `typing.Optional[str]` — The currency format for the store. For example: `$`, `£`, etc.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the store.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The store phone number.
    
</dd>
</dl>

<dl>
<dd>

**platform:** `typing.Optional[str]` — The e-commerce platform of the store.
    
</dd>
</dl>

<dl>
<dd>

**primary_locale:** `typing.Optional[str]` — The primary locale for the store. For example: `en`, `de`, etc.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — The timezone for the store.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_store_carts</a>(...) -> ListStoreCartsEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a store's carts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_store_carts(
    store_id="store_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store_cart</a>(...) -> ECommerceCart</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new cart to a store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient, EcommerceStoresCartsPost
from mailchimp_marketing.environment import MailchimpClientEnvironment
from mailchimp_marketing.ecommerce import CreateStoreCartEcommerceRequestLinesItem

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**currency_code:** `str` — The three-letter ISO 4217 code for the currency that the cart uses.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `EcommerceStoresCartsPost` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `CreateStoreCartEcommerceRequestId` — A unique identifier for the cart.
    
</dd>
</dl>

<dl>
<dd>

**lines:** `typing.List[CreateStoreCartEcommerceRequestLinesItem]` — An array of the cart's line items.
    
</dd>
</dl>

<dl>
<dd>

**order_total:** `CreateStoreCartEcommerceRequestOrderTotal` 
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — A string that uniquely identifies the campaign for a cart.
    
</dd>
</dl>

<dl>
<dd>

**checkout_url:** `typing.Optional[str]` — The URL for the cart. This parameter is required for [Abandoned Cart](https://mailchimp.com/help/create-a-classic-abandoned-cart-email/) automations.
    
</dd>
</dl>

<dl>
<dd>

**tax_total:** `typing.Optional[CreateStoreCartEcommerceRequestTaxTotal]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store_cart</a>(...) -> ECommerceCart</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific cart.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store_cart(
    store_id="store_id",
    cart_id="cart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**cart_id:** `str` — The id for the cart.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store_cart</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a cart.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store_cart(
    store_id="store_id",
    cart_id="cart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**cart_id:** `str` — The id for the cart.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store_cart</a>(...) -> ECommerceCart</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific cart.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store_cart(
    store_id="store_id",
    cart_id="cart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**cart_id:** `str` — The id for the cart.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — A string that uniquely identifies the campaign associated with a cart.
    
</dd>
</dl>

<dl>
<dd>

**checkout_url:** `typing.Optional[str]` — The URL for the cart. This parameter is required for [Abandoned Cart](https://mailchimp.com/help/create-a-classic-abandoned-cart-email/) automations.
    
</dd>
</dl>

<dl>
<dd>

**currency_code:** `typing.Optional[str]` — The three-letter ISO 4217 code for the currency that the cart uses.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[EcommerceStoresCartsPatch]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[UpdateStoreCartEcommerceRequestId]` — A unique identifier for the cart.
    
</dd>
</dl>

<dl>
<dd>

**lines:** `typing.Optional[typing.List[UpdateStoreCartEcommerceRequestLinesItem]]` — An array of the cart's line items.
    
</dd>
</dl>

<dl>
<dd>

**order_total:** `typing.Optional[UpdateStoreCartEcommerceRequestOrderTotal]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_total:** `typing.Optional[UpdateStoreCartEcommerceRequestTaxTotal]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_store_cart_lines</a>(...) -> ListStoreCartLinesEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a cart's line items.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_store_cart_lines(
    store_id="store_id",
    cart_id="cart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**cart_id:** `str` — The id for the cart.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store_cart_line</a>(...) -> ECommerceCartLineItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new line item to an existing cart.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**cart_id:** `str` — The id for the cart.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — A unique identifier for the cart line item.
    
</dd>
</dl>

<dl>
<dd>

**price:** `CreateStoreCartLineEcommerceRequestPrice` 
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — A unique identifier for the product associated with the cart line item.
    
</dd>
</dl>

<dl>
<dd>

**product_variant_id:** `str` — A unique identifier for the product variant associated with the cart line item.
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `int` — The quantity of a cart line item.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store_cart_line</a>(...) -> ECommerceCartLineItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific cart line item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store_cart_line(
    store_id="store_id",
    cart_id="cart_id",
    line_id="line_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**cart_id:** `str` — The id for the cart.
    
</dd>
</dl>

<dl>
<dd>

**line_id:** `str` — The id for the line item of a cart.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store_cart_line</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific cart line item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store_cart_line(
    store_id="store_id",
    cart_id="cart_id",
    line_id="line_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**cart_id:** `str` — The id for the cart.
    
</dd>
</dl>

<dl>
<dd>

**line_id:** `str` — The id for the line item of a cart.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store_cart_line</a>(...) -> ECommerceCartLineItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific cart line item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store_cart_line(
    store_id="store_id",
    cart_id="cart_id",
    line_id="line_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**cart_id:** `str` — The id for the cart.
    
</dd>
</dl>

<dl>
<dd>

**line_id:** `str` — The id for the line item of a cart.
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[UpdateStoreCartLineEcommerceRequestPrice]` 
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `typing.Optional[str]` — A unique identifier for the product associated with the cart line item.
    
</dd>
</dl>

<dl>
<dd>

**product_variant_id:** `typing.Optional[str]` — A unique identifier for the product variant associated with the cart line item.
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[int]` — The quantity of a cart line item.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_store_customers</a>(...) -> ListStoreCustomersEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a store's customers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_store_customers(
    store_id="store_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` — Restrict the response to customers with the email address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store_customer</a>(...) -> ECommerceCustomer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new customer to a store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.create_store_customer(
    store_id="store_id",
    id="id",
    opt_in_status=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — A unique identifier for the customer. Limited to 50 characters.
    
</dd>
</dl>

<dl>
<dd>

**opt_in_status:** `bool` — The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing Mailchimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your Mailchimp list [will be added as `Transactional` members](https://mailchimp.com/developer/marketing/docs/e-commerce/#customers).
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[CreateStoreCustomerEcommerceRequestAddress]` — The customer's address.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` — The customer's company.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` — The customer's email address.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The customer's first name.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The customer's last name.
    
</dd>
</dl>

<dl>
<dd>

**sms_phone_number:** `typing.Optional[str]` — A US phone number for SMS contact.
    
</dd>
</dl>

<dl>
<dd>

**total_spent:** `typing.Optional[CreateStoreCustomerEcommerceRequestTotalSpent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store_customer</a>(...) -> ECommerceCustomer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific customer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store_customer(
    store_id="store_id",
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — The id for the customer of a store.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">upsert_store_customer</a>(...) -> ECommerceCustomer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add or update a customer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.upsert_store_customer(
    store_id="store_id",
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — The id for the customer of a store.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[UpsertStoreCustomerEcommerceRequestAddress]` — The customer's address.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` — The customer's company.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` — The customer's email address.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The customer's first name.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for the customer. Limited to 50 characters.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The customer's last name.
    
</dd>
</dl>

<dl>
<dd>

**opt_in_status:** `typing.Optional[bool]` — The customer's opt-in status. This value will never overwrite the opt-in status of a pre-existing Mailchimp list member, but will apply to list members that are added through the e-commerce API endpoints. Customers who don't opt in to your Mailchimp list [will be added as `Transactional` members](https://mailchimp.com/developer/marketing/docs/e-commerce/#customers).
    
</dd>
</dl>

<dl>
<dd>

**sms_phone_number:** `typing.Optional[str]` — A US phone number for SMS contact.
    
</dd>
</dl>

<dl>
<dd>

**total_spent:** `typing.Optional[UpsertStoreCustomerEcommerceRequestTotalSpent]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store_customer</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a customer from a store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store_customer(
    store_id="store_id",
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — The id for the customer of a store.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store_customer</a>(...) -> ECommerceCustomer</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a customer.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store_customer(
    store_id="store_id",
    customer_id="customer_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `str` — The id for the customer of a store.
    
</dd>
</dl>

<dl>
<dd>

**request:** `EcommerceStoresCartsPatch` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_store_orders</a>(...) -> ListStoreOrdersEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a store's orders.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_store_orders(
    store_id="store_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — Restrict results to orders made by a specific customer.
    
</dd>
</dl>

<dl>
<dd>

**has_outreach:** `typing.Optional[bool]` — Restrict results to orders that have an outreach attached. For example, an email campaign or Facebook ad.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — Restrict results to orders with a specific `campaign_id` value.
    
</dd>
</dl>

<dl>
<dd>

**outreach_id:** `typing.Optional[str]` — Restrict results to orders with a specific `outreach_id` value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store_order</a>(...) -> ECommerceOrder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new order to a store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient, EcommerceStoresCartsPost
from mailchimp_marketing.environment import MailchimpClientEnvironment
from mailchimp_marketing.ecommerce import CreateStoreOrderEcommerceRequestLinesItem

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**currency_code:** `str` — The three-letter ISO 4217 code for the currency that the store accepts.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `EcommerceStoresCartsPost` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — A unique identifier for the order.
    
</dd>
</dl>

<dl>
<dd>

**lines:** `typing.List[CreateStoreOrderEcommerceRequestLinesItem]` — An array of the order's line items.
    
</dd>
</dl>

<dl>
<dd>

**order_total:** `CreateStoreOrderEcommerceRequestOrderTotal` 
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[CreateStoreOrderEcommerceRequestBillingAddress]` — The billing address for the order.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — A string that uniquely identifies the campaign for an order.
    
</dd>
</dl>

<dl>
<dd>

**cart_id:** `typing.Optional[CreateStoreOrderEcommerceRequestCartId]` — A cart id that the order was placed for.
    
</dd>
</dl>

<dl>
<dd>

**cancelled_at_foreign:** `typing.Optional[str]` — The date and time the order was cancelled in ISO 8601 format. Note: passing a value for this parameter will cancel the order being created.
    
</dd>
</dl>

<dl>
<dd>

**discount_total:** `typing.Optional[CreateStoreOrderEcommerceRequestDiscountTotal]` 
    
</dd>
</dl>

<dl>
<dd>

**financial_status:** `typing.Optional[str]` — The order status. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).
    
</dd>
</dl>

<dl>
<dd>

**fulfillment_status:** `typing.Optional[str]` — The fulfillment status for the order. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).
    
</dd>
</dl>

<dl>
<dd>

**landing_site:** `typing.Optional[str]` — The URL for the page where the buyer landed when entering the shop.
    
</dd>
</dl>

<dl>
<dd>

**order_url:** `typing.Optional[str]` — The URL for the order.
    
</dd>
</dl>

<dl>
<dd>

**outreach:** `typing.Optional[CreateStoreOrderEcommerceRequestOutreach]` — The outreach associated with this order. For example, an email campaign or Facebook ad.
    
</dd>
</dl>

<dl>
<dd>

**processed_at_foreign:** `typing.Optional[str]` — The date and time the order was processed in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**promos:** `typing.Optional[typing.List[CreateStoreOrderEcommerceRequestPromosItem]]` — The promo codes applied on the order
    
</dd>
</dl>

<dl>
<dd>

**shipping_address:** `typing.Optional[CreateStoreOrderEcommerceRequestShippingAddress]` — The shipping address for the order.
    
</dd>
</dl>

<dl>
<dd>

**shipping_total:** `typing.Optional[CreateStoreOrderEcommerceRequestShippingTotal]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_total:** `typing.Optional[CreateStoreOrderEcommerceRequestTaxTotal]` 
    
</dd>
</dl>

<dl>
<dd>

**tracking_carrier:** `typing.Optional[str]` — The tracking carrier associated with the order.
    
</dd>
</dl>

<dl>
<dd>

**tracking_code:** `typing.Optional[CreateStoreOrderEcommerceRequestTrackingCode]` — The Mailchimp tracking code for the order. Uses the 'mc_tc' parameter in E-Commerce tracking URLs.
    
</dd>
</dl>

<dl>
<dd>

**tracking_number:** `typing.Optional[str]` — The tracking number associated with the order.
    
</dd>
</dl>

<dl>
<dd>

**tracking_url:** `typing.Optional[str]` — The tracking URL associated with the order.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_foreign:** `typing.Optional[str]` — The date and time the order was updated in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store_order</a>(...) -> ECommerceOrder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store_order(
    store_id="store_id",
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The id for the order in a store.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store_order</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store_order(
    store_id="store_id",
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The id for the order in a store.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store_order</a>(...) -> ECommerceOrder</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store_order(
    store_id="store_id",
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The id for the order in a store.
    
</dd>
</dl>

<dl>
<dd>

**billing_address:** `typing.Optional[UpdateStoreOrderEcommerceRequestBillingAddress]` — The billing address for the order.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — A string that uniquely identifies the campaign associated with an order.
    
</dd>
</dl>

<dl>
<dd>

**cart_id:** `typing.Optional[UpdateStoreOrderEcommerceRequestCartId]` — A cart id that the order was placed for.
    
</dd>
</dl>

<dl>
<dd>

**cancelled_at_foreign:** `typing.Optional[str]` — The date and time the order was cancelled in ISO 8601 format. Note: passing a value for this parameter will cancel the order being edited.
    
</dd>
</dl>

<dl>
<dd>

**currency_code:** `typing.Optional[str]` — The three-letter ISO 4217 code for the currency that the store accepts.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[EcommerceStoresCartsPatch]` 
    
</dd>
</dl>

<dl>
<dd>

**discount_total:** `typing.Optional[UpdateStoreOrderEcommerceRequestDiscountTotal]` 
    
</dd>
</dl>

<dl>
<dd>

**financial_status:** `typing.Optional[str]` — The order status. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).
    
</dd>
</dl>

<dl>
<dd>

**fulfillment_status:** `typing.Optional[str]` — The fulfillment status for the order. Use this parameter to trigger [Order Notifications](https://mailchimp.com/developer/marketing/docs/e-commerce/#order-notifications).
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for the order.
    
</dd>
</dl>

<dl>
<dd>

**landing_site:** `typing.Optional[str]` — The URL for the page where the buyer landed when entering the shop.
    
</dd>
</dl>

<dl>
<dd>

**lines:** `typing.Optional[typing.List[UpdateStoreOrderEcommerceRequestLinesItem]]` — An array of the order's line items.
    
</dd>
</dl>

<dl>
<dd>

**order_total:** `typing.Optional[UpdateStoreOrderEcommerceRequestOrderTotal]` 
    
</dd>
</dl>

<dl>
<dd>

**order_url:** `typing.Optional[str]` — The URL for the order.
    
</dd>
</dl>

<dl>
<dd>

**outreach:** `typing.Optional[UpdateStoreOrderEcommerceRequestOutreach]` — The outreach associated with this order. For example, an email campaign or Facebook ad.
    
</dd>
</dl>

<dl>
<dd>

**processed_at_foreign:** `typing.Optional[str]` — The date and time the order was processed in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**promos:** `typing.Optional[typing.List[UpdateStoreOrderEcommerceRequestPromosItem]]` — The promo codes applied on the order. Note: Patch will completely replace the value of promos with the new one provided.
    
</dd>
</dl>

<dl>
<dd>

**shipping_address:** `typing.Optional[UpdateStoreOrderEcommerceRequestShippingAddress]` — The shipping address for the order.
    
</dd>
</dl>

<dl>
<dd>

**shipping_total:** `typing.Optional[UpdateStoreOrderEcommerceRequestShippingTotal]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_total:** `typing.Optional[UpdateStoreOrderEcommerceRequestTaxTotal]` 
    
</dd>
</dl>

<dl>
<dd>

**tracking_carrier:** `typing.Optional[str]` — The tracking carrier associated with the order.
    
</dd>
</dl>

<dl>
<dd>

**tracking_code:** `typing.Optional[UpdateStoreOrderEcommerceRequestTrackingCode]` — The Mailchimp tracking code for the order. Uses the 'mc_tc' parameter in E-Commerce tracking URLs.
    
</dd>
</dl>

<dl>
<dd>

**tracking_number:** `typing.Optional[str]` — The tracking number associated with the order.
    
</dd>
</dl>

<dl>
<dd>

**tracking_url:** `typing.Optional[str]` — The tracking URL associated with the order.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_foreign:** `typing.Optional[str]` — The date and time the order was updated in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_store_order_lines</a>(...) -> ListStoreOrderLinesEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about an order's line items.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_store_order_lines(
    store_id="store_id",
    order_id="order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The id for the order in a store.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store_order_line</a>(...) -> ECommerceOrderLineItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new line item to an existing order.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The id for the order in a store.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — A unique identifier for the order line item.
    
</dd>
</dl>

<dl>
<dd>

**price:** `CreateStoreOrderLineEcommerceRequestPrice` 
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — A unique identifier for the product associated with the order line item.
    
</dd>
</dl>

<dl>
<dd>

**product_variant_id:** `str` — A unique identifier for the product variant associated with the order line item.
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `int` — The quantity of an order line item.
    
</dd>
</dl>

<dl>
<dd>

**discount:** `typing.Optional[CreateStoreOrderLineEcommerceRequestDiscount]` 
    
</dd>
</dl>

<dl>
<dd>

**product:** `typing.Optional[EcommerceStoresOrdersPost]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store_order_line</a>(...) -> ECommerceOrderLineItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific order line item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store_order_line(
    store_id="store_id",
    order_id="order_id",
    line_id="line_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The id for the order in a store.
    
</dd>
</dl>

<dl>
<dd>

**line_id:** `str` — The id for the line item of an order.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store_order_line</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific order line item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store_order_line(
    store_id="store_id",
    order_id="order_id",
    line_id="line_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The id for the order in a store.
    
</dd>
</dl>

<dl>
<dd>

**line_id:** `str` — The id for the line item of an order.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store_order_line</a>(...) -> ECommerceOrderLineItem</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific order line item.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store_order_line(
    store_id="store_id",
    order_id="order_id",
    line_id="line_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**order_id:** `str` — The id for the order in a store.
    
</dd>
</dl>

<dl>
<dd>

**line_id:** `str` — The id for the line item of an order.
    
</dd>
</dl>

<dl>
<dd>

**discount:** `typing.Optional[UpdateStoreOrderLineEcommerceRequestDiscount]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for the order line item.
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[UpdateStoreOrderLineEcommerceRequestPrice]` 
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `typing.Optional[str]` — A unique identifier for the product associated with the order line item.
    
</dd>
</dl>

<dl>
<dd>

**product_variant_id:** `typing.Optional[str]` — A unique identifier for the product variant associated with the order line item.
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[int]` — The quantity of an order line item.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_store_products</a>(...) -> ListStoreProductsEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a store's products.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_store_products(
    store_id="store_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store_product</a>(...) -> ECommerceProduct</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new product to a store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient, EcommerceStoresOrdersPostVariantsItem
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**request:** `EcommerceStoresOrdersPost` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store_product</a>(...) -> ECommerceProduct</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific product.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store_product(
    store_id="store_id",
    product_id="product_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">upsert_store_product</a>(...) -> ECommerceProduct</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific product.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.upsert_store_product(
    store_id="store_id",
    product_id="product_id",
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**id:** `UpsertStoreProductEcommerceRequestId` — A unique identifier for the product.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of a product.
    
</dd>
</dl>

<dl>
<dd>

**handle:** `typing.Optional[str]` — The handle of a product.
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[str]` — The image URL for a product.
    
</dd>
</dl>

<dl>
<dd>

**images:** `typing.Optional[typing.List[UpsertStoreProductEcommerceRequestImagesItem]]` — An array of the product's images.
    
</dd>
</dl>

<dl>
<dd>

**published_at_foreign:** `typing.Optional[str]` — The date and time the product was published.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of a product.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The type of product.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL for a product.
    
</dd>
</dl>

<dl>
<dd>

**variants:** `typing.Optional[typing.List[UpsertStoreProductEcommerceRequestVariantsItem]]` — An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.
    
</dd>
</dl>

<dl>
<dd>

**vendor:** `typing.Optional[str]` — The vendor for a product.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store_product</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a product.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store_product(
    store_id="store_id",
    product_id="product_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store_product</a>(...) -> ECommerceProduct</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific product.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store_product(
    store_id="store_id",
    product_id="product_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of a product.
    
</dd>
</dl>

<dl>
<dd>

**handle:** `typing.Optional[str]` — The handle of a product.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[UpdateStoreProductEcommerceRequestId]` — A unique identifier for the product.
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[str]` — The image URL for a product.
    
</dd>
</dl>

<dl>
<dd>

**images:** `typing.Optional[typing.List[UpdateStoreProductEcommerceRequestImagesItem]]` — An array of the product's images.
    
</dd>
</dl>

<dl>
<dd>

**published_at_foreign:** `typing.Optional[str]` — The date and time the product was published in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of a product.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The type of product.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL for a product.
    
</dd>
</dl>

<dl>
<dd>

**variants:** `typing.Optional[typing.List[UpdateStoreProductEcommerceRequestVariantsItem]]` — An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.
    
</dd>
</dl>

<dl>
<dd>

**vendor:** `typing.Optional[str]` — The vendor for a product.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_store_product_images</a>(...) -> ListStoreProductImagesEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a product's images.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_store_product_images(
    store_id="store_id",
    product_id="product_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store_product_image</a>(...) -> CreateStoreProductImageEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new image to the product.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.create_store_product_image(
    store_id="store_id",
    product_id="product_id",
    id="id",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — A unique identifier for the product image.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — The URL for a product image.
    
</dd>
</dl>

<dl>
<dd>

**variant_ids:** `typing.Optional[typing.List[CreateStoreProductImageEcommerceRequestVariantIdsItem]]` — The list of product variants using the image.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store_product_image</a>(...) -> GetStoreProductImageEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific product image.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store_product_image(
    store_id="store_id",
    product_id="product_id",
    image_id="image_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**image_id:** `str` — The id for the product image.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store_product_image</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a product image.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store_product_image(
    store_id="store_id",
    product_id="product_id",
    image_id="image_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**image_id:** `str` — The id for the product image.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store_product_image</a>(...) -> UpdateStoreProductImageEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a product image.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store_product_image(
    store_id="store_id",
    product_id="product_id",
    image_id="image_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**image_id:** `str` — The id for the product image.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for the product image.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL for a product image.
    
</dd>
</dl>

<dl>
<dd>

**variant_ids:** `typing.Optional[typing.List[UpdateStoreProductImageEcommerceRequestVariantIdsItem]]` — The list of product variants using the image.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_store_product_variants</a>(...) -> ListStoreProductVariantsEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a product's variants.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_store_product_variants(
    store_id="store_id",
    product_id="product_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store_product_variant</a>(...) -> ECommerceProductVariant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new variant to the product.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.create_store_product_variant(
    store_id="store_id",
    product_id="product_id",
    id="id",
    title="Cat Hat",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**id:** `CreateStoreProductVariantEcommerceRequestId` — A unique identifier for the product variant.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The title of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**backorders:** `typing.Optional[str]` — The backorders of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[str]` — The image URL for a product variant.
    
</dd>
</dl>

<dl>
<dd>

**inventory_quantity:** `typing.Optional[int]` — The inventory quantity of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[CreateStoreProductVariantEcommerceRequestPrice]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` — The stock keeping unit (SKU) of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL for a product variant.
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[str]` — The visibility of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store_product_variant</a>(...) -> ECommerceProductVariant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific product variant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store_product_variant(
    store_id="store_id",
    product_id="product_id",
    variant_id="variant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**variant_id:** `str` — The id for the product variant.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">upsert_store_product_variant</a>(...) -> ECommerceProductVariant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add or update a product variant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.upsert_store_product_variant(
    store_id="store_id",
    product_id="product_id",
    variant_id="variant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**variant_id:** `str` — The id for the product variant.
    
</dd>
</dl>

<dl>
<dd>

**backorders:** `typing.Optional[str]` — The backorders of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for the product variant.
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[str]` — The image URL for a product variant.
    
</dd>
</dl>

<dl>
<dd>

**inventory_quantity:** `typing.Optional[int]` — The inventory quantity of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[UpsertStoreProductVariantEcommerceRequestPrice]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` — The stock keeping unit (SKU) of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL for a product variant.
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[str]` — The visibility of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store_product_variant</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a product variant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store_product_variant(
    store_id="store_id",
    product_id="product_id",
    variant_id="variant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**variant_id:** `str` — The id for the product variant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store_product_variant</a>(...) -> ECommerceProductVariant</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a product variant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store_product_variant(
    store_id="store_id",
    product_id="product_id",
    variant_id="variant_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**product_id:** `str` — The id for the product of a store.
    
</dd>
</dl>

<dl>
<dd>

**variant_id:** `str` — The id for the product variant.
    
</dd>
</dl>

<dl>
<dd>

**backorders:** `typing.Optional[str]` — The backorders of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**image_url:** `typing.Optional[str]` — The image URL for a product variant.
    
</dd>
</dl>

<dl>
<dd>

**inventory_quantity:** `typing.Optional[int]` — The inventory quantity of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[UpdateStoreProductVariantEcommerceRequestPrice]` 
    
</dd>
</dl>

<dl>
<dd>

**sku:** `typing.Optional[str]` — The stock keeping unit (SKU) of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — The URL for a product variant.
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[str]` — The visibility of a product variant.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_store_promo_rules</a>(...) -> ListStorePromoRulesEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a store's promo rules.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_store_promo_rules(
    store_id="store_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store_promo_rule</a>(...) -> ECommercePromoRule</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new promo rule to a store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.create_store_promo_rule(
    store_id="store_id",
    amount=1.1,
    description="Save BIG during our summer sale!",
    id="id",
    target="per_item",
    type="fixed",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `CreateStorePromoRuleEcommerceRequestAmount` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — The description of a promotion restricted to UTF-8 characters with max length 255.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — A unique identifier for the promo rule. If Ecommerce platform does not support promo rule, use promo code id as promo rule id. Restricted to UTF-8 characters with max length 50.
    
</dd>
</dl>

<dl>
<dd>

**target:** `CreateStorePromoRuleEcommerceRequestTarget` — The target that the discount applies to.
    
</dd>
</dl>

<dl>
<dd>

**type:** `CreateStorePromoRuleEcommerceRequestType` — Type of discount. For free shipping set type to fixed.
    
</dd>
</dl>

<dl>
<dd>

**created_at_foreign:** `typing.Optional[str]` — The date and time the promotion was created in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the promo rule is currently enabled.
    
</dd>
</dl>

<dl>
<dd>

**ends_at:** `typing.Optional[CreateStorePromoRuleEcommerceRequestEndsAt]` 
    
</dd>
</dl>

<dl>
<dd>

**starts_at:** `typing.Optional[CreateStorePromoRuleEcommerceRequestStartsAt]` 
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title that will show up in promotion campaign. Restricted to UTF-8 characters with max length of 100 bytes.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_foreign:** `typing.Optional[str]` — The date and time the promotion was updated in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store_promo_rule</a>(...) -> ECommercePromoRule</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific promo rule.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store_promo_rule(
    store_id="store_id",
    promo_rule_id="promo_rule_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**promo_rule_id:** `str` — The id for the promo rule of a store.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store_promo_rule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a promo rule from a store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store_promo_rule(
    store_id="store_id",
    promo_rule_id="promo_rule_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**promo_rule_id:** `str` — The id for the promo rule of a store.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store_promo_rule</a>(...) -> ECommercePromoRule</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a promo rule.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store_promo_rule(
    store_id="store_id",
    promo_rule_id="promo_rule_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**promo_rule_id:** `str` — The id for the promo rule of a store.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[UpdateStorePromoRuleEcommerceRequestAmount]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_foreign:** `typing.Optional[str]` — The date and time the promotion was created in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of a promotion restricted to UTF-8 characters with max length 255.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the promo rule is currently enabled.
    
</dd>
</dl>

<dl>
<dd>

**ends_at:** `typing.Optional[UpdateStorePromoRuleEcommerceRequestEndsAt]` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for the promo rule. If Ecommerce platform does not support promo rule, use promo code id as promo rule id. Restricted to UTF-8 characters with max length 50.
    
</dd>
</dl>

<dl>
<dd>

**starts_at:** `typing.Optional[UpdateStorePromoRuleEcommerceRequestStartsAt]` 
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[UpdateStorePromoRuleEcommerceRequestTarget]` — The target that the discount applies to.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title that will show up in promotion campaign. Restricted to UTF-8 characters with max length of 100 bytes.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdateStorePromoRuleEcommerceRequestType]` — Type of discount. For free shipping set type to fixed.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_foreign:** `typing.Optional[str]` — The date and time the promotion was updated in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">list_store_promo_rule_promo_codes</a>(...) -> ListStorePromoRulePromoCodesEcommerceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a store's promo codes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.list_store_promo_rule_promo_codes(
    store_id="store_id",
    promo_rule_id="promo_rule_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**promo_rule_id:** `str` — The id for the promo rule of a store.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">create_store_promo_rule_promo_code</a>(...) -> ECommercePromoCode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new promo code to a store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.create_store_promo_rule_promo_code(
    store_id="store_id",
    promo_rule_id="promo_rule_id",
    code="summersale",
    id="id",
    redemption_url="A url that applies promo code directly at checkout or a url that points to sale page or store url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**promo_rule_id:** `str` — The id for the promo rule of a store.
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — The discount code. Restricted to UTF-8 characters with max length 50.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — A unique identifier for the promo code. Restricted to UTF-8 characters with max length 50.
    
</dd>
</dl>

<dl>
<dd>

**redemption_url:** `str` — The url that should be used in the promotion campaign restricted to UTF-8 characters with max length 2000.
    
</dd>
</dl>

<dl>
<dd>

**created_at_foreign:** `typing.Optional[str]` — The date and time the promotion was created in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the promo code is currently enabled.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_foreign:** `typing.Optional[str]` — The date and time the promotion was updated in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**usage_count:** `typing.Optional[int]` — Number of times promo code has been used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">get_store_promo_rule_promo_code</a>(...) -> ECommercePromoCode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific promo code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.get_store_promo_rule_promo_code(
    store_id="store_id",
    promo_rule_id="promo_rule_id",
    promo_code_id="promo_code_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**promo_rule_id:** `str` — The id for the promo rule of a store.
    
</dd>
</dl>

<dl>
<dd>

**promo_code_id:** `str` — The id for the promo code of a store.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">delete_store_promo_rule_promo_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a promo code from a store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.delete_store_promo_rule_promo_code(
    store_id="store_id",
    promo_rule_id="promo_rule_id",
    promo_code_id="promo_code_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**promo_rule_id:** `str` — The id for the promo rule of a store.
    
</dd>
</dl>

<dl>
<dd>

**promo_code_id:** `str` — The id for the promo code of a store.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ecommerce.<a href="src/mailchimp_marketing/ecommerce/client.py">update_store_promo_rule_promo_code</a>(...) -> ECommercePromoCode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a promo code.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ecommerce.update_store_promo_rule_promo_code(
    store_id="store_id",
    promo_rule_id="promo_rule_id",
    promo_code_id="promo_code_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**store_id:** `str` — The store id.
    
</dd>
</dl>

<dl>
<dd>

**promo_rule_id:** `str` — The id for the promo rule of a store.
    
</dd>
</dl>

<dl>
<dd>

**promo_code_id:** `str` — The id for the promo code of a store.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — The discount code. Restricted to UTF-8 characters with max length 50.
    
</dd>
</dl>

<dl>
<dd>

**created_at_foreign:** `typing.Optional[str]` — The date and time the promotion was created in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether the promo code is currently enabled.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — A unique identifier for the promo code. Restricted to UTF-8 characters with max length 50.
    
</dd>
</dl>

<dl>
<dd>

**redemption_url:** `typing.Optional[str]` — The url that should be used in the promotion campaign restricted to UTF-8 characters with max length 2000.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_foreign:** `typing.Optional[str]` — The date and time the promotion was updated in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**usage_count:** `typing.Optional[int]` — Number of times promo code has been used.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FacebookAds
<details><summary><code>client.facebook_ads.<a href="src/mailchimp_marketing/facebook_ads/client.py">list</a>(...) -> ListFacebookAdsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get list of Facebook ads.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.facebook_ads.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListFacebookAdsRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListFacebookAdsRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.facebook_ads.<a href="src/mailchimp_marketing/facebook_ads/client.py">get</a>(...) -> FacebookAds</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a Facebook ad.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.facebook_ads.get(
    outreach_id="outreach_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**outreach_id:** `str` — The outreach id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## FileManager
<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">list</a>() -> typing.List[ListFileManagerResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about the file-manager endpoint's resources
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">list_files</a>(...) -> ListFilesFileManagerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of available images and files stored in the File Manager for the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.list_files()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The file type for the File Manager file.
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — The Mailchimp account user who created the File Manager file.
    
</dd>
</dl>

<dl>
<dd>

**before_created_at:** `typing.Optional[str]` — Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_created_at:** `typing.Optional[str]` — Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListFilesFileManagerRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListFilesFileManagerRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">create_file</a>(...) -> GalleryFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a new image or file to the File Manager.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.create_file(
    file_data="file_data",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_data:** `str` — The base64-encoded contents of the file.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the file.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[int]` — The id of the folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">get_file</a>(...) -> GalleryFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific file in the File Manager.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.get_file(
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The unique id for the File Manager file.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">delete_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a specific file from the File Manager.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.delete_file(
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The unique id for the File Manager file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">update_file</a>(...) -> GalleryFile</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a file in the File Manager.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.update_file(
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — The unique id for the File Manager file.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[int]` — The id of the folder. Setting `folder_id` to `0` will remove a file from its current folder.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the file.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">list_folders</a>(...) -> ListFoldersFileManagerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all folders in the File Manager.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.list_folders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — The Mailchimp account user who created the File Manager file.
    
</dd>
</dl>

<dl>
<dd>

**before_created_at:** `typing.Optional[str]` — Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_created_at:** `typing.Optional[str]` — Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">create_folder</a>(...) -> CreateFolderFileManagerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new folder in the File Manager.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.create_folder(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">get_folder</a>(...) -> GetFolderFileManagerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific folder in the File Manager.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.get_folder(
    folder_id="folder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — The unique id for the File Manager folder.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">delete_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific folder in the File Manager.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.delete_folder(
    folder_id="folder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — The unique id for the File Manager folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">update_folder</a>(...) -> UpdateFolderFileManagerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific File Manager folder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.update_folder(
    folder_id="folder_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — The unique id for the File Manager folder.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.file_manager.<a href="src/mailchimp_marketing/file_manager/client.py">list_folder_files</a>(...) -> ListFolderFilesFileManagerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of available images and files stored in this folder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.file_manager.list_folder_files(
    folder_id="folder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — The unique id for the File Manager folder.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The file type for the File Manager file.
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — The Mailchimp account user who created the File Manager file.
    
</dd>
</dl>

<dl>
<dd>

**before_created_at:** `typing.Optional[str]` — Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_created_at:** `typing.Optional[str]` — Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListFolderFilesFileManagerRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListFolderFilesFileManagerRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## LandingPages
<details><summary><code>client.landing_pages.<a href="src/mailchimp_marketing/landing_pages/client.py">list</a>(...) -> ListLandingPagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all landing pages.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.landing_pages.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListLandingPagesRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListLandingPagesRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.landing_pages.<a href="src/mailchimp_marketing/landing_pages/client.py">create</a>(...) -> LandingPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an unpublished and contentless Mailchimp landing page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.landing_pages.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**use_default_list:** `typing.Optional[bool]` — Will create the Landing Page using the account's Default List instead of requiring a list_id.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of this landing page.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `typing.Optional[str]` — The list's ID associated with this landing page.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of this landing page.
    
</dd>
</dl>

<dl>
<dd>

**store_id:** `typing.Optional[str]` — The ID of the store associated with this landing page.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[int]` — The template_id of this landing page.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of this landing page seen in the browser's title bar.
    
</dd>
</dl>

<dl>
<dd>

**tracking:** `typing.Optional[CreateLandingPagesRequestTracking]` — The tracking settings applied to this landing page.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CreateLandingPagesRequestType]` — The type of template the landing page has.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.landing_pages.<a href="src/mailchimp_marketing/landing_pages/client.py">get</a>(...) -> LandingPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.landing_pages.get(
    page_id="page_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_id:** `str` — The unique id for the page.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.landing_pages.<a href="src/mailchimp_marketing/landing_pages/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a landing page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.landing_pages.delete(
    page_id="page_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_id:** `str` — The unique id for the page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.landing_pages.<a href="src/mailchimp_marketing/landing_pages/client.py">update</a>(...) -> LandingPage</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a landing page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.landing_pages.update(
    page_id="page_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_id:** `str` — The unique id for the page.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of this landing page.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `typing.Optional[str]` — The list's ID associated with this landing page.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of this landing page.
    
</dd>
</dl>

<dl>
<dd>

**store_id:** `typing.Optional[str]` — The ID of the store associated with this landing page.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of this landing page seen in the browser's title bar.
    
</dd>
</dl>

<dl>
<dd>

**tracking:** `typing.Optional[UpdateLandingPagesRequestTracking]` — The tracking settings applied to this landing page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.landing_pages.<a href="src/mailchimp_marketing/landing_pages/client.py">create_action_publish</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish a landing page that is in draft, unpublished, or has been previously published and edited.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.landing_pages.create_action_publish(
    page_id="page_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_id:** `str` — The unique id for the page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.landing_pages.<a href="src/mailchimp_marketing/landing_pages/client.py">create_action_unpublish</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unpublish a landing page that is in draft or has been published.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.landing_pages.create_action_unpublish(
    page_id="page_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_id:** `str` — The unique id for the page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.landing_pages.<a href="src/mailchimp_marketing/landing_pages/client.py">list_content</a>(...) -> ListContentLandingPagesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the the HTML for your landing page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.landing_pages.list_content(
    page_id="page_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_id:** `str` — The unique id for the page.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## lists
<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list</a>(...) -> ListListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about all lists in the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**before_date_created:** `typing.Optional[str]` — Restrict response to lists created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_date_created:** `typing.Optional[str]` — Restrict results to lists created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**before_campaign_last_sent:** `typing.Optional[str]` — Restrict results to lists created before the last campaign send date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_campaign_last_sent:** `typing.Optional[str]` — Restrict results to lists created after the last campaign send date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Restrict results to lists that include a specific subscriber's email address.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListListsRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListListsRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**has_ecommerce_store:** `typing.Optional[bool]` — Restrict results to lists that contain an active, connected, undeleted ecommerce store.
    
</dd>
</dl>

<dl>
<dd>

**include_total_contacts:** `typing.Optional[bool]` — Deprecated. Return the total_contacts field in the stats response, which contains an approximate count of subscribed, unsubscribed, and transactional contacts. For a complete audience contact count, use the /audiences endpoint instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create</a>(...) -> SubscriberList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new list in your Mailchimp account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment
from mailchimp_marketing.lists import CreateListsRequestCampaignDefaults, CreateListsRequestContact

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create(
    campaign_defaults=CreateListsRequestCampaignDefaults(
        from_email="from_email",
        from_name="from_name",
        language="language",
        subject="subject",
    ),
    contact=CreateListsRequestContact(
        address1="address1",
        city="city",
        company="company",
        country="country",
    ),
    email_type_option=True,
    name="name",
    permission_reminder="permission_reminder",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_defaults:** `CreateListsRequestCampaignDefaults` — [Default values for campaigns](https://mailchimp.com/help/edit-your-emails-subject-preview-text-from-name-or-from-email-address/) created for this list.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `CreateListsRequestContact` — [Contact information displayed in campaign footers](https://mailchimp.com/help/about-campaign-footers/) to comply with international spam laws.
    
</dd>
</dl>

<dl>
<dd>

**email_type_option:** `bool` — Whether the list supports [multiple formats for emails](https://mailchimp.com/help/audience-settings-and-defaults/). When set to `true`, subscribers can choose whether they want to receive HTML or plain-text emails. When set to `false`, subscribers will receive HTML emails, with a plain-text alternative backup.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the list.
    
</dd>
</dl>

<dl>
<dd>

**permission_reminder:** `str` — The [permission reminder](https://mailchimp.com/help/edit-the-permission-reminder/) for the list.
    
</dd>
</dl>

<dl>
<dd>

**double_optin:** `typing.Optional[bool]` — Whether or not to require the subscriber to confirm subscription via email.
    
</dd>
</dl>

<dl>
<dd>

**marketing_permissions:** `typing.Optional[bool]` — Whether or not the list has marketing permissions (eg. GDPR) enabled.
    
</dd>
</dl>

<dl>
<dd>

**notify_on_subscribe:** `typing.Optional[str]` — The email address to send [subscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.
    
</dd>
</dl>

<dl>
<dd>

**notify_on_unsubscribe:** `typing.Optional[str]` — The email address to send [unsubscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.
    
</dd>
</dl>

<dl>
<dd>

**use_archive_bar:** `typing.Optional[bool]` — Whether campaigns for this list use the [Archive Bar](https://mailchimp.com/help/about-email-campaign-archives-and-pages/) in archives by default.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get</a>(...) -> SubscriberList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific list in your Mailchimp account. Results include list members who have signed up but haven't confirmed their subscription yet and unsubscribed or cleaned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**include_total_contacts:** `typing.Optional[bool]` — Deprecated. Return the total_contacts field in the stats response, which contains an approximate count of subscribed, unsubscribed, and transactional contacts. For a complete audience contact count, use the /audiences endpoint instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">batch_subscribe_or_unsubscribe</a>(...) -> BatchSubscribeOrUnsubscribeListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch subscribe or unsubscribe list members.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.batch_subscribe_or_unsubscribe(
    list_id="list_id",
    members=[],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.List[BatchSubscribeOrUnsubscribeListsRequestMembersItem]` — An array of objects, each representing an email address and the subscription status for a specific list. Up to 500 members may be added or updated with each API call.
    
</dd>
</dl>

<dl>
<dd>

**skip_merge_validation:** `typing.Optional[bool]` — If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**skip_duplicate_check:** `typing.Optional[bool]` — If skip_duplicate_check is true, we will ignore duplicates sent in the request when using the batch sub/unsub on the lists endpoint. The status of the first appearance in the request will be saved. This defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**sync_tags:** `typing.Optional[bool]` — Whether this batch operation will replace all existing tags with tags in request.
    
</dd>
</dl>

<dl>
<dd>

**update_existing:** `typing.Optional[bool]` — Whether this batch operation will change existing members' subscription status.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a list from your Mailchimp account. If you delete a list, you'll lose the list history—including subscriber activity, unsubscribes, complaints, and bounces. You’ll also lose subscribers’ email addresses, unless you exported and backed up your list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.delete(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">update</a>(...) -> SubscriberList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the settings for a specific list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.update(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**campaign_defaults:** `typing.Optional[UpdateListsRequestCampaignDefaults]` — [Default values for campaigns](https://mailchimp.com/help/edit-your-emails-subject-preview-text-from-name-or-from-email-address/) created for this list.
    
</dd>
</dl>

<dl>
<dd>

**contact:** `typing.Optional[UpdateListsRequestContact]` — [Contact information displayed in campaign footers](https://mailchimp.com/help/about-campaign-footers/) to comply with international spam laws.
    
</dd>
</dl>

<dl>
<dd>

**double_optin:** `typing.Optional[bool]` — Whether or not to require the subscriber to confirm subscription via email.
    
</dd>
</dl>

<dl>
<dd>

**email_type_option:** `typing.Optional[bool]` — Whether the list supports [multiple formats for emails](https://mailchimp.com/help/audience-settings-and-defaults/). When set to `true`, subscribers can choose whether they want to receive HTML or plain-text emails. When set to `false`, subscribers will receive HTML emails, with a plain-text alternative backup.
    
</dd>
</dl>

<dl>
<dd>

**marketing_permissions:** `typing.Optional[bool]` — Whether or not the list has marketing permissions (eg. GDPR) enabled.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the list.
    
</dd>
</dl>

<dl>
<dd>

**notify_on_subscribe:** `typing.Optional[str]` — The email address to send [subscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.
    
</dd>
</dl>

<dl>
<dd>

**notify_on_unsubscribe:** `typing.Optional[str]` — The email address to send [unsubscribe notifications](https://mailchimp.com/help/change-subscribe-and-unsubscribe-notifications/) to.
    
</dd>
</dl>

<dl>
<dd>

**permission_reminder:** `typing.Optional[str]` — The [permission reminder](https://mailchimp.com/help/edit-the-permission-reminder/) for the list.
    
</dd>
</dl>

<dl>
<dd>

**use_archive_bar:** `typing.Optional[bool]` — Whether campaigns for this list use the [Archive Bar](https://mailchimp.com/help/about-email-campaign-archives-and-pages/) in archives by default.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_abuse_reports</a>(...) -> ListAbuseReportsListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all abuse reports for a specific list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_abuse_reports(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get_abuse_report</a>(...) -> ListsAbuseReports</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about a specific abuse report.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get_abuse_report(
    list_id="list_id",
    report_id="report_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**report_id:** `str` — The id for the abuse report.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_activity</a>(...) -> ListActivityListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get up to the previous 180 days of daily detailed aggregated activity stats for a list, not including Automation activity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_activity(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_clients</a>(...) -> ListClientsListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of the top email clients based on user-agent strings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_clients(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_growth_history</a>(...) -> ListGrowthHistoryListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a month-by-month summary of a specific list's growth activity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_growth_history(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListGrowthHistoryListsRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListGrowthHistoryListsRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get_growth_history</a>(...) -> GrowthHistory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a summary of a specific list's growth activity for a specific month and year.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get_growth_history(
    list_id="list_id",
    month="month",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**month:** `str` — A specific month of list growth history.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_interest_categories</a>(...) -> ListInterestCategoriesListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a list's interest categories.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_interest_categories(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Restrict results a type of interest group
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListInterestCategoriesListsRequestSortField]` — Returns interest categories sorted by the specified field. Defaults to display_order.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListInterestCategoriesListsRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_interest_category</a>(...) -> InterestCategory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new interest category.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_interest_category(
    list_id="list_id",
    title="title",
    type="checkboxes",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**title:** `str` — The text description of this category. This field appears on signup forms and is often phrased as a question.
    
</dd>
</dl>

<dl>
<dd>

**type:** `CreateInterestCategoryListsRequestType` — Determines how this category’s interests appear on signup forms.
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[int]` — The order that the categories are displayed in the list. Lower numbers display first.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get_interest_category</a>(...) -> InterestCategory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific interest category.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get_interest_category(
    list_id="list_id",
    interest_category_id="interest_category_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**interest_category_id:** `str` — The unique ID for the interest category.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">delete_interest_category</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific interest category.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.delete_interest_category(
    list_id="list_id",
    interest_category_id="interest_category_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**interest_category_id:** `str` — The unique ID for the interest category.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">update_interest_category</a>(...) -> InterestCategory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific interest category.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.update_interest_category(
    list_id="list_id",
    interest_category_id="interest_category_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**interest_category_id:** `str` — The unique ID for the interest category.
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[int]` — The order that the categories are displayed in the list. Lower numbers display first.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The text description of this category. This field appears on signup forms and is often phrased as a question.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[UpdateInterestCategoryListsRequestType]` — Determines how this category’s interests appear on signup forms.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_interest_category_interests</a>(...) -> ListInterestCategoryInterestsListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of this category's interests.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_interest_category_interests(
    list_id="list_id",
    interest_category_id="interest_category_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**interest_category_id:** `str` — The unique ID for the interest category.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_interest_category_interest</a>(...) -> Interest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new interest or 'group name' for a specific category.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_interest_category_interest(
    list_id="list_id",
    interest_category_id="interest_category_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**interest_category_id:** `str` — The unique ID for the interest category.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the interest. This can be shown publicly on a subscription form.
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[int]` — The display order for interests.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get_interest_category_interest</a>(...) -> Interest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get interests or 'group names' for a specific category.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get_interest_category_interest(
    list_id="list_id",
    interest_category_id="interest_category_id",
    interest_id="interest_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**interest_category_id:** `str` — The unique ID for the interest category.
    
</dd>
</dl>

<dl>
<dd>

**interest_id:** `str` — The specific interest or 'group name'.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">delete_interest_category_interest</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete interests or group names in a specific category.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.delete_interest_category_interest(
    list_id="list_id",
    interest_category_id="interest_category_id",
    interest_id="interest_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**interest_category_id:** `str` — The unique ID for the interest category.
    
</dd>
</dl>

<dl>
<dd>

**interest_id:** `str` — The specific interest or 'group name'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">update_interest_category_interest</a>(...) -> Interest</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update interests or 'group names' for a specific category.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.update_interest_category_interest(
    list_id="list_id",
    interest_category_id="interest_category_id",
    interest_id="interest_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**interest_category_id:** `str` — The unique ID for the interest category.
    
</dd>
</dl>

<dl>
<dd>

**interest_id:** `str` — The specific interest or 'group name'.
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[int]` — The display order for interests.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the interest. This can be shown publicly on a subscription form.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_locations</a>(...) -> ListLocationsListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the locations (countries) that the list's subscribers have been tagged to based on geocoding their IP address.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_locations(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_members</a>(...) -> ListMembersListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about members in a specific Mailchimp list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_members(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**email_type:** `typing.Optional[str]` — The email type.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListMembersListsRequestStatus]` — The subscriber's status.
    
</dd>
</dl>

<dl>
<dd>

**since_timestamp_opt:** `typing.Optional[str]` — Restrict results to subscribers who opted-in after the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**before_timestamp_opt:** `typing.Optional[str]` — Restrict results to subscribers who opted-in before the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_last_changed:** `typing.Optional[str]` — Restrict results to subscribers whose information changed after the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**before_last_changed:** `typing.Optional[str]` — Restrict results to subscribers whose information changed before the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**unique_email_id:** `typing.Optional[str]` — A unique identifier for the email address across all Mailchimp lists.
    
</dd>
</dl>

<dl>
<dd>

**vip_only:** `typing.Optional[bool]` — A filter to return only the list's VIP members. Passing `true` will restrict results to VIP list members, passing `false` will return all list members.
    
</dd>
</dl>

<dl>
<dd>

**interest_category_id:** `typing.Optional[str]` — The unique id for the interest category.
    
</dd>
</dl>

<dl>
<dd>

**interest_ids:** `typing.Optional[str]` — Used to filter list members by interests. Must be accompanied by interest_category_id and interest_match. The value must be a comma separated list of interest ids present for any supplied interest categories.
    
</dd>
</dl>

<dl>
<dd>

**interest_match:** `typing.Optional[ListMembersListsRequestInterestMatch]` — Used to filter list members by interests. Must be accompanied by interest_category_id and interest_ids. "any" will match a member with any of the interest supplied, "all" will only match members with every interest supplied, and "none" will match members without any of the interest supplied.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListMembersListsRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListMembersListsRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**since_last_campaign:** `typing.Optional[bool]` — Filter subscribers by those subscribed/unsubscribed/pending/cleaned since last email campaign send. Member status is required to use this filter.
    
</dd>
</dl>

<dl>
<dd>

**unsubscribed_since:** `typing.Optional[str]` — Filter subscribers by those unsubscribed since a specific date. Using any status other than unsubscribed with this filter will result in an error.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_member</a>(...) -> ListMembers</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new member to the list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_member(
    list_id="list_id",
    email_address="email_address",
    status="subscribed",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `str` — Email address for a subscriber.
    
</dd>
</dl>

<dl>
<dd>

**status:** `CreateMemberListsRequestStatus` — Subscriber's current status.
    
</dd>
</dl>

<dl>
<dd>

**skip_merge_validation:** `typing.Optional[bool]` — If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**email_type:** `typing.Optional[str]` — Type of email this member asked to get ('html' or 'text').
    
</dd>
</dl>

<dl>
<dd>

**interests:** `typing.Optional[typing.Dict[str, bool]]` — The key of this object's properties is the ID of the interest in question.
    
</dd>
</dl>

<dl>
<dd>

**ip_opt:** `typing.Optional[str]` — The IP address the subscriber used to confirm their opt-in status.
    
</dd>
</dl>

<dl>
<dd>

**ip_signup:** `typing.Optional[str]` — IP address the subscriber signed up from.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — If set/detected, the [subscriber's language](https://mailchimp.com/help/view-and-edit-contact-languages/).
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[CreateMemberListsRequestLocation]` — Subscriber location information.
    
</dd>
</dl>

<dl>
<dd>

**marketing_permissions:** `typing.Optional[typing.List[CreateMemberListsRequestMarketingPermissionsItem]]` — The marketing permissions for the subscriber.
    
</dd>
</dl>

<dl>
<dd>

**merge_fields:** `typing.Optional[typing.Dict[str, CreateMemberListsRequestMergeFieldsValue]]` — A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — The tags that are associated with a member.
    
</dd>
</dl>

<dl>
<dd>

**timestamp_opt:** `typing.Optional[CreateMemberListsRequestTimestampOpt]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_signup:** `typing.Optional[CreateMemberListsRequestTimestampSignup]` 
    
</dd>
</dl>

<dl>
<dd>

**vip:** `typing.Optional[bool]` — [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get_member</a>(...) -> ListMembers</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific list member, including a currently subscribed, unsubscribed, or bounced member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get_member(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">upsert_member</a>(...) -> ListMembers</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add or update a list member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.upsert_member(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
    email_address="email_address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `str` — Email address for a subscriber. This value is required only if the email address is not already present on the list.
    
</dd>
</dl>

<dl>
<dd>

**skip_merge_validation:** `typing.Optional[bool]` — If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**email_type:** `typing.Optional[str]` — Type of email this member asked to get ('html' or 'text').
    
</dd>
</dl>

<dl>
<dd>

**interests:** `typing.Optional[typing.Dict[str, bool]]` — The key of this object's properties is the ID of the interest in question.
    
</dd>
</dl>

<dl>
<dd>

**ip_opt:** `typing.Optional[str]` — The IP address the subscriber used to confirm their opt-in status.
    
</dd>
</dl>

<dl>
<dd>

**ip_signup:** `typing.Optional[str]` — IP address the subscriber signed up from.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — If set/detected, the [subscriber's language](https://mailchimp.com/help/view-and-edit-contact-languages/).
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[UpsertMemberListsRequestLocation]` — Subscriber location information.
    
</dd>
</dl>

<dl>
<dd>

**marketing_permissions:** `typing.Optional[typing.List[UpsertMemberListsRequestMarketingPermissionsItem]]` — The marketing permissions for the subscriber.
    
</dd>
</dl>

<dl>
<dd>

**merge_fields:** `typing.Optional[typing.Dict[str, UpsertMemberListsRequestMergeFieldsValue]]` — A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpsertMemberListsRequestStatus]` — Subscriber's current status.
    
</dd>
</dl>

<dl>
<dd>

**status_if_new:** `typing.Optional[UpsertMemberListsRequestStatusIfNew]` — Subscriber's status. This value is required only if the email address is not already present on the list.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.List[str]]` — The tags that are associated with a member.
    
</dd>
</dl>

<dl>
<dd>

**timestamp_opt:** `typing.Optional[UpsertMemberListsRequestTimestampOpt]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_signup:** `typing.Optional[UpsertMemberListsRequestTimestampSignup]` 
    
</dd>
</dl>

<dl>
<dd>

**vip:** `typing.Optional[bool]` — [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">delete_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive a list member. To permanently delete, use the delete-permanent action.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.delete_member(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">update_member</a>(...) -> ListMembers</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update information for a specific list member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.update_member(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**skip_merge_validation:** `typing.Optional[bool]` — If skip_merge_validation is true, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` — Email address for a subscriber.
    
</dd>
</dl>

<dl>
<dd>

**email_type:** `typing.Optional[str]` — Type of email this member asked to get ('html' or 'text').
    
</dd>
</dl>

<dl>
<dd>

**interests:** `typing.Optional[typing.Dict[str, bool]]` — The key of this object's properties is the ID of the interest in question.
    
</dd>
</dl>

<dl>
<dd>

**ip_opt:** `typing.Optional[str]` — The IP address the subscriber used to confirm their opt-in status.
    
</dd>
</dl>

<dl>
<dd>

**ip_signup:** `typing.Optional[str]` — IP address the subscriber signed up from.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — If set/detected, the [subscriber's language](https://mailchimp.com/help/view-and-edit-contact-languages/).
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[UpdateMemberListsRequestLocation]` — Subscriber location information.
    
</dd>
</dl>

<dl>
<dd>

**marketing_permissions:** `typing.Optional[typing.List[UpdateMemberListsRequestMarketingPermissionsItem]]` — The marketing permissions for the subscriber.
    
</dd>
</dl>

<dl>
<dd>

**merge_fields:** `typing.Optional[typing.Dict[str, UpdateMemberListsRequestMergeFieldsValue]]` — A dictionary of merge fields where the keys are the merge tags. See the [Merge Fields documentation](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for more about the structure.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[UpdateMemberListsRequestStatus]` — Subscriber's current status.
    
</dd>
</dl>

<dl>
<dd>

**timestamp_opt:** `typing.Optional[UpdateMemberListsRequestTimestampOpt]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_signup:** `typing.Optional[UpdateMemberListsRequestTimestampSignup]` 
    
</dd>
</dl>

<dl>
<dd>

**vip:** `typing.Optional[bool]` — [VIP status](https://mailchimp.com/help/designate-and-send-to-vip-contacts/) for subscriber.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_member_action_delete_permanent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete all personally identifiable information related to a list member, and remove them from a list. This will make it impossible to re-import the list member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_member_action_delete_permanent(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_member_activity</a>(...) -> ListMemberActivityListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the last 50 events of a member's activity on a specific list, including opens, clicks, and unsubscribes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_member_activity(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[typing.Union[ListMemberActivityListsRequestActionItem, typing.Sequence[ListMemberActivityListsRequestActionItem]]]` — A comma seperated list of actions to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_member_activity_feed</a>(...) -> ListMemberActivityFeedListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a member's activity on a specific list, including opens, clicks, and unsubscribes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_member_activity_feed(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**activity_filters:** `typing.Optional[typing.Union[ListMemberActivityFeedListsRequestActivityFiltersItem, typing.Sequence[ListMemberActivityFeedListsRequestActivityFiltersItem]]]` — A comma-separated list of activity filters that correspond to a set of activity types, e.g "?activity_filters=open,bounce,click".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_member_events</a>(...) -> ListMemberEventsListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get events for a contact.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_member_events(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_member_event</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add an event for a list member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_member_event(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name for this type of event ('purchased', 'visited', etc). Must be 2-30 characters in length
    
</dd>
</dl>

<dl>
<dd>

**is_syncing:** `typing.Optional[bool]` — Events created with the is_syncing value set to `true` will not trigger automations.
    
</dd>
</dl>

<dl>
<dd>

**occurred_at:** `typing.Optional[datetime.datetime]` — The date and time the event occurred in ISO 8601 format.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Dict[str, str]]` — An optional list of properties
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_member_goals</a>(...) -> ListMemberGoalsListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the last 50 Goal events for a member on a specific list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_member_goals(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_member_notes</a>(...) -> ListMemberNotesListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get recent notes for a specific list member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_member_notes(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListMemberNotesListsRequestSortField]` — Returns notes sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListMemberNotesListsRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_member_note</a>(...) -> MemberNotes</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new note for a specific subscriber.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_member_note(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — The content of the note. Note length is limited to 1,000 characters.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get_member_note</a>(...) -> MemberNotes</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific note for a specific list member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get_member_note(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
    note_id="note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` — The id for the note.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">delete_member_note</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific note for a specific list member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.delete_member_note(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
    note_id="note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` — The id for the note.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">update_member_note</a>(...) -> MemberNotes</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific note for a specific list member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.update_member_note(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
    note_id="note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**note_id:** `str` — The id for the note.
    
</dd>
</dl>

<dl>
<dd>

**note:** `typing.Optional[str]` — The content of the note. Note length is limited to 1,000 characters.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_member_tags</a>(...) -> ListMemberTagsListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the tags on a list member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_member_tags(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_member_tag</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add or remove tags from a list member. If a tag that does not exist is passed in and set as 'active', a new tag will be created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment
from mailchimp_marketing.lists import CreateMemberTagListsRequestTagsItem

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_member_tag(
    list_id="list_id",
    subscriber_hash="subscriber_hash",
    tags=[
        CreateMemberTagListsRequestTagsItem(
            name="name",
            status="inactive",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.List[CreateMemberTagListsRequestTagsItem]` — A list of tags assigned to the list member.
    
</dd>
</dl>

<dl>
<dd>

**is_syncing:** `typing.Optional[bool]` — When is_syncing is true, automations based on the tags in the request will not fire
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_merge_fields</a>(...) -> ListMergeFieldsListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all merge fields for an audience.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_merge_fields(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — The merge field type.
    
</dd>
</dl>

<dl>
<dd>

**required:** `typing.Optional[bool]` — Whether it's a required merge field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_merge_field</a>(...) -> MergeField</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new merge field for a specific audience.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_merge_field(
    list_id="list_id",
    name="name",
    type="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the merge field (audience field).
    
</dd>
</dl>

<dl>
<dd>

**type:** `CreateMergeFieldListsRequestType` — The [type](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for the merge field.
    
</dd>
</dl>

<dl>
<dd>

**default_value:** `typing.Optional[str]` — The default value for the merge field if `null`.
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[int]` — The order that the merge field displays on the list signup form.
    
</dd>
</dl>

<dl>
<dd>

**help_text:** `typing.Optional[str]` — Extra text to help the subscriber fill out the form.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[CreateMergeFieldListsRequestOptions]` — Extra options for some merge field types.
    
</dd>
</dl>

<dl>
<dd>

**public:** `typing.Optional[bool]` — Whether the merge field is displayed on the signup form.
    
</dd>
</dl>

<dl>
<dd>

**required:** `typing.Optional[bool]` — Whether the merge field is required to import a contact.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — The merge tag used for Mailchimp campaigns and [adding contact information](https://mailchimp.com/developer/marketing/docs/merge-fields/#add-merge-data-to-contacts).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get_merge_field</a>(...) -> MergeField</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific merge field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get_merge_field(
    list_id="list_id",
    merge_id="merge_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**merge_id:** `str` — The id for the merge field.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">delete_merge_field</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific merge field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.delete_merge_field(
    list_id="list_id",
    merge_id="merge_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**merge_id:** `str` — The id for the merge field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">update_merge_field</a>(...) -> MergeField</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific merge field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.update_merge_field(
    list_id="list_id",
    merge_id="merge_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**merge_id:** `str` — The id for the merge field.
    
</dd>
</dl>

<dl>
<dd>

**default_value:** `typing.Optional[str]` — The default value for the merge field if `null`.
    
</dd>
</dl>

<dl>
<dd>

**display_order:** `typing.Optional[int]` — The order that the merge field displays on the list signup form.
    
</dd>
</dl>

<dl>
<dd>

**help_text:** `typing.Optional[str]` — Extra text to help the subscriber fill out the form.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the merge field (audience field).
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[UpdateMergeFieldListsRequestOptions]` — Extra options for some merge field types.
    
</dd>
</dl>

<dl>
<dd>

**public:** `typing.Optional[bool]` — Whether the merge field is displayed on the signup form.
    
</dd>
</dl>

<dl>
<dd>

**required:** `typing.Optional[bool]` — Whether the merge field is required to import a contact.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — The merge tag used for Mailchimp campaigns and [adding contact information](https://mailchimp.com/developer/marketing/docs/merge-fields/#add-merge-data-to-contacts).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_segments</a>(...) -> ListSegmentsListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about all available segments for a specific list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_segments(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Limit results based on segment type.
    
</dd>
</dl>

<dl>
<dd>

**since_created_at:** `typing.Optional[str]` — Restrict results to segments created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**before_created_at:** `typing.Optional[str]` — Restrict results to segments created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**include_cleaned:** `typing.Optional[bool]` — Include cleaned members in response
    
</dd>
</dl>

<dl>
<dd>

**include_transactional:** `typing.Optional[bool]` — Include transactional members in response
    
</dd>
</dl>

<dl>
<dd>

**include_unsubscribed:** `typing.Optional[bool]` — Include unsubscribed members in response
    
</dd>
</dl>

<dl>
<dd>

**since_updated_at:** `typing.Optional[str]` — Restrict results to segments update after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**before_updated_at:** `typing.Optional[str]` — Restrict results to segments update before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**exclude_type:** `typing.Optional[ListSegmentsListsRequestExcludeType]` — Exclude results based on segment type. For example, use `exclude_type=static` to exclude tags from the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_segment</a>(...) -> List</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new segment in a specific list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_segment(
    list_id="list_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the segment.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[CreateSegmentListsRequestOptions]` — The [conditions of the segment](https://mailchimp.com/help/save-and-manage-segments/). Static and fuzzy segments don't have conditions.
    
</dd>
</dl>

<dl>
<dd>

**static_segment:** `typing.Optional[typing.List[str]]` — An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. Passing an empty array will create a static segment without any subscribers. This field cannot be provided with the options field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get_segment</a>(...) -> List</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific segment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get_segment(
    list_id="list_id",
    segment_id="segment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `str` — The unique id for the segment.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**include_cleaned:** `typing.Optional[bool]` — Include cleaned members in response
    
</dd>
</dl>

<dl>
<dd>

**include_transactional:** `typing.Optional[bool]` — Include transactional members in response
    
</dd>
</dl>

<dl>
<dd>

**include_unsubscribed:** `typing.Optional[bool]` — Include unsubscribed members in response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">batch_add_or_remove_members</a>(...) -> BatchAddOrRemoveMembersListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Batch add/remove list members to static segment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.batch_add_or_remove_members(
    list_id="list_id",
    segment_id="segment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `str` — The unique id for the segment.
    
</dd>
</dl>

<dl>
<dd>

**members_to_add:** `typing.Optional[typing.List[str]]` — An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. A maximum of 500 members can be sent.
    
</dd>
</dl>

<dl>
<dd>

**members_to_remove:** `typing.Optional[typing.List[str]]` — An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. A maximum of 500 members can be sent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">delete_segment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific segment in a list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.delete_segment(
    list_id="list_id",
    segment_id="segment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `str` — The unique id for the segment.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">update_segment</a>(...) -> List</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific segment in a list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.update_segment(
    list_id="list_id",
    segment_id="segment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `str` — The unique id for the segment.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the segment.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[UpdateSegmentListsRequestOptions]` — The [conditions of the segment](https://mailchimp.com/help/save-and-manage-segments/). Static and fuzzy segments don't have conditions.
    
</dd>
</dl>

<dl>
<dd>

**static_segment:** `typing.Optional[typing.List[str]]` — An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. Passing an empty array for an existing static segment will reset that segment and remove all members. This field cannot be provided with the `options` field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_segment_members</a>(...) -> ListSegmentMembersListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about members in a saved segment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_segment_members(
    list_id="list_id",
    segment_id="segment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `str` — The unique id for the segment.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**include_cleaned:** `typing.Optional[bool]` — Include cleaned members in response
    
</dd>
</dl>

<dl>
<dd>

**include_transactional:** `typing.Optional[bool]` — Include transactional members in response
    
</dd>
</dl>

<dl>
<dd>

**include_unsubscribed:** `typing.Optional[bool]` — Include unsubscribed members in response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_segment_member</a>(...) -> ListsSegmentsMembers</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a member to a static segment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_segment_member(
    list_id="list_id",
    segment_id="segment_id",
    email_address="email_address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `str` — The unique id for the segment.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `str` — Email address for a subscriber.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">delete_segment_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a member from the specified static segment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.delete_segment_member(
    list_id="list_id",
    segment_id="segment_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**segment_id:** `str` — The unique id for the segment.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_signup_forms</a>(...) -> ListSignupFormsListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get signup forms for a specific list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_signup_forms(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_signup_form</a>(...) -> SignupForm</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Customize a list's default signup form.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_signup_form(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**contents:** `typing.Optional[typing.List[CreateSignupFormListsRequestContentsItem]]` — The signup form body content.
    
</dd>
</dl>

<dl>
<dd>

**header:** `typing.Optional[CreateSignupFormListsRequestHeader]` — Options for customizing your signup form header.
    
</dd>
</dl>

<dl>
<dd>

**styles:** `typing.Optional[typing.List[CreateSignupFormListsRequestStylesItem]]` — An array of objects, each representing an element style for the signup form.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_surveys</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about all available surveys for a specific list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_surveys(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_survey</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a draft survey for an audience.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_survey(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of the survey.
    
</dd>
</dl>

<dl>
<dd>

**sections:** `typing.Optional[typing.List[SurveySectionRequest]]` — Initial survey sections.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get_survey</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details about a specific survey.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get_survey(
    list_id="list_id",
    survey_id="survey_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">delete_survey</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a survey.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.delete_survey(
    list_id="list_id",
    survey_id="survey_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">update_survey</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a survey. When sections is provided, send the complete section list in display order. Any existing section not included is deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.update_survey(
    list_id="list_id",
    survey_id="survey_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title of the survey.
    
</dd>
</dl>

<dl>
<dd>

**is_piped_to_inbox:** `typing.Optional[bool]` — Whether responses are sent to Mailchimp Inbox.
    
</dd>
</dl>

<dl>
<dd>

**sections:** `typing.Optional[typing.List[SurveySectionRequest]]` — The complete survey section list in display order. On update, sections omitted from this array are deleted. Include section id to update an existing section; omit section id to add a new section.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_list_survey_action_replicate</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replicate a survey.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_list_survey_action_replicate(
    list_id_path_param="list_id",
    survey_id="survey_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id_path_param:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title for the replicated survey.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `typing.Optional[str]` — The unique ID of the audience for the replicated survey. Defaults to the source survey audience.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_tag_search</a>(...) -> ListTagSearchListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for tags on a list by name. If no name is provided, will return all tags on the list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_tag_search(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The search query used to filter tags.  The search query will be compared to each tag as a prefix, so all tags that have a name starting with this field will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">list_webhooks</a>(...) -> ListWebhooksListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about all webhooks for a specific list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.list_webhooks(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">create_webhook</a>(...) -> CreateWebhookListsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new webhook for a specific list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.create_webhook(
    list_id="list_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddWebhook` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">get_webhook</a>(...) -> ListWebhooks</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific webhook.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.get_webhook(
    list_id="list_id",
    webhook_id="webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `str` — The webhook's id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">delete_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific webhook in a list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.delete_webhook(
    list_id="list_id",
    webhook_id="webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `str` — The webhook's id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.lists.<a href="src/mailchimp_marketing/lists/client.py">update_webhook</a>(...) -> ListWebhooks</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the settings for an existing webhook.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.lists.update_webhook(
    list_id="list_id",
    webhook_id="webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**webhook_id:** `str` — The webhook's id.
    
</dd>
</dl>

<dl>
<dd>

**request:** `AddWebhook` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## surveys
<details><summary><code>client.surveys.<a href="src/mailchimp_marketing/surveys/client.py">create_list_survey_action_create_email</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Utilize the List ID and Survey ID to generate a Campaign that links to your survey.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.surveys.create_list_survey_action_create_email(
    list_id="list_id",
    survey_id="survey_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.surveys.<a href="src/mailchimp_marketing/surveys/client.py">create_list_survey_action_publish</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish a survey that is in draft, unpublished, or has been previously published and edited.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.surveys.create_list_survey_action_publish(
    list_id="list_id",
    survey_id="survey_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.surveys.<a href="src/mailchimp_marketing/surveys/client.py">create_list_survey_action_unpublish</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unpublish a survey that has been published.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.surveys.create_list_survey_action_unpublish(
    list_id="list_id",
    survey_id="survey_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**list_id:** `str` — The unique ID for the list.
    
</dd>
</dl>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ping
<details><summary><code>client.ping.<a href="src/mailchimp_marketing/ping/client.py">list</a>() -> ListPingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A health check for the API that won't return any account-specific information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.ping.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## reporting
<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">list</a>() -> typing.List[ListReportingResponseItem]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about the reporting endpoint's resources.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">list_facebook_ads</a>(...) -> ListFacebookAdsReportingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get reports of Facebook ads.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.list_facebook_ads()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListFacebookAdsReportingRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListFacebookAdsReportingRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">get_facebook_ad</a>(...) -> ReportingFacebookAd</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get report of a Facebook ad.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.get_facebook_ad(
    outreach_id="outreach_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**outreach_id:** `str` — The outreach id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">list_facebook_ad_ecommerce_product_activity</a>(...) -> ListFacebookAdEcommerceProductActivityReportingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get breakdown of product activity for an outreach.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.list_facebook_ad_ecommerce_product_activity(
    outreach_id="outreach_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**outreach_id:** `str` — The outreach id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListFacebookAdEcommerceProductActivityReportingRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">list_landing_pages</a>(...) -> ListLandingPagesReportingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get reports of landing pages.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.list_landing_pages()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">get_landing_page</a>(...) -> LandingPageReport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get report of a landing page.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.get_landing_page(
    outreach_id="outreach_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**outreach_id:** `str` — The outreach id.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">list_surveys</a>(...) -> ListSurveysReportingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get reports for surveys.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.list_surveys()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">get_survey</a>(...) -> GetSurveyReportingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get report for a survey.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.get_survey(
    survey_id="survey_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">list_survey_questions</a>(...) -> ListSurveyQuestionsReportingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get reports for survey questions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.list_survey_questions(
    survey_id="survey_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">get_survey_question</a>(...) -> SurveyQuestionReport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get report for a survey question.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.get_survey_question(
    survey_id="survey_id",
    question_id="question_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**question_id:** `str` — The ID of the survey question.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">list_survey_question_answers</a>(...) -> ListSurveyQuestionAnswersReportingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get answers for a survey question.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.list_survey_question_answers(
    survey_id="survey_id",
    question_id="question_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**question_id:** `str` — The ID of the survey question.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**respondent_familiarity_is:** `typing.Optional[ListSurveyQuestionAnswersReportingRequestRespondentFamiliarityIs]` — Filter survey responses by familiarity of the respondents.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">list_survey_responses</a>(...) -> ListSurveyResponsesReportingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get responses to a survey.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.list_survey_responses(
    survey_id="survey_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**answered_question:** `typing.Optional[int]` — The ID of the question that was answered.
    
</dd>
</dl>

<dl>
<dd>

**chose_answer:** `typing.Optional[str]` — The ID of the option chosen to filter responses on.
    
</dd>
</dl>

<dl>
<dd>

**respondent_familiarity_is:** `typing.Optional[ListSurveyResponsesReportingRequestRespondentFamiliarityIs]` — Filter survey responses by familiarity of the respondents.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reporting.<a href="src/mailchimp_marketing/reporting/client.py">get_survey_respons</a>(...) -> GetSurveyResponsReportingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a single survey response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reporting.get_survey_respons(
    survey_id="survey_id",
    response_id="response_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**survey_id:** `str` — The ID of the survey.
    
</dd>
</dl>

<dl>
<dd>

**response_id:** `str` — The ID of the survey response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## reports
<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list</a>(...) -> ListReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get campaign reports.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListReportsRequestType]` — The campaign type.
    
</dd>
</dl>

<dl>
<dd>

**before_send_time:** `typing.Optional[datetime.datetime]` — Restrict the response to campaigns sent before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**since_send_time:** `typing.Optional[datetime.datetime]` — Restrict the response to campaigns sent after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">get</a>(...) -> CampaignReport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get report details for a specific sent campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.get(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_abuse_reports</a>(...) -> ListAbuseReportsReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of abuse complaints for a specific campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_abuse_reports(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">get_abuse_report</a>(...) -> AbuseComplaint</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific abuse report for a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.get_abuse_report(
    campaign_id="campaign_id",
    report_id="report_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**report_id:** `str` — The id for the abuse report.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_advice</a>(...) -> ListAdviceReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get feedback based on a campaign's statistics. Advice feedback is based on campaign stats like opens, clicks, unsubscribes, bounces, and more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_advice(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_click_details</a>(...) -> ListClickDetailsReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about clicks on specific links in your Mailchimp campaigns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_click_details(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListClickDetailsReportsRequestSortField]` — Returns click reports sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListClickDetailsReportsRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**filter_bots:** `typing.Optional[bool]` — When true, exclude automated bot clicks so the returned click counts reflect human clicks only, matching the in-app Recipient Activity view. Filtering changes a link's counts, but never removes a link from the response. Defaults to false (all clicks).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">get_click_detail</a>(...) -> ClickDetailReport</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get click details for a specific link in a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.get_click_detail(
    campaign_id="campaign_id",
    link_id="link_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `str` — The id for the link.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**filter_bots:** `typing.Optional[bool]` — When true, exclude automated bot clicks so the returned click counts reflect human clicks only, matching the in-app Recipient Activity view. Filtering changes a link's counts, but never removes a link from the response. Defaults to false (all clicks).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_click_detail_members</a>(...) -> ListClickDetailMembersReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about list members who clicked on a specific link in a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_click_detail_members(
    campaign_id="campaign_id",
    link_id="link_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `str` — The id for the link.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">get_click_detail_member</a>(...) -> ClickDetailMember</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific subscriber who clicked a link in a specific campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.get_click_detail_member(
    campaign_id="campaign_id",
    link_id="link_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**link_id:** `str` — The id for the link.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_domain_performance</a>(...) -> ListDomainPerformanceReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get statistics for the top-performing email domains in a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_domain_performance(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_ecommerce_product_activity</a>(...) -> ListEcommerceProductActivityReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get breakdown of product activity for a campaign
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_ecommerce_product_activity(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListEcommerceProductActivityReportsRequestSortField]` — Returns files sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_eepurl</a>(...) -> ListEepurlReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a summary of social activity for the campaign, tracked by EepURL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_eepurl(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_email_activity</a>(...) -> ListEmailActivityReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of member's subscriber activity in a specific campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_email_activity(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Restrict results to email activity events that occur after a specific time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**filter_bots:** `typing.Optional[bool]` — When true, exclude automated bot and Apple Mail Privacy Protection (MPP) proxy activity so the returned activity reflects human-only opens and clicks, matching the in-app Recipient Activity view. Filtering removes events from a member's activity, but never removes the member from the response. Defaults to false (all activity).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">get_email_activity</a>(...) -> EmailActivity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific list member's activity in a campaign including opens, clicks, and bounces.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.get_email_activity(
    campaign_id="campaign_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Restrict results to email activity events that occur after a specific time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**filter_bots:** `typing.Optional[bool]` — When true, exclude automated bot and Apple Mail Privacy Protection (MPP) proxy activity so the returned activity reflects human-only opens and clicks, matching the in-app Recipient Activity view. Filtering removes events from a member's activity, but never removes the member from the response. Defaults to false (all activity).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_locations</a>(...) -> ListLocationsReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get top open locations for a specific campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_locations(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_open_details</a>(...) -> ListOpenDetailsReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed information about any campaign emails that were opened by a list member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_open_details(
    campaign_id="campaign_id",
    since="2016-04-12 12:00:00",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[str]` — Restrict results to campaign open events that occur after a specific time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListOpenDetailsReportsRequestSortField]` — Returns open reports sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListOpenDetailsReportsRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**filter_bots:** `typing.Optional[bool]` — When true, exclude automated (proxy/bot) opens so the returned open counts reflect human opens only, matching the in-app Recipient Activity view. A member whose opens are all automated is excluded from the human-only view. Defaults to false (all opens).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">get_open_detail</a>(...) -> OpenActivity</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific subscriber who opened a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.get_open_detail(
    campaign_id="campaign_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**filter_bots:** `typing.Optional[bool]` — When true, exclude automated (proxy/bot) opens so the returned open counts reflect human opens only, matching the in-app Recipient Activity view. A member whose opens are all automated is excluded from the human-only view. Defaults to false (all opens).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_sent_to</a>(...) -> ListSentToReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about campaign recipients.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_sent_to(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">get_sent_to</a>(...) -> SentTo</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific campaign recipient.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.get_sent_to(
    campaign_id="campaign_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_sub_reports</a>(...) -> ListSubReportsReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of reports with child campaigns for a specific parent campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_sub_reports(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">list_unsubscribed</a>(...) -> ListUnsubscribedReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about members who have unsubscribed from a specific campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.list_unsubscribed(
    campaign_id="campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.reports.<a href="src/mailchimp_marketing/reports/client.py">get_unsubscribed</a>(...) -> Unsubscribes</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific list member who unsubscribed from a campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.reports.get_unsubscribed(
    campaign_id="campaign_id",
    subscriber_hash="subscriber_hash",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**campaign_id:** `str` — The unique id for the campaign.
    
</dd>
</dl>

<dl>
<dd>

**subscriber_hash:** `str` — The MD5 hash of the lowercase version of the list member's email address.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SearchCampaigns
<details><summary><code>client.search_campaigns.<a href="src/mailchimp_marketing/search_campaigns/client.py">list</a>(...) -> ListSearchCampaignsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search all campaigns for the specified query terms.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.search_campaigns.list(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — The search query used to filter results.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SmsCampaigns
<details><summary><code>client.sms_campaigns.<a href="src/mailchimp_marketing/sms_campaigns/client.py">list</a>(...) -> ListSmsCampaignsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all SMS campaigns in an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.sms_campaigns.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/mailchimp_marketing/sms_campaigns/client.py">create</a>(...) -> SmsCampaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new SMS campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.sms_campaigns.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the campaign.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `typing.Optional[int]` — The numeric ID of the list to send the campaign to.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — The ID of the folder to place this campaign in.
    
</dd>
</dl>

<dl>
<dd>

**segments:** `typing.Optional[typing.List[int]]` — The segment IDs to target for this campaign.
    
</dd>
</dl>

<dl>
<dd>

**excluded_segments:** `typing.Optional[typing.List[int]]` — The segment IDs to exclude from this campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/mailchimp_marketing/sms_campaigns/client.py">get</a>(...) -> SmsCampaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details for a single SMS campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.sms_campaigns.get(
    sms_campaign_id="sms_campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sms_campaign_id:** `str` — The unique id for the SMS campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/mailchimp_marketing/sms_campaigns/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a campaign from your Mailchimp account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.sms_campaigns.delete(
    sms_campaign_id="sms_campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sms_campaign_id:** `str` — The unique id for the SMS campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/mailchimp_marketing/sms_campaigns/client.py">update</a>(...) -> SmsCampaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an SMS campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.sms_campaigns.update(
    sms_campaign_id="sms_campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sms_campaign_id:** `str` — The unique id for the SMS campaign.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the campaign.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — The ID of the folder to place this campaign in.
    
</dd>
</dl>

<dl>
<dd>

**segments:** `typing.Optional[typing.List[int]]` — The segment IDs to target for this campaign.
    
</dd>
</dl>

<dl>
<dd>

**excluded_segments:** `typing.Optional[typing.List[int]]` — The segment IDs to exclude from this campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/mailchimp_marketing/sms_campaigns/client.py">create_action_cancel_send</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a scheduled or sending SMS campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.sms_campaigns.create_action_cancel_send(
    sms_campaign_id="sms_campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sms_campaign_id:** `str` — The unique id for the SMS campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/mailchimp_marketing/sms_campaigns/client.py">create_action_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Schedule an SMS campaign for delivery.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment
import datetime

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.sms_campaigns.create_action_schedule(
    sms_campaign_id="sms_campaign_id",
    schedule_time=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sms_campaign_id:** `str` — The unique id for the SMS campaign.
    
</dd>
</dl>

<dl>
<dd>

**schedule_time:** `datetime.datetime` — The UTC date and time to schedule the campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/mailchimp_marketing/sms_campaigns/client.py">create_action_send</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an SMS campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.sms_campaigns.create_action_send(
    sms_campaign_id="sms_campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sms_campaign_id:** `str` — The unique id for the SMS campaign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/mailchimp_marketing/sms_campaigns/client.py">get_content</a>(...) -> SmsCampaignContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the content for an SMS campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.sms_campaigns.get_content(
    sms_campaign_id="sms_campaign_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sms_campaign_id:** `str` — The unique id for the SMS campaign.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sms_campaigns.<a href="src/mailchimp_marketing/sms_campaigns/client.py">upsert_content</a>(...) -> SmsCampaignContent</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the content for an SMS campaign.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.sms_campaigns.upsert_content(
    sms_campaign_id="sms_campaign_id",
    message_body="message_body",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sms_campaign_id:** `str` — The unique id for the SMS campaign.
    
</dd>
</dl>

<dl>
<dd>

**message_body:** `str` — The SMS message body.
    
</dd>
</dl>

<dl>
<dd>

**media:** `typing.Optional[typing.List[UpsertContentSmsCampaignsRequestMediaItem]]` — Attached images or files. Limited to one item. Omitting this field or sending an empty array removes any existing media; to keep the current media while updating other fields, re-send the media array.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SearchMembers
<details><summary><code>client.search_members.<a href="src/mailchimp_marketing/search_members/client.py">list</a>(...) -> ListSearchMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search for list members. This search can be restricted to a specific list, or can be used to search across all lists in an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.search_members.list(
    query="query",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — The search query used to filter results. Query should be a valid email, or a string representing a contact's first or last name.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**list_id:** `typing.Optional[str]` — The unique id for the list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TemplateFolders
<details><summary><code>client.template_folders.<a href="src/mailchimp_marketing/template_folders/client.py">list</a>(...) -> ListTemplateFoldersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all folders used to organize templates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.template_folders.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.template_folders.<a href="src/mailchimp_marketing/template_folders/client.py">create</a>(...) -> CreateTemplateFoldersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new template folder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.template_folders.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.template_folders.<a href="src/mailchimp_marketing/template_folders/client.py">get</a>(...) -> GetTemplateFoldersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific folder used to organize templates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.template_folders.get(
    folder_id="folder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — The unique id for the template folder.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.template_folders.<a href="src/mailchimp_marketing/template_folders/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific template folder, and mark all the templates in the folder as 'unfiled'.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.template_folders.delete(
    folder_id="folder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — The unique id for the template folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.template_folders.<a href="src/mailchimp_marketing/template_folders/client.py">update</a>(...) -> UpdateTemplateFoldersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a specific folder used to organize templates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.template_folders.update(
    folder_id="folder_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**folder_id:** `str` — The unique id for the template folder.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## templates
<details><summary><code>client.templates.<a href="src/mailchimp_marketing/templates/client.py">list</a>(...) -> ListTemplatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of an account's available templates.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.templates.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — The number of records to return. Default value is 10. Maximum value is 1000
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Used for [pagination](https://mailchimp.com/developer/marketing/docs/methods-parameters/#pagination), this is the number of records from a collection to skip. Default value is 0.
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — The Mailchimp account user who created the template.
    
</dd>
</dl>

<dl>
<dd>

**since_date_created:** `typing.Optional[str]` — Restrict the response to templates created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**before_date_created:** `typing.Optional[str]` — Restrict the response to templates created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Limit results based on template type.
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Limit results based on category.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — The unique folder id.
    
</dd>
</dl>

<dl>
<dd>

**sort_field:** `typing.Optional[ListTemplatesRequestSortField]` — Returns user templates sorted by the specified field.
    
</dd>
</dl>

<dl>
<dd>

**content_type:** `typing.Optional[ListTemplatesRequestContentType]` — Limit results based on how the template's content is put together. Only templates of type `user` can be filtered by `content_type`. If you want to retrieve saved templates created with the legacy email editor, then filter `content_type` to `template`. If you'd rather pull your saved templates for the new editor, filter to `multichannel`. For code your own templates, filter to `html`.
    
</dd>
</dl>

<dl>
<dd>

**sort_dir:** `typing.Optional[ListTemplatesRequestSortDir]` — Determines the order direction for sorted results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.templates.<a href="src/mailchimp_marketing/templates/client.py">create</a>(...) -> TemplateInstance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new template for the account. Only Classic templates are supported.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.templates.create(
    html="html",
    name="Freddie\'s Jokes",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**html:** `str` — The raw HTML for the template. We  support the Mailchimp [Template Language](https://mailchimp.com/help/getting-started-with-mailchimps-template-language/) in any HTML code passed via the API.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the template.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — The id of the folder the template is currently in.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.templates.<a href="src/mailchimp_marketing/templates/client.py">get</a>(...) -> TemplateInstance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.templates.get(
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` — The unique id for the template.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.templates.<a href="src/mailchimp_marketing/templates/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.templates.delete(
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` — The unique id for the template.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.templates.<a href="src/mailchimp_marketing/templates/client.py">update</a>(...) -> TemplateInstance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name, HTML, or `folder_id` of an existing template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.templates.update(
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` — The unique id for the template.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — The id of the folder the template is currently in.
    
</dd>
</dl>

<dl>
<dd>

**html:** `typing.Optional[str]` — The raw HTML for the template. We  support the Mailchimp [Template Language](https://mailchimp.com/help/getting-started-with-mailchimps-template-language/) in any HTML code passed via the API.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the template.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.templates.<a href="src/mailchimp_marketing/templates/client.py">list_default_content</a>(...) -> ListDefaultContentTemplatesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the sections that you can edit in a template, including each section's default content.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.templates.list_default_content(
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` — The unique id for the template.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**exclude_fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## VerifiedDomains
<details><summary><code>client.verified_domains.<a href="src/mailchimp_marketing/verified_domains/client.py">list</a>() -> ListVerifiedDomainsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all of the sending domains on the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.verified_domains.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verified_domains.<a href="src/mailchimp_marketing/verified_domains/client.py">create</a>(...) -> CreateVerifiedDomainsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a domain to the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.verified_domains.create(
    verification_email="verification_email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**verification_email:** `str` — The e-mail address at the domain you want to verify. This will receive a two-factor challenge to be used in the verify action.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verified_domains.<a href="src/mailchimp_marketing/verified_domains/client.py">get</a>(...) -> GetVerifiedDomainsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the details for a single domain on the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.verified_domains.get(
    domain_name="domain_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_name:** `str` — The domain name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verified_domains.<a href="src/mailchimp_marketing/verified_domains/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a verified domain from the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.verified_domains.delete(
    domain_name="domain_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_name:** `str` — The domain name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.verified_domains.<a href="src/mailchimp_marketing/verified_domains/client.py">create_action_verify</a>(...) -> CreateActionVerifyVerifiedDomainsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify a domain for sending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mailchimp_marketing import MailchimpClient
from mailchimp_marketing.environment import MailchimpClientEnvironment

client = MailchimpClient(
    token="<token>",
    environment=MailchimpClientEnvironment.DEFAULT,
)

client.verified_domains.create_action_verify(
    domain_name="domain_name",
    code="code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_name:** `str` — The domain name.
    
</dd>
</dl>

<dl>
<dd>

**code:** `str` — The code that was sent to the email address provided when adding a new domain to verify.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

