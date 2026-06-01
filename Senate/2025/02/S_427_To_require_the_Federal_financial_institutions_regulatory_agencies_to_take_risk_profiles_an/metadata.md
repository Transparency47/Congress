# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/427?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/427
- Title: TAILOR Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 427
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2025-12-05T21:53:00Z
- Update date including text: 2025-12-05T21:53:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/427",
    "number": "427",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "TAILOR Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:53:00Z",
    "updateDateIncludingText": "2025-12-05T21:53:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T21:16:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "TN"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "WY"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "ND"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "MT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s427is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 427\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Rounds (for himself, Mr. Tillis , Mr. Hagerty , Ms. Lummis , Mr. Cramer , and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Federal financial institutions regulatory agencies to take risk profiles and business models of institutions into account when taking regulatory actions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taking Account of Institutions with Low Operation Risk Act of 2025 or the TAILOR Act of 2025 .\n#### 2. Tailoring regulation to business model and risk\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term Federal financial institutions regulatory agency means the Office of the Comptroller of the Currency, the Board of Governors of the Federal Reserve System, the Federal Deposit Insurance Corporation, the National Credit Union Administration, and the Bureau of Consumer Financial Protection; and\n**(2)**\nthe term regulatory action \u2014\n**(A)**\nmeans any proposed, interim, or final rule or regulation; and\n**(B)**\ndoes not include any action taken by a Federal financial institutions regulatory agency that is solely applicable to an individual institution, including an enforcement action or order.\n##### (b) Consideration and tailoring\nFor any regulatory action occurring after the date of enactment of this Act, each Federal financial institutions regulatory agency shall\u2014\n**(1)**\ntake into consideration the risk profile and business models of each type of institution or class of institutions subject to the regulatory action; and\n**(2)**\ntailor the regulatory action applicable to an institution, or type of institution, in a manner that limits the regulatory impact, including cost, human resource allocation, and other burdens, on the institution or type of institution as is appropriate for the risk profile and business model involved.\n##### (c) Factors To consider\nIn carrying out the requirements of subsection (b), each Federal financial institutions regulatory agency shall consider\u2014\n**(1)**\nthe aggregate impact of all applicable regulatory action on the ability of institutions to flexibly serve their customers and local markets on and after the date of enactment of this Act;\n**(2)**\nthe potential impact that efforts to implement the regulatory action and third-party service provider actions may work to undercut efforts to tailor the regulatory action described in subsection (b)(2); and\n**(3)**\nthe statutory provision authorizing the regulatory action, the congressional intent with respect to the statutory provision, and the underlying policy objectives of the regulatory action.\n##### (d) Notice of proposed and final rulemaking\nEach Federal financial institutions regulatory agency shall disclose and document in every notice of proposed rulemaking and in any final rulemaking for a regulatory action how the agency has applied subsections (b) and (c).\n##### (e) Reports to Congress\n**(1) Individual agency reports**\nNot later than 1 year after the date of enactment of this Act and annually thereafter, each Federal financial institutions regulatory agency shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report on the specific actions taken to tailor the regulatory actions of the Federal financial institutions regulatory agency pursuant to the requirements of this section.\n##### (f) Limited look-Back application\n**(1) In general**\nEach Federal financial institutions regulatory agency shall\u2014\n**(A)**\nconduct a review of all regulations issued in final form pursuant to statutes enacted during the period beginning on the date that is 7 years before the date on which this Act is introduced in the Senate and ending on the date of enactment of this Act; and\n**(B)**\napply the requirements of this section to the regulations described in subparagraph (A).\n**(2) Revision**\nAny regulation revised under paragraph (1) shall be revised not later than 3 years after the date of enactment of this Act.\n#### 3. Short-form call reports for all banks eligible for the community bank leverage ratio\nThe appropriate Federal banking agencies, as defined in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ), shall promulgate regulations establishing a reduced reporting requirement for all banks eligible for the Community Bank Leverage Ratio, as defined in section 201(a) of the Economic Growth, Regulatory Relief, and Consumer Protection Act ( 12 U.S.C. 5371 note), when making the first and third report of condition of a year as required by section 7(a) of the Federal Deposit Insurance Act ( 12 U.S.C. 1817(a) ).\n#### 4. Report to Congress on modernization of supervision\nNot later than 18 months after the date of enactment of this Act, the appropriate Federal banking agencies, as defined in section 3 of the Federal Deposit Insurance Act ( 12 U.S.C. 1813 ), in consultation with State bank supervisors, shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report on the modernization of bank supervision, including the following factors:\n**(1)**\nChanging bank business models.\n**(2)**\nExaminer workforce and training.\n**(3)**\nThe structure of supervisory activities within banking agencies.\n**(4)**\nImproving bank-supervisor communication and collaboration.\n**(5)**\nThe use of supervisory technology.\n**(6)**\nSupervisory factors uniquely applicable to community banks.\n**(7)**\nChanges in statutes necessary to achieve more effective supervision.",
      "versionDate": "2025-02-05",
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
        "actionDate": "2025-06-04",
        "text": "Placed on the Union Calendar, Calendar No. 104."
      },
      "number": "3380",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TAILOR Act of 2025",
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
            "name": "Banking and financial institutions regulation",
            "updateDate": "2025-05-28T14:50:41Z"
          },
          {
            "name": "Business records",
            "updateDate": "2025-05-28T14:50:41Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-28T14:50:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-12T16:48:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119s427",
          "measure-number": "427",
          "measure-type": "s",
          "orig-publish-date": "2025-02-05",
          "originChamber": "SENATE",
          "update-date": "2025-07-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s427v00",
            "update-date": "2025-07-29"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Taking Account of Institutions with Low Operation Risk Act of 2025 or the TAILOR Act of 2025</strong></p><p>This bill addresses the supervision of financial institutions.</p><p>Federal financial regulatory agencies must (1) tailor any regulatory actions so as to limit burdens on the institutions involved,\u00a0with consideration of the risk profiles and business models of those institutions; and (2) report to Congress on specific actions taken to do so, as well as on other related issues. The bill's\u00a0tailoring requirement applies to future regulatory actions and to regulations adopted within the last seven years.</p><p>The bill also reduces certain reporting requirements for community banks eligible for a simplified capital leverage ratio.</p><p>Finally, federal banking agencies must report on the modernization of bank supervision, including examiner workforce and training and statutory changes necessary to achieve more effective supervision.</p>"
        },
        "title": "TAILOR Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s427.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Taking Account of Institutions with Low Operation Risk Act of 2025 or the TAILOR Act of 2025</strong></p><p>This bill addresses the supervision of financial institutions.</p><p>Federal financial regulatory agencies must (1) tailor any regulatory actions so as to limit burdens on the institutions involved,\u00a0with consideration of the risk profiles and business models of those institutions; and (2) report to Congress on specific actions taken to do so, as well as on other related issues. The bill's\u00a0tailoring requirement applies to future regulatory actions and to regulations adopted within the last seven years.</p><p>The bill also reduces certain reporting requirements for community banks eligible for a simplified capital leverage ratio.</p><p>Finally, federal banking agencies must report on the modernization of bank supervision, including examiner workforce and training and statutory changes necessary to achieve more effective supervision.</p>",
      "updateDate": "2025-07-29",
      "versionCode": "id119s427"
    },
    "title": "TAILOR Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Taking Account of Institutions with Low Operation Risk Act of 2025 or the TAILOR Act of 2025</strong></p><p>This bill addresses the supervision of financial institutions.</p><p>Federal financial regulatory agencies must (1) tailor any regulatory actions so as to limit burdens on the institutions involved,\u00a0with consideration of the risk profiles and business models of those institutions; and (2) report to Congress on specific actions taken to do so, as well as on other related issues. The bill's\u00a0tailoring requirement applies to future regulatory actions and to regulations adopted within the last seven years.</p><p>The bill also reduces certain reporting requirements for community banks eligible for a simplified capital leverage ratio.</p><p>Finally, federal banking agencies must report on the modernization of bank supervision, including examiner workforce and training and statutory changes necessary to achieve more effective supervision.</p>",
      "updateDate": "2025-07-29",
      "versionCode": "id119s427"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s427is.xml"
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
      "title": "TAILOR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TAILOR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Taking Account of Institutions with Low Operation Risk Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Federal financial institutions regulatory agencies to take risk profiles and business models of institutions into account when taking regulatory actions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:53Z"
    }
  ]
}
```
