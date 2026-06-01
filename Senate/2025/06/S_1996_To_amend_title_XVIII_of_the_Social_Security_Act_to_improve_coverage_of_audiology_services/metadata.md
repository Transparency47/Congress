# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1996?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1996
- Title: Medicare Audiology Access Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1996
- Origin chamber: Senate
- Introduced date: 2025-06-09
- Update date: 2025-12-02T12:03:45Z
- Update date including text: 2025-12-02T12:03:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-09: Introduced in Senate
- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-09: Introduced in Senate

## Actions

- 2025-06-09 - IntroReferral: Introduced in Senate
- 2025-06-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-09",
    "latestAction": {
      "actionDate": "2025-06-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1996",
    "number": "1996",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Medicare Audiology Access Improvement Act of 2025",
    "type": "S",
    "updateDate": "2025-12-02T12:03:45Z",
    "updateDateIncludingText": "2025-12-02T12:03:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-09",
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
      "actionDate": "2025-06-09",
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
          "date": "2025-06-09T22:25:41Z",
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
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "KY"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "IA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NH"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "VT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-09",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "MN"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NJ"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
      "state": "AZ"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "OR"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1996is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1996\nIN THE SENATE OF THE UNITED STATES\nJune 9, 2025 Ms. Warren (for herself, Mr. Paul , Mr. Grassley , Mrs. Shaheen , Mr. Welch , Mr. King , Ms. Klobuchar , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to improve coverage of audiology services under the Medicare program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medicare Audiology Access Improvement Act of 2025 .\n#### 2. Coverage of audiology services under the Medicare program\n##### (a) In general\nSection 1861(s)(2) of the Social Security Act ( 42 U.S.C. 1395x(s)(2) ) is amended\u2014\n**(1)**\nin subparagraph (JJ), by inserting and after the semicolon at the end; and\n**(2)**\nby adding at the end the following new subparagraph:\n(KK) audiology services (as defined in subsection (ll)(3)); .\n##### (b) Improved access to audiology services\nParagraph (3) of section 1861(ll) of the Social Security Act ( 42 U.S.C. 1395x(ll) ) is amended to read as follows:\n(3) The term audiology services means such hearing and balance assessment services and, beginning January 1, 2027, such treatment services, furnished by a qualified audiologist which the qualified audiologist is legally authorized to perform under State law (or the regulatory mechanism provided by State law), as would otherwise be covered if furnished by a physician or as incident to a physician\u2019s service. A qualified audiologist shall be permitted to furnish such audiology services without regard to any requirement that the individual receiving such audiology services is under the care of (or referred by) a physician or other health care practitioner or that such services are furnished under the supervision of a physician or other health care practitioner. .\n##### (c) Payment amount and coinsurance\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ) is amended\u2014\n**(1)**\nby striking and before (HH); and\n**(2)**\nby inserting the following before the semicolon: and (II) with respect to audiology services furnished under section 1861(s)(2)(KK), the amounts paid shall be 80 percent of the lesser of the actual charge for the services or the fee schedule amount provided under section 1848 .\n##### (d) Payment on assignment-Related basis\nSection 1842(b)(18)(C) of the Social Security Act ( 42 U.S.C. 1395u(b)(18)(C) ) is amended by adding at the end the following new clause:\n(ix) A qualified audiologist (as defined in section 1861(ll)(4)(B)). .\n##### (e) Inclusion of qualified audiologists as RHC and FQHC practitioners\nSection 1861(aa)(1)(B) of the Social Security Act ( 42 U.S.C. 1395x(aa)(1)(B) ) is amended\u2014\n**(1)**\nby striking or by a mental and inserting by a mental ; and\n**(2)**\nby inserting or by a qualified audiologist (as defined in subsection (ll)(4)(B)), after (as defined in subsection (lll)(4)), .\n##### (f) Rule of construction\nNothing in the amendments made by this section shall be construed to expand the scope of audiology services or services for which payment may be made to other providers under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) beyond those services for which such payment may be made as of December 31, 2026.\n##### (g) Effective date\nThe amendments made by this section shall apply to items and services furnished on or after January 1, 2027.",
      "versionDate": "2025-06-09",
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
        "actionDate": "2025-04-09",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2757",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Medicare Audiology Access Improvement Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-07-02T18:09:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-09",
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
          "measure-id": "id119s1996",
          "measure-number": "1996",
          "measure-type": "s",
          "orig-publish-date": "2025-06-09",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1996v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Medicare Audiology Access Improvement Act of 2025</strong></p><p>This bill provides for Medicare coverage of certain audiology services. Specifically, the bill expands coverage to include diagnostic and treatment services that are furnished by audiologists and that would otherwise be covered if provided by a physician, including incidental services, regardless of whether such services are provided pursuant to a referral from, or under the supervision of, a physician or other health care practitioner.</p>"
        },
        "title": "Medicare Audiology Access Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1996.xml",
    "summary": {
      "actionDate": "2025-06-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Medicare Audiology Access Improvement Act of 2025</strong></p><p>This bill provides for Medicare coverage of certain audiology services. Specifically, the bill expands coverage to include diagnostic and treatment services that are furnished by audiologists and that would otherwise be covered if provided by a physician, including incidental services, regardless of whether such services are provided pursuant to a referral from, or under the supervision of, a physician or other health care practitioner.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1996"
    },
    "title": "Medicare Audiology Access Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Medicare Audiology Access Improvement Act of 2025</strong></p><p>This bill provides for Medicare coverage of certain audiology services. Specifically, the bill expands coverage to include diagnostic and treatment services that are furnished by audiologists and that would otherwise be covered if provided by a physician, including incidental services, regardless of whether such services are provided pursuant to a referral from, or under the supervision of, a physician or other health care practitioner.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1996"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1996is.xml"
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
      "title": "Medicare Audiology Access Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T12:03:45Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medicare Audiology Access Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to improve coverage of audiology services under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T03:33:22Z"
    }
  ]
}
```
