# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/26?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/26
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to "Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles-Phase 3".
- Congress: 119
- Bill type: HJRES
- Bill number: 26
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2026-02-11T22:06:16Z
- Update date including text: 2026-02-11T22:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/26",
    "number": "26",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "F000469",
        "district": "1",
        "firstName": "Russ",
        "fullName": "Rep. Fulcher, Russ [R-ID-1]",
        "lastName": "Fulcher",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles-Phase 3\".",
    "type": "HJRES",
    "updateDate": "2026-02-11T22:06:16Z",
    "updateDateIncludingText": "2026-02-11T22:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:01:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres26ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 26\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Fulcher submitted the following joint resolution; which was referred to the Committee on Energy and Commerce\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles\u2014Phase 3 .\nThat Congress disapproves the rule submitted by the Environmental Protection Agency relating to Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles\u2014Phase 3 (89 Fed. Reg. 29440 (April 22, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-01-22",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-01-27T17:26:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hjres26",
          "measure-number": "26",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres26v00",
            "update-date": "2025-03-04"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution nullifies the Environmental Protection Agency (EPA) rule titled <em>Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles\u2014Phase 3</em> and published on April 22, 2024. Heavy-duty vehicles\u00a0generally include vocational vehicles (such as public utility trucks and school buses) and tractors (such as cabs on tractor-trailer trucks).</p><p>Among other requirements, the rule phases in standards to reduce greenhouse gas emissions from certain heavy-duty vehicles. The phased-in standards replace previous standards that were established under the EPA's <em>Greenhouse Gas Emissions and Fuel Efficiency Standards for Medium- and Heavy-Duty Engines and Vehicles\u2014Phase 2</em> rule with more stringent standards.</p>"
        },
        "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles-Phase 3\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres26.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency (EPA) rule titled <em>Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles\u2014Phase 3</em> and published on April 22, 2024. Heavy-duty vehicles\u00a0generally include vocational vehicles (such as public utility trucks and school buses) and tractors (such as cabs on tractor-trailer trucks).</p><p>Among other requirements, the rule phases in standards to reduce greenhouse gas emissions from certain heavy-duty vehicles. The phased-in standards replace previous standards that were established under the EPA's <em>Greenhouse Gas Emissions and Fuel Efficiency Standards for Medium- and Heavy-Duty Engines and Vehicles\u2014Phase 2</em> rule with more stringent standards.</p>",
      "updateDate": "2025-03-04",
      "versionCode": "id119hjres26"
    },
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles-Phase 3\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution nullifies the Environmental Protection Agency (EPA) rule titled <em>Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles\u2014Phase 3</em> and published on April 22, 2024. Heavy-duty vehicles\u00a0generally include vocational vehicles (such as public utility trucks and school buses) and tractors (such as cabs on tractor-trailer trucks).</p><p>Among other requirements, the rule phases in standards to reduce greenhouse gas emissions from certain heavy-duty vehicles. The phased-in standards replace previous standards that were established under the EPA's <em>Greenhouse Gas Emissions and Fuel Efficiency Standards for Medium- and Heavy-Duty Engines and Vehicles\u2014Phase 2</em> rule with more stringent standards.</p>",
      "updateDate": "2025-03-04",
      "versionCode": "id119hjres26"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres26ih.xml"
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
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles-Phase 3\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-23T09:18:20Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles-Phase 3\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-23T09:05:39Z"
    }
  ]
}
```
