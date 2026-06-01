# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/536?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/536
- Title: Fair SHARE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 536
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2025-12-05T22:50:23Z
- Update date including text: 2025-12-05T22:50:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/536",
    "number": "536",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Fair SHARE Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:50:23Z",
    "updateDateIncludingText": "2025-12-05T22:50:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T17:29:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NE"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s536is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 536\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mrs. Fischer (for herself, Mr. Ricketts , and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a tax on the sale of electric vehicles and batteries.\n#### 1. Short title\nThis Act may be cited as the Fair Sharing of Highways and Roads for Electric Vehicles Act of 2025 or the Fair SHARE Act of 2025 .\n#### 2. Tax on sale of electric vehicles and batteries\n##### (a) Imposition of tax\n**(1) In general**\nSubchapter A of chapter 32 of the Internal Revenue Code of 1986 is amended by adding at the end the following new part:\nIV Electric Vehicles and Batteries Sec. 4091. Tax on Electric Vehicles and Batteries. 4091. Tax on Electric Vehicles and batteries (a) Battery module There is hereby imposed a tax equal to $550 on each battery module with a weight of greater than 1,000 pounds which is\u2014 (1) sold by the manufacturer, producer, or importer thereof, and (2) intended for use in an electric vehicle. (b) Electric vehicles There is hereby imposed a tax equal to $1,000 on each electric vehicle sold by the manufacturer, producer, or importer thereof. (c) Definitions In this section\u2014 (1) Battery module The term battery module has the same meaning given such term in section 45X(c)(5)(B)(iii). (2) Electric vehicle (A) In general The term electric vehicle means a light-duty vehicle which satisfies the requirements under section 30D(d)(1)(F). (B) Exception for hybrid vehicles The term electric vehicle shall not include any motor vehicle which draws propulsion energy from onboard sources of stored energy which are both\u2014 (i) an internal combustion or heat engine using consumable fuel, and (ii) a rechargeable energy storage system. (3) Light-duty vehicle The term light-duty vehicle means a motor vehicle, as defined in section 30D(d)(2), which has a gross vehicle weight rating of less than 8,500 pounds. .\n**(2) Clerical amendment**\nThe table of parts for subchapter A of chapter 32 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nPART IV\u2014ELECTRIC VEHICLES AND BATTERIES .\n##### (b) Transfer of revenue to Highway Trust Fund\nSection 9503(b)(1) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subparagraph (D), by striking and at the end,\n**(2)**\nby redesignating subparagraph (E) as subparagraph (F), and\n**(3)**\nby inserting after subparagraph (D) the following new subparagraph:\n(E) section 4091 (relating to tax on electric vehicles and batteries), and .\n##### (c) Effective date\nThe amendments made by this section shall apply to sales after December 31, 2025.",
      "versionDate": "2025-02-12",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-12",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1253",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fair SHARE Act of 2025",
      "type": "HR"
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
        "name": "Taxation",
        "updateDate": "2025-05-06T17:46:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119s536",
          "measure-number": "536",
          "measure-type": "s",
          "orig-publish-date": "2025-02-12",
          "originChamber": "SENATE",
          "update-date": "2025-09-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s536v00",
            "update-date": "2025-09-24"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fair Sharing of Highways and Roads for Electric Vehicles\u00a0Act of 2025</strong></p><p>This bill imposes a new excise tax in the amount of $1,000 on the sale of an electric vehicle and a new excise tax in the amount of $550 on the sale of a battery module weighing over 1,000 pounds for use in an electric vehicle. The bill also requires the Department of the Treasury to transfer amounts collected from the new excise taxes to the Highway Trust Fund. (The Highway Trust Fund, which supports surface transportation programs and projects, is funded by transportation-related\u00a0excise\u00a0taxes.)</p><p>The bill defines <em>electric vehicle</em> as a light-duty vehicle (a motor vehicle weighing less than 8,500 pounds that is manufactured for use on public roads) that is powered by a battery with a capacity of at least seven kilowatt hours and is recharged through an external source of electricity. Under the bill, the excise tax\u00a0does not apply to hybrid vehicles, which are powered by a combination of fuel and a rechargeable energy storage system.</p><p>The bill defines <em>battery module</em> as a module with\u00a0two or more battery cells configured to create voltage or current (or no battery cells) and with an aggregate capacity of at least seven kilowatt hours (or one kilowatt hour for a hydrogen fuel cell vehicle).\u00a0</p>"
        },
        "title": "Fair SHARE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s536.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fair Sharing of Highways and Roads for Electric Vehicles\u00a0Act of 2025</strong></p><p>This bill imposes a new excise tax in the amount of $1,000 on the sale of an electric vehicle and a new excise tax in the amount of $550 on the sale of a battery module weighing over 1,000 pounds for use in an electric vehicle. The bill also requires the Department of the Treasury to transfer amounts collected from the new excise taxes to the Highway Trust Fund. (The Highway Trust Fund, which supports surface transportation programs and projects, is funded by transportation-related\u00a0excise\u00a0taxes.)</p><p>The bill defines <em>electric vehicle</em> as a light-duty vehicle (a motor vehicle weighing less than 8,500 pounds that is manufactured for use on public roads) that is powered by a battery with a capacity of at least seven kilowatt hours and is recharged through an external source of electricity. Under the bill, the excise tax\u00a0does not apply to hybrid vehicles, which are powered by a combination of fuel and a rechargeable energy storage system.</p><p>The bill defines <em>battery module</em> as a module with\u00a0two or more battery cells configured to create voltage or current (or no battery cells) and with an aggregate capacity of at least seven kilowatt hours (or one kilowatt hour for a hydrogen fuel cell vehicle).\u00a0</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119s536"
    },
    "title": "Fair SHARE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fair Sharing of Highways and Roads for Electric Vehicles\u00a0Act of 2025</strong></p><p>This bill imposes a new excise tax in the amount of $1,000 on the sale of an electric vehicle and a new excise tax in the amount of $550 on the sale of a battery module weighing over 1,000 pounds for use in an electric vehicle. The bill also requires the Department of the Treasury to transfer amounts collected from the new excise taxes to the Highway Trust Fund. (The Highway Trust Fund, which supports surface transportation programs and projects, is funded by transportation-related\u00a0excise\u00a0taxes.)</p><p>The bill defines <em>electric vehicle</em> as a light-duty vehicle (a motor vehicle weighing less than 8,500 pounds that is manufactured for use on public roads) that is powered by a battery with a capacity of at least seven kilowatt hours and is recharged through an external source of electricity. Under the bill, the excise tax\u00a0does not apply to hybrid vehicles, which are powered by a combination of fuel and a rechargeable energy storage system.</p><p>The bill defines <em>battery module</em> as a module with\u00a0two or more battery cells configured to create voltage or current (or no battery cells) and with an aggregate capacity of at least seven kilowatt hours (or one kilowatt hour for a hydrogen fuel cell vehicle).\u00a0</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119s536"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s536is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Fair SHARE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair SHARE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Sharing of Highways and Roads for Electric Vehicles Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to establish a tax on the sale of electric vehicles and batteries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:41Z"
    }
  ]
}
```
