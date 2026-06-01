# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/256?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/256
- Title: SAVE Act
- Congress: 119
- Bill type: HR
- Bill number: 256
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-03-27T12:32:01Z
- Update date including text: 2025-03-27T12:32:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/256",
    "number": "256",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "SAVE Act",
    "type": "HR",
    "updateDate": "2025-03-27T12:32:01Z",
    "updateDateIncludingText": "2025-03-27T12:32:01Z"
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
          "date": "2025-01-09T14:35:15Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IN"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "SD"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "UT"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "KS"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr256ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 256\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mrs. Bice (for herself, Mr. Baird , Mr. Valadao , Mr. Johnson of South Dakota , Mr. Owens , Mr. Mann , Mr. Rutherford , and Mr. Donalds ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the sale of petroleum products from the Strategic Petroleum Reserve to certain entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Save America\u2019s Valuable Energy Act or the SAVE Act .\n#### 2. Prohibition against selling SPR petroleum products to certain entities\n##### (a) Prohibition\nThe Energy Policy and Conservation Act is amended by inserting after section 169 ( 42 U.S.C. 6247b ) the following:\n170. Prohibition on sales to certain entities The Secretary shall prohibit the sale of petroleum products drawn down from the Strategic Petroleum Reserve, under any provision of law, to any entity headquartered in\u2014 (1) a country listed in table 1 to paragraph (d)(1) under section 126.1 of title 22, Code of Federal Regulations, as in effect on the date of enactment of this section; or (2) Russia. .\n##### (b) Conforming amendments\n**(1) Drawdown and sale of petroleum products**\nSection 161(a) of the Energy Policy and Conservation Act ( 42 U.S.C. 6241(a) ) is amended by inserting and section 170 before the period at the end.\n**(2) Table of contents**\nThe table of contents for the Energy Policy and Conservation Act is amended by inserting after the item relating to section 169 the following:\nSec. 170. Prohibition on sales to certain entities. .",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-02-07T12:59:59Z"
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
          "measure-id": "id119hr256",
          "measure-number": "256",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr256v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Save America\u2019s Valuable Energy Act or the SAVE Act</strong></p><p>This bill directs the Department of Energy to prohibit the sale of petroleum products (e.g., crude oil) from the Strategic Petroleum Reserve to entities headquartered in Russia,\u00a0Belarus, Burma, China, Cuba, Iran, North Korea, Syria, or\u00a0Venezuela.</p>"
        },
        "title": "SAVE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr256.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Save America\u2019s Valuable Energy Act or the SAVE Act</strong></p><p>This bill directs the Department of Energy to prohibit the sale of petroleum products (e.g., crude oil) from the Strategic Petroleum Reserve to entities headquartered in Russia,\u00a0Belarus, Burma, China, Cuba, Iran, North Korea, Syria, or\u00a0Venezuela.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr256"
    },
    "title": "SAVE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Save America\u2019s Valuable Energy Act or the SAVE Act</strong></p><p>This bill directs the Department of Energy to prohibit the sale of petroleum products (e.g., crude oil) from the Strategic Petroleum Reserve to entities headquartered in Russia,\u00a0Belarus, Burma, China, Cuba, Iran, North Korea, Syria, or\u00a0Venezuela.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr256"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr256ih.xml"
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
      "title": "SAVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T02:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T02:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save America\u2019s Valuable Energy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T02:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the sale of petroleum products from the Strategic Petroleum Reserve to certain entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T02:18:26Z"
    }
  ]
}
```
