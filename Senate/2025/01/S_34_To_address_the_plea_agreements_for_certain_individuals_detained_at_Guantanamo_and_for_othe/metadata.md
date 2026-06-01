# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/34?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/34
- Title: Justice for 9/11 Act
- Congress: 119
- Bill type: S
- Bill number: 34
- Origin chamber: Senate
- Introduced date: 2025-01-08
- Update date: 2025-12-05T22:49:10Z
- Update date including text: 2025-12-05T22:49:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-08: Introduced in Senate
- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-01-08: Introduced in Senate

## Actions

- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-08",
    "latestAction": {
      "actionDate": "2025-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/34",
    "number": "34",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Justice for 9/11 Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:10Z",
    "updateDateIncludingText": "2025-12-05T22:49:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-08",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-08",
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
          "date": "2025-01-08T18:37:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-01-08",
      "state": "KY"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s34is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 34\nIN THE SENATE OF THE UNITED STATES\nJanuary 8, 2025 Mr. Cotton (for himself and Mr. McConnell ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo address the plea agreements for certain individuals detained at Guantanamo, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for 9/11 Act .\n#### 2. Trial and post-trial matters relating to certain individuals detained at Guantanamo\n##### (a) Plea agreements and judgments\nNotwithstanding the provisions of section 949h of title 10, United States Code, any plea agreement entered into by Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi for actions involving the terrorist attack on September 11, 2001, and its related judgment, shall not preclude the trial of such individual under chapter 47A of such title or any other provision of law for that terrorist attack.\n##### (b) Sentencing\nNotwithstanding any other provision of law, in any trial of Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi under chapter 47A of title 10, United States Code, or any other provision of law for the terrorist attack of September 11, 2001, a sentence of death shall be available.\n##### (c) Conditions of confinement; transfer\nNotwithstanding any other provision of law, in the case of any sentence imposed on Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi, such individual\u2014\n**(1)**\nshall be\u2014\n**(A)**\nheld at United States Naval Station, Guantanamo Bay, Cuba, in solitary confinement;\n**(B)**\nprovided no contact with foreign nationals; and\n**(C)**\nprovided no psychological treatment except that specifically authorized by medical authorities at United States Naval Station, Guantanamo Bay; and\n**(2)**\nshall not be transferred to the continental United States or any other country.",
      "versionDate": "2025-01-08",
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
        "actionDate": "2025-01-09",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Justice for 9/11 Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-03-05T16:08:04Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-03-05T16:08:00Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-03-05T16:07:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T15:36:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-08",
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
          "measure-id": "id119s34",
          "measure-number": "34",
          "measure-type": "s",
          "orig-publish-date": "2025-01-08",
          "originChamber": "SENATE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s34v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Justice for 9/11 Act</strong></p><p>This bill provides that any plea agreement entered into by\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi for actions involving the terrorist attack on September 11, 2001, and its related judgment must not preclude the trial of such individuals under other provisions of law for that attack. In any trial of such individuals, the death penalty must be available.</p><p>In the case of any sentence imposed on\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi, the individual must (1) be held at U.S. Naval Station, Guantanamo Bay, Cuba, in solitary confinement; (2) not be provided contact with foreign nationals; (3) not be provided with psychological treatment except that specifically authorized by medical authorities at Guantanamo Bay; and (4) not be transferred to the continental United States or any other country.</p>"
        },
        "title": "Justice for 9/11 Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s34.xml",
    "summary": {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Justice for 9/11 Act</strong></p><p>This bill provides that any plea agreement entered into by\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi for actions involving the terrorist attack on September 11, 2001, and its related judgment must not preclude the trial of such individuals under other provisions of law for that attack. In any trial of such individuals, the death penalty must be available.</p><p>In the case of any sentence imposed on\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi, the individual must (1) be held at U.S. Naval Station, Guantanamo Bay, Cuba, in solitary confinement; (2) not be provided contact with foreign nationals; (3) not be provided with psychological treatment except that specifically authorized by medical authorities at Guantanamo Bay; and (4) not be transferred to the continental United States or any other country.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119s34"
    },
    "title": "Justice for 9/11 Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Justice for 9/11 Act</strong></p><p>This bill provides that any plea agreement entered into by\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi for actions involving the terrorist attack on September 11, 2001, and its related judgment must not preclude the trial of such individuals under other provisions of law for that attack. In any trial of such individuals, the death penalty must be available.</p><p>In the case of any sentence imposed on\u00a0Khalid Shaikh Mohammad, Walid Muhammad Salih Mubarak Bin \u2018Attash, or Mustafa Ahmed Adam al Hawsawi, the individual must (1) be held at U.S. Naval Station, Guantanamo Bay, Cuba, in solitary confinement; (2) not be provided contact with foreign nationals; (3) not be provided with psychological treatment except that specifically authorized by medical authorities at Guantanamo Bay; and (4) not be transferred to the continental United States or any other country.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119s34"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s34is.xml"
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
      "title": "Justice for 9/11 Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T01:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Justice for 9/11 Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T01:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address the plea agreements for certain individuals detained at Guantanamo, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:24Z"
    }
  ]
}
```
