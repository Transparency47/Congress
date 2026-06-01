# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/72?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/72
- Title: Justice for Jocelyn Act
- Congress: 119
- Bill type: S
- Bill number: 72
- Origin chamber: Senate
- Introduced date: 2025-01-13
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in Senate
- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-13: Introduced in Senate

## Actions

- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/72",
    "number": "72",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Justice for Jocelyn Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T22:35:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "WV"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "LA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "TN"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "MT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "MS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s72is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 72\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2025 Mr. Cruz (for himself, Mrs. Capito , Mr. Cassidy , Mrs. Blackburn , Mr. Daines , Mr. Wicker , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo remove aliens who fail to comply with a release order, to enroll all aliens on the ICE nondetained docket in the Alternatives to Detention program with continuous GPS monitoring, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for Jocelyn Act .\n#### 2. Limitation on participation in Alternatives to Detention\nNo alien may be released as part of any program under an Alternatives to Detention program unless\u2014\n**(1)**\nall detention beds available to the Secretary of Homeland Security have been filled;\n**(2)**\nthere exists no available option to hold such alien in detention; and\n**(3)**\nthe Secretary has exercised and exhausted all reasonable efforts to hold such alien in detention.\n#### 3. GPS tracking and curfew requirements for certain aliens\nEach alien on U.S. Immigration and Customs Enforcement\u2019s nondetained docket shall be\u2014\n**(1)**\nenrolled in an Alternatives to Detention program;\n**(2)**\ncontinuously subject to GPS monitoring\u2014\n**(A)**\nfor the duration of all applicable immigration proceedings, including any appeal; and\n**(B)**\nin the case of an alien who has been ordered removed from the United States, until removal; and\n**(3)**\nrequired to stay in their Alternatives to Detention-compliant home address between the hours of 10:00 p.m. and 5:00 a.m.\n#### 4. Removal of aliens who fail to comply with release order\nSection 240(b)(5) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(b)(5) ) is amended by adding at the end the following:\n(F) Failure to comply with release order If an immigration officer submits an affidavit to an immigration judge stating that an alien failed to comply with a condition of release under section 236(a), such alien shall be ordered removed in absentia. .\n#### 5. Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held by a Federal court to be unconstitutional, the remainder of this Act and the application of such provisions to any other person or circumstance shall not be affected.",
      "versionDate": "2025-01-13",
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
        "actionDate": "2025-01-13",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "355",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Justice for Jocelyn Act",
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
        "name": "Immigration",
        "updateDate": "2025-02-13T15:38:02Z"
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
          "measure-id": "id119s72",
          "measure-number": "72",
          "measure-type": "s",
          "orig-publish-date": "2025-01-13",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s72v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Justice for Jocelyn Act</strong></p><p>This bill limits Immigration and Customs Enforcement\u2019s (ICE\u2019s) Alternatives to Detention program, which supervises\u00a0non-U.S. nationals (<em>aliens</em> under federal law) subject to removal who are released from the custody of the Department of Homeland Security (DHS). Specifically, releases under this program are prohibited unless all detention beds are filled and DHS found no alternatives after exercising and exhausting all reasonable options.</p><p>The bill requires all individuals on ICE\u2019s nondetained docket to be enrolled in the program and be subject to continuous GPS monitoring and curfew.</p><p>Further, the bill requires a\u00a0non-U.S. national who was arrested and released to be removed in absentia if an immigration officer submits an affidavit to an immigration judge stating that the individual failed to comply with a condition of release.</p>"
        },
        "title": "Justice for Jocelyn Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s72.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Justice for Jocelyn Act</strong></p><p>This bill limits Immigration and Customs Enforcement\u2019s (ICE\u2019s) Alternatives to Detention program, which supervises\u00a0non-U.S. nationals (<em>aliens</em> under federal law) subject to removal who are released from the custody of the Department of Homeland Security (DHS). Specifically, releases under this program are prohibited unless all detention beds are filled and DHS found no alternatives after exercising and exhausting all reasonable options.</p><p>The bill requires all individuals on ICE\u2019s nondetained docket to be enrolled in the program and be subject to continuous GPS monitoring and curfew.</p><p>Further, the bill requires a\u00a0non-U.S. national who was arrested and released to be removed in absentia if an immigration officer submits an affidavit to an immigration judge stating that the individual failed to comply with a condition of release.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s72"
    },
    "title": "Justice for Jocelyn Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Justice for Jocelyn Act</strong></p><p>This bill limits Immigration and Customs Enforcement\u2019s (ICE\u2019s) Alternatives to Detention program, which supervises\u00a0non-U.S. nationals (<em>aliens</em> under federal law) subject to removal who are released from the custody of the Department of Homeland Security (DHS). Specifically, releases under this program are prohibited unless all detention beds are filled and DHS found no alternatives after exercising and exhausting all reasonable options.</p><p>The bill requires all individuals on ICE\u2019s nondetained docket to be enrolled in the program and be subject to continuous GPS monitoring and curfew.</p><p>Further, the bill requires a\u00a0non-U.S. national who was arrested and released to be removed in absentia if an immigration officer submits an affidavit to an immigration judge stating that the individual failed to comply with a condition of release.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s72"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s72is.xml"
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
      "title": "Justice for Jocelyn Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Justice for Jocelyn Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to remove aliens who fail to comply with a release order, to enroll all aliens on the ICE nondetailed docket in the Alternatives to Detention program with continuous GPS monitoring, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:31Z"
    }
  ]
}
```
