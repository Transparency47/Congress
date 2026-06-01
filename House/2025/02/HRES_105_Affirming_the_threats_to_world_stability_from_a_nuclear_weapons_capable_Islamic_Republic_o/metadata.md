# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/105?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/105
- Title: Affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.
- Congress: 119
- Bill type: HRES
- Bill number: 105
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-12-12T21:23:53Z
- Update date including text: 2025-12-12T21:23:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-02-04 - Committee: Submitted in House
- Latest action: 2025-02-04: Submitted in House

## Actions

- 2025-02-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-02-04 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/105",
    "number": "105",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.",
    "type": "HRES",
    "updateDate": "2025-12-12T21:23:53Z",
    "updateDateIncludingText": "2025-12-12T21:23:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-04T17:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "PA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres105ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 105\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Moskowitz (for himself and Mr. Lawler ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nAffirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.\nThat the House of Representatives\u2014\n**(1)**\naffirms that the Islamic Republic of Iran\u2019s continued pursuit of a nuclear weapons capability is\u2014\n**(A)**\na credible threat to the United States; and\n**(B)**\nan existential threat to Israel and other allies and partners in the Middle East;\n**(2)**\nasserts all options should be considered to address the nuclear threat the Islamic Republic of Iran poses to the United States, Israel, and our allies and partners; and\n**(3)**\ndemands the Islamic Republic of Iran to immediately cease engaging in any and all activities that threaten the national security interests of the United States, Israel, and our allies and partners, including\u2014\n**(A)**\nenriching uranium;\n**(B)**\ndeveloping or possessing delivery vehicles capable of carrying nuclear warheads; and\n**(C)**\ndeveloping or possessing a nuclear warhead.\n#### 1. Rule of construction\nNothing in this resolution may be construed to authorize the use of military force or the introduction of United States Armed Forces into hostilities.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-01-29",
        "text": "Referred to the Committee on Foreign Relations. (text: CR S485-486)"
      },
      "number": "43",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-27",
        "text": "Referred to the Committee on Foreign Relations. (text: CR S1431-1433)"
      },
      "number": "101",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.",
      "type": "SRES"
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
        "name": "International Affairs",
        "updateDate": "2025-02-21T13:07:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hres105",
          "measure-number": "105",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres105v00",
            "update-date": "2025-04-03"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution affirms that Iran's pursuit of nuclear weapons is a credible threat to the United States and an existential threat to Israel and other allies and partners in the Middle East.\u00a0</p><p>The resolution also (1) demands that Iran cease engaging in activities such as enriching uranium and developing a nuclear warhead, and (2) asserts that all options should be considered to address the nuclear threat posed by Iran.</p>"
        },
        "title": "Affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres105.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution affirms that Iran's pursuit of nuclear weapons is a credible threat to the United States and an existential threat to Israel and other allies and partners in the Middle East.\u00a0</p><p>The resolution also (1) demands that Iran cease engaging in activities such as enriching uranium and developing a nuclear warhead, and (2) asserts that all options should be considered to address the nuclear threat posed by Iran.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hres105"
    },
    "title": "Affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran."
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution affirms that Iran's pursuit of nuclear weapons is a credible threat to the United States and an existential threat to Israel and other allies and partners in the Middle East.\u00a0</p><p>The resolution also (1) demands that Iran cease engaging in activities such as enriching uranium and developing a nuclear warhead, and (2) asserts that all options should be considered to address the nuclear threat posed by Iran.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hres105"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres105ih.xml"
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
      "title": "Affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T12:03:25Z"
    },
    {
      "title": "Affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T09:05:52Z"
    }
  ]
}
```
