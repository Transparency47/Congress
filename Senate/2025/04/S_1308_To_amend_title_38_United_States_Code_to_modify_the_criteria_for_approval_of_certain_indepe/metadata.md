# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1308?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1308
- Title: VETS Opportunity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1308
- Origin chamber: Senate
- Introduced date: 2025-04-04
- Update date: 2026-03-27T11:03:21Z
- Update date including text: 2026-03-27T11:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-04: Introduced in Senate
- 2025-04-04 - IntroReferral: Introduced in Senate
- 2025-04-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-04-04: Introduced in Senate

## Actions

- 2025-04-04 - IntroReferral: Introduced in Senate
- 2025-04-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-04",
    "latestAction": {
      "actionDate": "2025-04-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1308",
    "number": "1308",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "VETS Opportunity Act of 2025",
    "type": "S",
    "updateDate": "2026-03-27T11:03:21Z",
    "updateDateIncludingText": "2026-03-27T11:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-04",
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
        "item": [
          {
            "date": "2025-04-04T19:34:00Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-04T19:34:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "NC"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "TX"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "TX"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "AZ"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "OH"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "MI"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "FL"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1308is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1308\nIN THE SENATE OF THE UNITED STATES\nApril 4, 2025 Mr. Tillis (for himself, Mr. Budd , Mr. Cornyn , Mr. Cruz , Mr. Gallego , Mr. Moreno , Mr. Peters , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to modify the criteria for approval of certain independent study programs for purposes of the educational assistance programs of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Veterans Education and Technical Skills Opportunity Act of 2025 or the VETS Opportunity Act of 2025 .\n#### 2. Treatment of certain independent study programs under educational assistance programs of Department of Veterans Affairs\n##### (a) In general\nSection 3680A(a)(4)(A)(ii)(III) of title 38, United States Code, is amended\u2014\n**(1)**\nin the matter before item (aa), by inserting that requires regular and substantive interaction between students and instructors after study ; and\n**(2)**\nby amending item (bb) to read as follows:\n(bb) an institution of higher education (as defined in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 )) that is participating in a student financial assistance program authorized by title IV of that Act; and .\n##### (b) Applicability\nThe amendment made by subsection (a) shall apply with respect to any quarter, semester, or term, as applicable, that begins on or after August 1, 2025.",
      "versionDate": "2025-04-04",
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
        "actionDate": "2026-02-03",
        "text": "Received in the Senate and Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "1458",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "VETS Opportunity Act of 2025",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T18:25:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-04",
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
          "measure-id": "id119s1308",
          "measure-number": "1308",
          "measure-type": "s",
          "orig-publish-date": "2025-04-04",
          "originChamber": "SENATE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1308v00",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-04-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans Education and Technical Skills Opportunity Act of 2025 or the VETS Opportunity Act of 2025</strong></p><p>This bill modifies which independent study programs are covered under veterans\u2019 educational assistance benefits.</p><p>The bill requires independent study programs that lead to a certificate that reflects graduation from a course of study to include regular and substantive interaction between students and instructors.</p><p>The bill allows such independent study programs to be offered by any institutions of higher education, including for-profit institutions, that are approved to participate in the Department of Education\u2019s financial assistance programs.</p>"
        },
        "title": "VETS Opportunity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1308.xml",
    "summary": {
      "actionDate": "2025-04-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Education and Technical Skills Opportunity Act of 2025 or the VETS Opportunity Act of 2025</strong></p><p>This bill modifies which independent study programs are covered under veterans\u2019 educational assistance benefits.</p><p>The bill requires independent study programs that lead to a certificate that reflects graduation from a course of study to include regular and substantive interaction between students and instructors.</p><p>The bill allows such independent study programs to be offered by any institutions of higher education, including for-profit institutions, that are approved to participate in the Department of Education\u2019s financial assistance programs.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119s1308"
    },
    "title": "VETS Opportunity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Education and Technical Skills Opportunity Act of 2025 or the VETS Opportunity Act of 2025</strong></p><p>This bill modifies which independent study programs are covered under veterans\u2019 educational assistance benefits.</p><p>The bill requires independent study programs that lead to a certificate that reflects graduation from a course of study to include regular and substantive interaction between students and instructors.</p><p>The bill allows such independent study programs to be offered by any institutions of higher education, including for-profit institutions, that are approved to participate in the Department of Education\u2019s financial assistance programs.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119s1308"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1308is.xml"
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
      "title": "VETS Opportunity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VETS Opportunity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Education and Technical Skills Opportunity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to modify the criteria for approval of certain independent study programs for purposes of the educational assistance programs of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:30Z"
    }
  ]
}
```
