# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/124?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/124
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to "National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision".
- Congress: 119
- Bill type: HJRES
- Bill number: 124
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-12-09T13:39:07Z
- Update date including text: 2025-12-09T13:39:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/124",
    "number": "124",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001323",
        "district": "",
        "firstName": "Nicholas",
        "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
        "lastName": "Begich",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to \"National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision\".",
    "type": "HJRES",
    "updateDate": "2025-12-09T13:39:07Z",
    "updateDateIncludingText": "2025-12-09T13:39:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:06:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres124ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 124\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Begich submitted the following joint resolution; which was referred to the Committee on Natural Resources\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision .\nThat Congress disapproves the rule submitted by the Bureau of Land Management relating to National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision (issued April 25, 2022, as a record of decision, and a letter of opinion from the Government Accountability Office dated July 24, 2025, printed in the Congressional Record on July 28, 2025, on pages S4768\u2013S4770, concluding that such record of decision is a rule under the Congressional Review Act), and such rule shall have no force or effect.",
      "versionDate": "2025-09-18",
      "versionType": "IH"
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
        "actionDate": "2025-12-05",
        "text": "Became Public Law No: 119-47."
      },
      "number": "80",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to \"National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision\".",
      "type": "SJRES"
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
        "updateDate": "2025-09-24T13:32:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-18",
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
          "measure-id": "id119hjres124",
          "measure-number": "124",
          "measure-type": "hjres",
          "orig-publish-date": "2025-09-18",
          "originChamber": "HOUSE",
          "update-date": "2025-11-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres124v00",
            "update-date": "2025-11-18"
          },
          "action-date": "2025-09-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the rule submitted by the Bureau of Land Management (BLM) titled <em>National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision\u00a0</em>and issued on April 25, 2022. BLM's plan provides for the management of the National Petroleum Reserve in Alaska, which is an approximately 23-million-acre area on Alaska\u2019s North Slope. The\u00a02022 plan replaced the 2020 plan and closed approximately 48% of the reserve to oil and gas leasing\u00a0in order to protect certain surface resources and uses, such as protecting wildlife and providing subsistence\u00a0for communities. Thus, the joint resolution removes the protections provided under the 2022 plan and reverts to the 2020 plan.</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to \"National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres124.xml",
    "summary": {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the rule submitted by the Bureau of Land Management (BLM) titled <em>National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision\u00a0</em>and issued on April 25, 2022. BLM's plan provides for the management of the National Petroleum Reserve in Alaska, which is an approximately 23-million-acre area on Alaska\u2019s North Slope. The\u00a02022 plan replaced the 2020 plan and closed approximately 48% of the reserve to oil and gas leasing\u00a0in order to protect certain surface resources and uses, such as protecting wildlife and providing subsistence\u00a0for communities. Thus, the joint resolution removes the protections provided under the 2022 plan and reverts to the 2020 plan.</p>",
      "updateDate": "2025-11-18",
      "versionCode": "id119hjres124"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to \"National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision\"."
  },
  "summaries": [
    {
      "actionDate": "2025-09-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the rule submitted by the Bureau of Land Management (BLM) titled <em>National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision\u00a0</em>and issued on April 25, 2022. BLM's plan provides for the management of the National Petroleum Reserve in Alaska, which is an approximately 23-million-acre area on Alaska\u2019s North Slope. The\u00a02022 plan replaced the 2020 plan and closed approximately 48% of the reserve to oil and gas leasing\u00a0in order to protect certain surface resources and uses, such as protecting wildlife and providing subsistence\u00a0for communities. Thus, the joint resolution removes the protections provided under the 2022 plan and reverts to the 2020 plan.</p>",
      "updateDate": "2025-11-18",
      "versionCode": "id119hjres124"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres124ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to \"National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T08:18:19Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Land Management relating to \"National Petroleum Reserve in Alaska Integrated Activity Plan Record of Decision\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T08:07:53Z"
    }
  ]
}
```
