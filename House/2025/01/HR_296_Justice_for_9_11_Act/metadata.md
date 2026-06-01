# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/296?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/296
- Title: Justice for 9/11 Act
- Congress: 119
- Bill type: HR
- Bill number: 296
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-12-05T22:49:21Z
- Update date including text: 2025-12-05T22:49:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Armed Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/296",
    "number": "296",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Justice for 9/11 Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:49:21Z",
    "updateDateIncludingText": "2025-12-05T22:49:21Z"
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
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
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
          "date": "2025-01-09T14:37:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr296ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 296\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Lawler (for himself, Ms. Tenney , Ms. Malliotakis , Mr. Fitzpatrick , Mr. Garbarino , Mr. Loudermilk , Mr. Langworthy , Mr. Ellzey , and Mr. Crenshaw ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo address the plea agreements for certain individuals detained at United States Naval Station, Guantanamo Bay, Cuba, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for 9/11 Act .\n#### 2. Trial and post-trial matters relating to certain individuals detained at United States Naval Station, Guantanamo Bay, Cuba\n##### (a) Plea agreements and judgments\nNotwithstanding the provisions of section 949h of title 10, United States Code, any plea agreement entered into by Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi for actions involving the terrorist attack on September 11, 2001, and its related judgment, shall not preclude the trial of such individual under chapter 47A of such title or any other provision of law for that terrorist attack.\n##### (b) Sentencing\nNotwithstanding any other provision of law, in any trial of Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi under chapter 47A of title 10, United States Code, or any other provision of law for the terrorist attack of September 11, 2001, a sentence of death shall be available.\n##### (c) Conditions of confinement; transfer\nNotwithstanding any other provision of law, in the case of any sentence imposed on Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi, such individual\u2014\n**(1)**\nshall be\u2014\n**(A)**\nheld at United States Naval Station, Guantanamo Bay, Cuba, in solitary confinement;\n**(B)**\nprovided no contact with foreign nationals; and\n**(C)**\nprovided no psychological treatment except that specifically authorized by medical authorities at United States Naval Station, Guantanamo Bay, Cuba; and\n**(2)**\nshall not be transferred to the continental United States or any other country.",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-01-08",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "34",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Justice for 9/11 Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-03-05T16:08:18Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-03-05T16:08:18Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-03-05T16:08:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T15:36:56Z"
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
          "measure-id": "id119hr296",
          "measure-number": "296",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr296v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Justice for 9/11 Act</strong></p><p>This bill provides that any plea agreement entered into by\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi for actions involving the terrorist attack on September 11, 2001, and its related judgment must not preclude the trial of such individuals under other provisions of law for that attack. In any trial of such individuals, the death penalty must be available.</p><p>In the case of any sentence imposed on\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi, the individual must (1) be held at U.S. Naval Station, Guantanamo Bay, Cuba, in solitary confinement; (2) not be provided contact with foreign nationals; (3) not be provided with psychological treatment except that specifically authorized by medical authorities at Guantanamo Bay; and (4) not be transferred to the continental United States or any other country.</p>"
        },
        "title": "Justice for 9/11 Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr296.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Justice for 9/11 Act</strong></p><p>This bill provides that any plea agreement entered into by\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi for actions involving the terrorist attack on September 11, 2001, and its related judgment must not preclude the trial of such individuals under other provisions of law for that attack. In any trial of such individuals, the death penalty must be available.</p><p>In the case of any sentence imposed on\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi, the individual must (1) be held at U.S. Naval Station, Guantanamo Bay, Cuba, in solitary confinement; (2) not be provided contact with foreign nationals; (3) not be provided with psychological treatment except that specifically authorized by medical authorities at Guantanamo Bay; and (4) not be transferred to the continental United States or any other country.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr296"
    },
    "title": "Justice for 9/11 Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Justice for 9/11 Act</strong></p><p>This bill provides that any plea agreement entered into by\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi for actions involving the terrorist attack on September 11, 2001, and its related judgment must not preclude the trial of such individuals under other provisions of law for that attack. In any trial of such individuals, the death penalty must be available.</p><p>In the case of any sentence imposed on\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi, the individual must (1) be held at U.S. Naval Station, Guantanamo Bay, Cuba, in solitary confinement; (2) not be provided contact with foreign nationals; (3) not be provided with psychological treatment except that specifically authorized by medical authorities at Guantanamo Bay; and (4) not be transferred to the continental United States or any other country.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr296"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr296ih.xml"
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
      "title": "Justice for 9/11 Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Justice for 9/11 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address the plea agreements for certain individuals detained at United States Naval Station, Guantanamo Bay, Cuba, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T02:48:26Z"
    }
  ]
}
```
