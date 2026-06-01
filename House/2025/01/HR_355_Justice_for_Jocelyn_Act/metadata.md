# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/355?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/355
- Title: Justice for Jocelyn Act
- Congress: 119
- Bill type: HR
- Bill number: 355
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-09-03T08:05:22Z
- Update date including text: 2025-09-03T08:05:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/355",
    "number": "355",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Justice for Jocelyn Act",
    "type": "HR",
    "updateDate": "2025-09-03T08:05:22Z",
    "updateDateIncludingText": "2025-09-03T08:05:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T17:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "AZ"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "SC"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-04-14",
      "state": "CO"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "TX"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr355ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 355\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Nehls (for himself, Mr. Hunt , and Mr. Biggs of Arizona ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo remove aliens who fail to comply with a release order, to enroll all aliens on the nondetained docket of an immigration court in the Alternatives to Detention program with continuous GPS monitoring, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for Jocelyn Act .\n#### 2. Limitation on participation in alternatives to detention\nNo alien may be released as part of any program under the Alternatives to Detention program unless\u2014\n**(1)**\nall detention beds available to the Secretary have been filled;\n**(2)**\nthere exists no available option to hold aliens in detention; and\n**(3)**\nthe Secretary exercised and exhausted all reasonable efforts to hold aliens in detention.\n#### 3. Gps tracking and curfew requirements for certain aliens\nEach alien on the Immigration and Customs Enforcement\u2019s nondetained docket shall be enrolled in the Alternatives to Detention program and\u2014\n**(1)**\nshall be continuously subject to GPS monitoring\u2014\n**(A)**\nfor the duration of all applicable immigration proceedings, including any appeal; and\n**(B)**\nin the case of an alien who is ordered removed from the United States, until removal; and\n**(2)**\nshall be required to stay in their Alternatives to Detention-compliant home address between the hours of 10 p.m. to 5 a.m.\n#### 4. Removal of aliens who fail to comply with release order\nSection 240(b)(5) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(b)(5) ) is amended by adding at the end the following:\n(F) Failure to comply with release order In the case that an immigration officer submits an affidavit to an immigration judge stating that an alien failed to comply with a condition of release under section 236(a), such alien shall be ordered removed in absentia. .\n#### 5. Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held by a Federal court to be unconstitutional, the remainder of this Act and the application of such provisions to any other person or circumstance shall not be affected.",
      "versionDate": "2025-01-13",
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
        "actionDate": "2025-01-13",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "72",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Justice for Jocelyn Act",
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
        "name": "Immigration",
        "updateDate": "2025-02-10T20:38:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr355",
          "measure-number": "355",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr355v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Justice for Jocelyn Act</strong></p><p>This bill limits Immigration and Customs Enforcement\u2019s (ICE\u2019s) Alternatives to Detention program, which supervises\u00a0non-U.S. nationals (<em>aliens</em> under federal law) subject to removal who are released from the custody of the Department of Homeland Security (DHS). Specifically, releases under this program are prohibited unless all detention beds are filled and DHS found no alternatives after exercising and exhausting all reasonable options.</p><p>The bill requires all individuals on ICE\u2019s nondetained docket to be enrolled in the program and be subject to continuous GPS monitoring and curfew.</p><p>Further, the bill requires a\u00a0non-U.S. national who was arrested and released to be removed in absentia if an immigration officer submits an affidavit to an immigration judge stating that the individual failed to comply with a condition of release.</p>"
        },
        "title": "Justice for Jocelyn Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr355.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Justice for Jocelyn Act</strong></p><p>This bill limits Immigration and Customs Enforcement\u2019s (ICE\u2019s) Alternatives to Detention program, which supervises\u00a0non-U.S. nationals (<em>aliens</em> under federal law) subject to removal who are released from the custody of the Department of Homeland Security (DHS). Specifically, releases under this program are prohibited unless all detention beds are filled and DHS found no alternatives after exercising and exhausting all reasonable options.</p><p>The bill requires all individuals on ICE\u2019s nondetained docket to be enrolled in the program and be subject to continuous GPS monitoring and curfew.</p><p>Further, the bill requires a\u00a0non-U.S. national who was arrested and released to be removed in absentia if an immigration officer submits an affidavit to an immigration judge stating that the individual failed to comply with a condition of release.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr355"
    },
    "title": "Justice for Jocelyn Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Justice for Jocelyn Act</strong></p><p>This bill limits Immigration and Customs Enforcement\u2019s (ICE\u2019s) Alternatives to Detention program, which supervises\u00a0non-U.S. nationals (<em>aliens</em> under federal law) subject to removal who are released from the custody of the Department of Homeland Security (DHS). Specifically, releases under this program are prohibited unless all detention beds are filled and DHS found no alternatives after exercising and exhausting all reasonable options.</p><p>The bill requires all individuals on ICE\u2019s nondetained docket to be enrolled in the program and be subject to continuous GPS monitoring and curfew.</p><p>Further, the bill requires a\u00a0non-U.S. national who was arrested and released to be removed in absentia if an immigration officer submits an affidavit to an immigration judge stating that the individual failed to comply with a condition of release.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr355"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr355ih.xml"
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
      "title": "Justice for Jocelyn Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Justice for Jocelyn Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To remove aliens who fail to comply with a release order, to enroll all aliens on the nondetained docket of an immigration court in the Alternatives to Detention program with continuous GPS monitoring, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T09:03:21Z"
    }
  ]
}
```
