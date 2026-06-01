# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/43?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/43
- Title: A resolution affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.
- Congress: 119
- Bill type: SRES
- Bill number: 43
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-12-05T22:50:56Z
- Update date including text: 2025-12-05T22:50:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S485-486)
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S485-486)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/43",
    "number": "43",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "A resolution affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.",
    "type": "SRES",
    "updateDate": "2025-12-05T22:50:56Z",
    "updateDateIncludingText": "2025-12-05T22:50:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S485-486)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T20:31:56Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "PA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres43is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 43\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Graham (for himself, Mr. Fetterman , and Mrs. Britt ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nAffirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.\nThat the Senate\u2014\n**(1)**\naffirms that the Islamic Republic of Iran\u2019s continued pursuit of a nuclear weapons capability is\u2014\n**(A)**\na credible threat to the United States; and\n**(B)**\nan existential threat to Israel and other allies and partners in the Middle East;\n**(2)**\nasserts all options should be considered to address the nuclear threat the Islamic Republic of Iran poses to the United States, Israel, and our allies and partners;\n**(3)**\ndemands the Islamic Republic of Iran to immediately cease engaging in any and all activities that threaten the national security interests of the United States, Israel, and our allies and partners, including\u2014\n**(A)**\nenriching uranium;\n**(B)**\ndeveloping or possessing delivery vehicles capable of carrying nuclear warheads; and\n**(C)**\ndeveloping or possessing a nuclear warhead.\n#### 1. Rule of construction\nNothing in this resolution may be construed to authorize the use of military force or the introduction of United States Armed Forces into hostilities.",
      "versionDate": "2025-01-29",
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
        "actionDate": "2025-02-04",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "105",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.",
      "type": "HRES"
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
        "updateDate": "2025-02-21T13:02:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119sres43",
          "measure-number": "43",
          "measure-type": "sres",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres43v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution affirms that Iran's pursuit of nuclear weapons is a credible threat to the United States and an existential threat to Israel and other allies and partners in the Middle East.\u00a0</p><p>The resolution also (1) demands that Iran cease engaging in activities such as enriching uranium and developing a nuclear warhead, and (2) asserts that all options should be considered to address the nuclear threat posed by Iran.</p>"
        },
        "title": "A resolution affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres43.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution affirms that Iran's pursuit of nuclear weapons is a credible threat to the United States and an existential threat to Israel and other allies and partners in the Middle East.\u00a0</p><p>The resolution also (1) demands that Iran cease engaging in activities such as enriching uranium and developing a nuclear warhead, and (2) asserts that all options should be considered to address the nuclear threat posed by Iran.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119sres43"
    },
    "title": "A resolution affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran."
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution affirms that Iran's pursuit of nuclear weapons is a credible threat to the United States and an existential threat to Israel and other allies and partners in the Middle East.\u00a0</p><p>The resolution also (1) demands that Iran cease engaging in activities such as enriching uranium and developing a nuclear warhead, and (2) asserts that all options should be considered to address the nuclear threat posed by Iran.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119sres43"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres43is.xml"
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
      "title": "A resolution affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T04:48:32Z"
    },
    {
      "title": "A resolution affirming the threats to world stability from a nuclear weapons-capable Islamic Republic of Iran.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T11:56:22Z"
    }
  ]
}
```
