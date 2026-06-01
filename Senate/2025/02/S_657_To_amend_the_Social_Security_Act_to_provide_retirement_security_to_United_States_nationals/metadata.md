# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/657?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/657
- Title: Retirement Security for American Hostages Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 657
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2025-08-04T18:56:30Z
- Update date including text: 2025-08-04T18:56:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/657",
    "number": "657",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "Retirement Security for American Hostages Act of 2025",
    "type": "S",
    "updateDate": "2025-08-04T18:56:30Z",
    "updateDateIncludingText": "2025-08-04T18:56:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T19:34:00Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "LA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "VA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "ME"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s657is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 657\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Coons (for himself, Mr. Cassidy , Mr. Kaine , Ms. Collins , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Social Security Act to provide retirement security to United States nationals who were unlawfully or wrongfully detained or held hostage abroad.\n#### 1. Short title\nThis Act may be cited as the Retirement Security for American Hostages Act of 2025 .\n#### 2. Deemed wages for hostages and individuals wrongfully detained abroad\n##### (a) In general\nTitle II of the Social Security Act is amended by adding after section 234 ( 42 U.S.C. 434 ) the following new section:\n235. Deemed wages for hostages and individuals wrongfully detained abroad (a) Definitions For purposes of this section\u2014 (1) Qualifying month (A) In general Subject to subparagraph (B), the term qualifying month means, in connection with an individual, any month\u2014 (i) beginning before, on, or after the date of enactment of this section, and (ii) during which such individual was\u2014 (I) unlawfully or wrongfully detained abroad; or (II) held hostage abroad. (B) Exception The term qualifying month does not include any month ending after the date on which such individual attains retirement age (as defined in section 216(l)). (2) Qualifying individual The term qualifying individual means an individual who is\u2014 (A) a United States national unlawfully or wrongfully detained abroad, as determined under section 302 of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741 ); or (B) a United States national taken hostage abroad, as determined pursuant to the findings of the Hostage Recovery Fusion Cell (as described in section 304 of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741b )). (b) Deemed Wages (1) In general For purposes of determining entitlement to and the amount of any monthly benefit for any month, or entitlement to and the amount of any lump-sum death payment in the case of a death, payable under this title on the basis of the wages and self-employment income of any qualifying individual, such individual shall be deemed to have been paid during each qualifying month at an amount per month equal to 1/12 th of the national average wage index (as defined in section 209(k)(1)) for the second calendar year preceding the calendar year in which such month occurs. (2) Exception Paragraph (1) shall not be applicable in the case of any monthly benefit or lump-sum death payment if a larger such benefit or payment, as the case may be, would be payable without its application. (c) Rules and regulations (1) In general Not later than 1 year after the date of the enactment of this section, the Commissioner of Social Security shall promulgate such regulations as are necessary to carry out this section, including regulations establishing procedures for the application and certification requirements described in paragraph (2). (2) Application and certification requirements A qualifying month shall not be taken into account under this section with respect to an individual unless the individual (or any other individual entitled to any benefit or payment payable under this title on the basis of the wages and self-employment income of such individual) submits to the Commissioner of Social Security an application for benefits under this section that includes\u2014 (A) documentation of a determination made by a Federal agency that the individual satisfies the requirements under subsection (a)(2) with respect to a qualifying individual, including the period during which the individual was\u2014 (i) unlawfully or wrongfully detained abroad; or (ii) held hostage abroad; and (B) such other information as the Commissioner may require. .\n##### (b) Conforming amendment\nSection 209(k)(1) of such Act ( 42 U.S.C. 409(k)(1) ) is amended\u2014\n**(1)**\nby striking and before 230(b)(2) the first time it appears; and\n**(2)**\nby inserting and 235(b)(1), after 1977), .\n##### (c) Effective date\nThe amendments made by this section shall take effect on the date which is 24 months after the date of enactment of this Act.",
      "versionDate": "2025-02-20",
      "versionType": "Introduced in Senate"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-13T17:21:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
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
          "measure-id": "id119s657",
          "measure-number": "657",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2025-08-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s657v00",
            "update-date": "2025-08-04"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Retirement Security for American Hostages Act of 2025</strong></p><p>This bill permits individuals held hostage or wrongfully detained abroad to collect Social Security benefits based on average national wages for months in which they were held hostage or detained.\u00a0</p><p>Specifically, for purposes of determining Social Security benefits based on an individual\u2019s wages or self-employment income, the bill directs the Social Security Administration (SSA) to deem qualifying individuals to have been paid a monthly portion of the national average wage index for any month during which the individual was held hostage or unlawfully or wrongfully detained abroad. (The national average wage index is determined annually by the SSA.) Deemed wages must apply for any affected month before the individual reaches the statutory retirement age (generally between ages 65 and 67).\u00a0</p><p>A <em>qualifying individual</em> is a U.S. national (1) determined by the Department of State to have been unlawfully or wrongfully detained abroad, or (2) determined by the interagency Hostage Recovery Fusion Cell to have been taken hostage abroad.\u00a0</p><p>A qualifying individual or an individual entitled to benefits on the basis of a qualifying individual\u2019s wages and income must apply to the SSA in order to receive deemed wages for affected months. These provisions do not apply if a larger benefit would be available without the application of deemed wages. \u00a0</p>"
        },
        "title": "Retirement Security for American Hostages Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s657.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Retirement Security for American Hostages Act of 2025</strong></p><p>This bill permits individuals held hostage or wrongfully detained abroad to collect Social Security benefits based on average national wages for months in which they were held hostage or detained.\u00a0</p><p>Specifically, for purposes of determining Social Security benefits based on an individual\u2019s wages or self-employment income, the bill directs the Social Security Administration (SSA) to deem qualifying individuals to have been paid a monthly portion of the national average wage index for any month during which the individual was held hostage or unlawfully or wrongfully detained abroad. (The national average wage index is determined annually by the SSA.) Deemed wages must apply for any affected month before the individual reaches the statutory retirement age (generally between ages 65 and 67).\u00a0</p><p>A <em>qualifying individual</em> is a U.S. national (1) determined by the Department of State to have been unlawfully or wrongfully detained abroad, or (2) determined by the interagency Hostage Recovery Fusion Cell to have been taken hostage abroad.\u00a0</p><p>A qualifying individual or an individual entitled to benefits on the basis of a qualifying individual\u2019s wages and income must apply to the SSA in order to receive deemed wages for affected months. These provisions do not apply if a larger benefit would be available without the application of deemed wages. \u00a0</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119s657"
    },
    "title": "Retirement Security for American Hostages Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Retirement Security for American Hostages Act of 2025</strong></p><p>This bill permits individuals held hostage or wrongfully detained abroad to collect Social Security benefits based on average national wages for months in which they were held hostage or detained.\u00a0</p><p>Specifically, for purposes of determining Social Security benefits based on an individual\u2019s wages or self-employment income, the bill directs the Social Security Administration (SSA) to deem qualifying individuals to have been paid a monthly portion of the national average wage index for any month during which the individual was held hostage or unlawfully or wrongfully detained abroad. (The national average wage index is determined annually by the SSA.) Deemed wages must apply for any affected month before the individual reaches the statutory retirement age (generally between ages 65 and 67).\u00a0</p><p>A <em>qualifying individual</em> is a U.S. national (1) determined by the Department of State to have been unlawfully or wrongfully detained abroad, or (2) determined by the interagency Hostage Recovery Fusion Cell to have been taken hostage abroad.\u00a0</p><p>A qualifying individual or an individual entitled to benefits on the basis of a qualifying individual\u2019s wages and income must apply to the SSA in order to receive deemed wages for affected months. These provisions do not apply if a larger benefit would be available without the application of deemed wages. \u00a0</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119s657"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s657is.xml"
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
      "title": "Retirement Security for American Hostages Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Retirement Security for American Hostages Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Social Security Act to provide retirement security to United States nationals who were unlawfully or wrongfully detained or held hostage abroad.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:45Z"
    }
  ]
}
```
