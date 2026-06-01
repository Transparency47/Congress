# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2874?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2874
- Title: Defense of Conscience in Health Care Act
- Congress: 119
- Bill type: HR
- Bill number: 2874
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-04-13T15:09:03Z
- Update date including text: 2026-04-13T15:09:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2874",
    "number": "2874",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Defense of Conscience in Health Care Act",
    "type": "HR",
    "updateDate": "2026-04-13T15:09:03Z",
    "updateDateIncludingText": "2026-04-13T15:09:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-04-10T13:10:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2874ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2874\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Moolenaar introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide for regulations on protecting statutory conscience rights in health care.\n#### 1. Short title\nThis Act may be cited as the Defense of Conscience in Health Care Act .\n#### 2. Regulations on protecting statutory conscience rights in health care\n##### (a) In general\nNot later than 6 months after the date of enactment of this Act, the Secretary of Health and Human Services shall\u2014\n**(1)**\nissue, under the Federal conscience and anti-discrimination laws, a final rule that is identical or materially equivalent to the former rule stated in part 88 of title 45, Code of Federal Regulations, as in effect on July 22, 2019 (84 Fed. Reg. 23170; relating to protecting statutory conscience rights in health care; delegations of authority); and\n**(2)**\nspecify in the final rule that the rule supersedes any contrary rule in existence on the date of issuance.\n##### (b) Definition\nIn this section, the term Federal conscience and anti-discrimination laws has the meaning given the term in the former rule specified in subsection (a)(1).",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-09",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "47",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Defense of Conscience in Health Care Act",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-19T14:47:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr2874",
          "measure-number": "2874",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2874v00",
            "update-date": "2026-04-13"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Defense of Conscience in Health Care Act</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to issue a final rule on protecting statutory conscience rights in health care that is identical or equivalent to the rule titled<em>\u00a0</em><em>Protecting Statutory Conscience\u00a0Rights in Health Care; Delegations of\u00a0Authority</em>, <em></em>which was scheduled to take effect on July 22, 2019, but was vacated by courts. </p><p>Federal law\u00a0generally prohibits discrimination based on conscience or religious beliefs with respect to federally funded health care programs, including prohibiting recipients of certain federal funding from requiring health care providers\u00a0to take\u00a0actions that they find religiously or morally objectionable (e.g., providing\u00a0referrals for abortions).\u00a0</p><p>In 2019,\u00a0HHS issued a final rule revising the\u00a0applicable\u00a0regulations, including imposing certification and cooperation requirements, as well as establishing additional enforcement provisions and penalties. However, this rule was later\u00a0vacated by federal courts and never took effect. In 2024,\u00a0HHS issued another final rule that generally applied\u00a0a pre-2019 enforcement framework while also maintaining certain aspects of the 2019 rule (e.g., specifically designating HHS' Office for Civil Rights as the entity with the authority to handle relevant complaints).</p><p>The bill requires HHS to reinstate\u00a0the 2019 rule in its entirety. <br/></p>"
        },
        "title": "Defense of Conscience in Health Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2874.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defense of Conscience in Health Care Act</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to issue a final rule on protecting statutory conscience rights in health care that is identical or equivalent to the rule titled<em>\u00a0</em><em>Protecting Statutory Conscience\u00a0Rights in Health Care; Delegations of\u00a0Authority</em>, <em></em>which was scheduled to take effect on July 22, 2019, but was vacated by courts. </p><p>Federal law\u00a0generally prohibits discrimination based on conscience or religious beliefs with respect to federally funded health care programs, including prohibiting recipients of certain federal funding from requiring health care providers\u00a0to take\u00a0actions that they find religiously or morally objectionable (e.g., providing\u00a0referrals for abortions).\u00a0</p><p>In 2019,\u00a0HHS issued a final rule revising the\u00a0applicable\u00a0regulations, including imposing certification and cooperation requirements, as well as establishing additional enforcement provisions and penalties. However, this rule was later\u00a0vacated by federal courts and never took effect. In 2024,\u00a0HHS issued another final rule that generally applied\u00a0a pre-2019 enforcement framework while also maintaining certain aspects of the 2019 rule (e.g., specifically designating HHS' Office for Civil Rights as the entity with the authority to handle relevant complaints).</p><p>The bill requires HHS to reinstate\u00a0the 2019 rule in its entirety. <br/></p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119hr2874"
    },
    "title": "Defense of Conscience in Health Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defense of Conscience in Health Care Act</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to issue a final rule on protecting statutory conscience rights in health care that is identical or equivalent to the rule titled<em>\u00a0</em><em>Protecting Statutory Conscience\u00a0Rights in Health Care; Delegations of\u00a0Authority</em>, <em></em>which was scheduled to take effect on July 22, 2019, but was vacated by courts. </p><p>Federal law\u00a0generally prohibits discrimination based on conscience or religious beliefs with respect to federally funded health care programs, including prohibiting recipients of certain federal funding from requiring health care providers\u00a0to take\u00a0actions that they find religiously or morally objectionable (e.g., providing\u00a0referrals for abortions).\u00a0</p><p>In 2019,\u00a0HHS issued a final rule revising the\u00a0applicable\u00a0regulations, including imposing certification and cooperation requirements, as well as establishing additional enforcement provisions and penalties. However, this rule was later\u00a0vacated by federal courts and never took effect. In 2024,\u00a0HHS issued another final rule that generally applied\u00a0a pre-2019 enforcement framework while also maintaining certain aspects of the 2019 rule (e.g., specifically designating HHS' Office for Civil Rights as the entity with the authority to handle relevant complaints).</p><p>The bill requires HHS to reinstate\u00a0the 2019 rule in its entirety. <br/></p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119hr2874"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2874ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Defense of Conscience in Health Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defense of Conscience in Health Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for regulations on protecting statutory conscience rights in health care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T04:18:19Z"
    }
  ]
}
```
