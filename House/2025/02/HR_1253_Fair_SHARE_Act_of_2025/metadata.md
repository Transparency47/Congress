# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1253?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1253
- Title: Fair SHARE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1253
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-12-05T22:50:19Z
- Update date including text: 2025-12-05T22:50:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1253",
    "number": "1253",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Fair SHARE Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:50:19Z",
    "updateDateIncludingText": "2025-12-05T22:50:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "OH"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "KS"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "MO"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1253ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1253\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Johnson of South Dakota (for himself and Mr. Taylor ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a tax on the sale of electric vehicles and batteries.\n#### 1. Short title\nThis Act may be cited as the Fair Sharing of Highways and Roads for Electric Vehicles Act of 2025 or the Fair SHARE Act of 2025 .\n#### 2. Tax on sale of electric vehicles and batteries\n##### (a) Imposition of tax\n**(1) In general**\nSubchapter A of chapter 32 of the Internal Revenue Code of 1986 is amended by adding at the end the following new part:\nIV Electric Vehicles and Batteries Sec. 4091. Tax on Electric Vehicles and Batteries. 4091. Tax on Electric Vehicles and batteries (a) Battery module There is hereby imposed a tax equal to $550 on each battery module with a weight of greater than 1,000 pounds which is\u2014 (1) sold by the manufacturer, producer, or importer thereof, and (2) intended for use in an electric vehicle. (b) Electric vehicles There is hereby imposed a tax equal to $1,000 on each electric vehicle sold by the manufacturer, producer, or importer thereof. (c) Definitions In this section\u2014 (1) Battery module The term battery module has the same meaning given such term in section 45X(c)(5)(B)(iii). (2) Electric vehicle (A) In general The term electric vehicle means a light-duty vehicle which satisfies the requirements under section 30D(d)(1)(F). (B) Exception for hybrid vehicles The term electric vehicle shall not include any motor vehicle which draws propulsion energy from onboard sources of stored energy which are both\u2014 (i) an internal combustion or heat engine using consumable fuel, and (ii) a rechargeable energy storage system. (3) Light-duty vehicle The term light-duty vehicle means a motor vehicle, as defined in section 30D(d)(2), which has a gross vehicle weight rating of less than 8,500 pounds. .\n**(2) Clerical amendment**\nThe table of parts for subchapter A of chapter 32 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nPART IV\u2014ELECTRIC VEHICLES AND BATTERIES .\n##### (b) Transfer of revenue to Highway Trust Fund\nSection 9503(b)(1) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subparagraph (D), by striking and at the end,\n**(2)**\nby redesignating subparagraph (E) as subparagraph (F), and\n**(3)**\nby inserting after subparagraph (D) the following new subparagraph:\n(E) section 4091 (relating to tax on electric vehicles and batteries), and .\n##### (c) Effective date\nThe amendments made by this section shall apply to sales after December 31, 2025.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-02-12",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "536",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fair SHARE Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-05-05T18:57:05Z"
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
          "measure-id": "id119hr1253",
          "measure-number": "1253",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-09-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1253v00",
            "update-date": "2025-09-24"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fair Sharing of Highways and Roads for Electric Vehicles\u00a0Act of 2025</strong></p><p>This bill imposes a new excise tax in the amount of $1,000 on the sale of an electric vehicle and a new excise tax in the amount of $550 on the sale of a battery module weighing over 1,000 pounds for use in an electric vehicle. The bill also requires the Department of the Treasury to transfer amounts collected from the new excise taxes to the Highway Trust Fund. (The Highway Trust Fund, which supports surface transportation programs and projects, is funded by transportation-related\u00a0excise\u00a0taxes.)</p><p>The bill defines <em>electric vehicle</em> as a light-duty vehicle (a motor vehicle weighing less than 8,500 pounds that is manufactured for use on public roads) that is powered by a battery with a capacity of at least seven kilowatt hours and is recharged through an external source of electricity. Under the bill, the excise tax\u00a0does not apply to hybrid vehicles, which are powered by a combination of fuel and a rechargeable energy storage system.</p><p>The bill defines <em>battery module</em> as a module with\u00a0two or more battery cells configured to create voltage or current (or no battery cells) and with an aggregate capacity of at least seven kilowatt hours (or one kilowatt hour for a hydrogen fuel cell vehicle).\u00a0</p>"
        },
        "title": "Fair SHARE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1253.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Sharing of Highways and Roads for Electric Vehicles\u00a0Act of 2025</strong></p><p>This bill imposes a new excise tax in the amount of $1,000 on the sale of an electric vehicle and a new excise tax in the amount of $550 on the sale of a battery module weighing over 1,000 pounds for use in an electric vehicle. The bill also requires the Department of the Treasury to transfer amounts collected from the new excise taxes to the Highway Trust Fund. (The Highway Trust Fund, which supports surface transportation programs and projects, is funded by transportation-related\u00a0excise\u00a0taxes.)</p><p>The bill defines <em>electric vehicle</em> as a light-duty vehicle (a motor vehicle weighing less than 8,500 pounds that is manufactured for use on public roads) that is powered by a battery with a capacity of at least seven kilowatt hours and is recharged through an external source of electricity. Under the bill, the excise tax\u00a0does not apply to hybrid vehicles, which are powered by a combination of fuel and a rechargeable energy storage system.</p><p>The bill defines <em>battery module</em> as a module with\u00a0two or more battery cells configured to create voltage or current (or no battery cells) and with an aggregate capacity of at least seven kilowatt hours (or one kilowatt hour for a hydrogen fuel cell vehicle).\u00a0</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119hr1253"
    },
    "title": "Fair SHARE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair Sharing of Highways and Roads for Electric Vehicles\u00a0Act of 2025</strong></p><p>This bill imposes a new excise tax in the amount of $1,000 on the sale of an electric vehicle and a new excise tax in the amount of $550 on the sale of a battery module weighing over 1,000 pounds for use in an electric vehicle. The bill also requires the Department of the Treasury to transfer amounts collected from the new excise taxes to the Highway Trust Fund. (The Highway Trust Fund, which supports surface transportation programs and projects, is funded by transportation-related\u00a0excise\u00a0taxes.)</p><p>The bill defines <em>electric vehicle</em> as a light-duty vehicle (a motor vehicle weighing less than 8,500 pounds that is manufactured for use on public roads) that is powered by a battery with a capacity of at least seven kilowatt hours and is recharged through an external source of electricity. Under the bill, the excise tax\u00a0does not apply to hybrid vehicles, which are powered by a combination of fuel and a rechargeable energy storage system.</p><p>The bill defines <em>battery module</em> as a module with\u00a0two or more battery cells configured to create voltage or current (or no battery cells) and with an aggregate capacity of at least seven kilowatt hours (or one kilowatt hour for a hydrogen fuel cell vehicle).\u00a0</p>",
      "updateDate": "2025-09-24",
      "versionCode": "id119hr1253"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1253ih.xml"
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
      "title": "Fair SHARE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair SHARE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T08:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Sharing of Highways and Roads for Electric Vehicles Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T08:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a tax on the sale of electric vehicles and batteries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T08:18:32Z"
    }
  ]
}
```
