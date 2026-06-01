# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/50?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/50
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to "Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment".
- Congress: 119
- Bill type: SJRES
- Bill number: 50
- Origin chamber: Senate
- Introduced date: 2025-04-28
- Update date: 2026-04-15T18:27:28Z
- Update date including text: 2026-04-15T18:27:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-28: Introduced in Senate
- 2025-04-28 - IntroReferral: Introduced in Senate
- 2025-04-28 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-04-28: Introduced in Senate

## Actions

- 2025-04-28 - IntroReferral: Introduced in Senate
- 2025-04-28 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/50",
    "number": "50",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment\".",
    "type": "SJRES",
    "updateDate": "2026-04-15T18:27:28Z",
    "updateDateIncludingText": "2026-04-15T18:27:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-04-28T21:00:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres50is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 50\nIN THE SENATE OF THE UNITED STATES\nApril 28, 2025 Mr. Husted introduced the following joint resolution; which was read twice and referred to the Committee on Energy and Natural Resources\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment .\nThat Congress disapproves the rule submitted by the Department of Energy relating to Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment (89 Fed. Reg. 81994 (October 9, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-04-28",
      "versionType": "IS"
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
        "actionDate": "2025-05-09",
        "text": "Became Public Law No: 119-8."
      },
      "number": "42",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment\".",
      "type": "HJRES"
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
        "name": "Energy",
        "updateDate": "2025-05-09T12:13:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-28",
    "originChamber": "Senate",
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
          "measure-id": "id119sjres50",
          "measure-number": "50",
          "measure-type": "sjres",
          "orig-publish-date": "2025-04-28",
          "originChamber": "SENATE",
          "update-date": "2026-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres50v00",
            "update-date": "2026-04-15"
          },
          "action-date": "2025-04-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution nullifies the\u00a0<em>Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment\u00a0</em>rule published by the Department of Energy (DOE) on October 9, 2024. Under the rule, DOE modified its regulations on the energy efficiency of certain types of\u00a0consumer products (e.g., washing machines and dishwashers) and\u00a0industrial equipment (e.g., computer room air conditioners). Specifically, it modified certification requirements, labeling requirements, and enforcement provisions for these products and equipment to (1) align reporting requirements with currently applicable energy conservation standards and test procedures, and (2) provide DOE with the information necessary to determine the appropriate classification of products for the application of standards.\u00a0</p>"
        },
        "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres50.xml",
    "summary": {
      "actionDate": "2025-04-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the\u00a0<em>Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment\u00a0</em>rule published by the Department of Energy (DOE) on October 9, 2024. Under the rule, DOE modified its regulations on the energy efficiency of certain types of\u00a0consumer products (e.g., washing machines and dishwashers) and\u00a0industrial equipment (e.g., computer room air conditioners). Specifically, it modified certification requirements, labeling requirements, and enforcement provisions for these products and equipment to (1) align reporting requirements with currently applicable energy conservation standards and test procedures, and (2) provide DOE with the information necessary to determine the appropriate classification of products for the application of standards.\u00a0</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119sjres50"
    },
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment\"."
  },
  "summaries": [
    {
      "actionDate": "2025-04-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the\u00a0<em>Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment\u00a0</em>rule published by the Department of Energy (DOE) on October 9, 2024. Under the rule, DOE modified its regulations on the energy efficiency of certain types of\u00a0consumer products (e.g., washing machines and dishwashers) and\u00a0industrial equipment (e.g., computer room air conditioners). Specifically, it modified certification requirements, labeling requirements, and enforcement provisions for these products and equipment to (1) align reporting requirements with currently applicable energy conservation standards and test procedures, and (2) provide DOE with the information necessary to determine the appropriate classification of products for the application of standards.\u00a0</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119sjres50"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres50is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-01T02:18:27Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program for Appliance Standards: Certification Requirements, Labeling Requirements, and Enforcement Provisions for Certain Consumer Products and Commercial Equipment\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T10:56:19Z"
    }
  ]
}
```
