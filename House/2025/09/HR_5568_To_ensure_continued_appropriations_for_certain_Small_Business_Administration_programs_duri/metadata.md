# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5568?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5568
- Title: Funding Small Businesses During Shutdown Act
- Congress: 119
- Bill type: HR
- Bill number: 5568
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-10-15T08:05:32Z
- Update date including text: 2025-10-15T08:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5568",
    "number": "5568",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001136",
        "district": "3",
        "firstName": "Herbert",
        "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
        "lastName": "Conaway",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Funding Small Businesses During Shutdown Act",
    "type": "HR",
    "updateDate": "2025-10-15T08:05:32Z",
    "updateDateIncludingText": "2025-10-15T08:05:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "MN"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "MD"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "OH"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NV"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "DE"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MO"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5568ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5568\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Conaway (for himself, Ms. Simon , Mr. Castro of Texas , Ms. Morrison , and Mr. Olszewski ) introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo ensure continued appropriations for certain Small Business Administration programs during a Government shutdown, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Funding Small Businesses During Shutdown Act .\n#### 2. Continuation of certain Small Business Administration programs during a Government shutdown\nThere are appropriated for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, during any period of a lapse in discretionary appropriations with respect to the Small Business Administration during such fiscal year beginning on or after the date of the enactment of this section, for any 30-day period of such lapse (and on a pro-rated basis if such lapse is less than 30 days) to pay for the salaries and expenses necessary to continue servicing any loans made under\u2014\n**(1)**\n$500,000 for loans made under subsection (m) of section 7 of the Small Business Act ( 15 U.S.C. 636(m) );\n**(2)**\n$2,916,666,667 for loans made under subsection (a) of section 7 of the Small Business Act ( 15 U.S.C. 636(a) );\n**(3)**\n$1,250,000,000 for loans made under title V of the Small Business Investment Act of 1958 ( 15 U.S.C. 695 et seq. ); and\n**(4)**\n$13,775,000 for administrative expenses to carry out the loan program under subsection (m) of section 7 of the Small Business Act ( 15 U.S.C. 636(m) ).",
      "versionDate": "2025-09-26",
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
        "name": "Commerce",
        "updateDate": "2025-10-09T15:04:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-26",
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
          "measure-id": "id119hr5568",
          "measure-number": "5568",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-26",
          "originChamber": "HOUSE",
          "update-date": "2025-10-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5568v00",
            "update-date": "2025-10-09"
          },
          "action-date": "2025-09-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Funding Small Businesses During Shutdown Act</strong></p><p>This bill provides FY2026 appropriations to continue servicing loans made under certain Small Business Administration (SBA) loan programs if there is a lapse in discretionary appropriations (i.e., government shutdown) in FY2026.</p><p>If there is a lapse in FY2026 appropriations for the SBA, the bill provides specified appropriations to pay for the salaries and expenses necessary to continue servicing any loans made under several loan programs authorized by the Small Business Act and the Small Business Investment Act of 1958.</p><p>The bill provides the appropriations for any 30-day period in which there is a lapse in SBA appropriations and on a pro-rated basis if the lapse is less than 30 days.</p>"
        },
        "title": "Funding Small Businesses During Shutdown Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5568.xml",
    "summary": {
      "actionDate": "2025-09-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Funding Small Businesses During Shutdown Act</strong></p><p>This bill provides FY2026 appropriations to continue servicing loans made under certain Small Business Administration (SBA) loan programs if there is a lapse in discretionary appropriations (i.e., government shutdown) in FY2026.</p><p>If there is a lapse in FY2026 appropriations for the SBA, the bill provides specified appropriations to pay for the salaries and expenses necessary to continue servicing any loans made under several loan programs authorized by the Small Business Act and the Small Business Investment Act of 1958.</p><p>The bill provides the appropriations for any 30-day period in which there is a lapse in SBA appropriations and on a pro-rated basis if the lapse is less than 30 days.</p>",
      "updateDate": "2025-10-09",
      "versionCode": "id119hr5568"
    },
    "title": "Funding Small Businesses During Shutdown Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Funding Small Businesses During Shutdown Act</strong></p><p>This bill provides FY2026 appropriations to continue servicing loans made under certain Small Business Administration (SBA) loan programs if there is a lapse in discretionary appropriations (i.e., government shutdown) in FY2026.</p><p>If there is a lapse in FY2026 appropriations for the SBA, the bill provides specified appropriations to pay for the salaries and expenses necessary to continue servicing any loans made under several loan programs authorized by the Small Business Act and the Small Business Investment Act of 1958.</p><p>The bill provides the appropriations for any 30-day period in which there is a lapse in SBA appropriations and on a pro-rated basis if the lapse is less than 30 days.</p>",
      "updateDate": "2025-10-09",
      "versionCode": "id119hr5568"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5568ih.xml"
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
      "title": "Funding Small Businesses During Shutdown Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Funding Small Businesses During Shutdown Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T10:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure continued appropriations for certain Small Business Administration programs during a Government shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:14Z"
    }
  ]
}
```
