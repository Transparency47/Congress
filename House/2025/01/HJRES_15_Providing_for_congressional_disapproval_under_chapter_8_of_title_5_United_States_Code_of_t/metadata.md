# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/15?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/15
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to "Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment".
- Congress: 119
- Bill type: HJRES
- Bill number: 15
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-02-27T23:41:17Z
- Update date including text: 2026-02-27T23:41:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/15",
    "number": "15",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001233",
        "district": "8",
        "firstName": "Mark",
        "fullName": "Rep. Messmer, Mark [R-IN-8]",
        "lastName": "Messmer",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment\".",
    "type": "HJRES",
    "updateDate": "2026-02-27T23:41:17Z",
    "updateDateIncludingText": "2026-02-27T23:41:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:32:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres15ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 15\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Messmer submitted the following joint resolution; which was referred to the Committee on Energy and Commerce\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment .\nThat Congress disapproves the final rule submitted by the Department of Energy relating to Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment (88 Fed. Reg. 69686 (October 6, 2023)), and such rule shall have no force or effect.",
      "versionDate": "2025-01-09",
      "versionType": "IH"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-01-22T16:28:17Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-01-22T16:28:27Z"
          },
          {
            "name": "Department of Energy",
            "updateDate": "2025-01-22T16:29:09Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2025-01-22T16:38:30Z"
          },
          {
            "name": "Lighting, heating, cooling",
            "updateDate": "2025-01-22T16:38:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-01-10T13:20:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hjres15",
          "measure-number": "15",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-01-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres15v00",
            "update-date": "2025-01-13"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the final rule titled <em>Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment</em>, which was submitted by the Department of Energy on October 6, 2023. The rule adopts more stringent energy conservation standards for commercial water heating equipment under the Energy Policy and Conservation Act in order to achieve more energy savings.</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres15.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule titled <em>Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment</em>, which was submitted by the Department of Energy on October 6, 2023. The rule adopts more stringent energy conservation standards for commercial water heating equipment under the Energy Policy and Conservation Act in order to achieve more energy savings.</p>",
      "updateDate": "2025-01-13",
      "versionCode": "id119hjres15"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the final rule titled <em>Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment</em>, which was submitted by the Department of Energy on October 6, 2023. The rule adopts more stringent energy conservation standards for commercial water heating equipment under the Energy Policy and Conservation Act in order to achieve more energy savings.</p>",
      "updateDate": "2025-01-13",
      "versionCode": "id119hjres15"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres15ih.xml"
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
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-10T09:18:16Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Commercial Water Heating Equipment\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:05:57Z"
    }
  ]
}
```
