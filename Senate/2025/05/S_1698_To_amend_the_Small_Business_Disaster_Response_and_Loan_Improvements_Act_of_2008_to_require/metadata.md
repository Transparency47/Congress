# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1698?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1698
- Title: Small Business Disaster Coordination Act
- Congress: 119
- Bill type: S
- Bill number: 1698
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-06-05T11:03:18Z
- Update date including text: 2025-06-05T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1698",
    "number": "1698",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Small Business Disaster Coordination Act",
    "type": "S",
    "updateDate": "2025-06-05T11:03:18Z",
    "updateDateIncludingText": "2025-06-05T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T19:27:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "WA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "ID"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CO"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MI"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1698is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1698\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Risch (for himself, Ms. Cantwell , Mr. Crapo , Mr. Bennet , and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Disaster Response and Loan Improvements Act of 2008 to require the Small Business Administration to coordinate with resource partners with respect to disaster planning activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Business Disaster Coordination Act .\n#### 2. Coordination in disaster response and disaster planning\n##### (a) Disaster response coordination\nThe Small Business Act ( 15 U.S.C. 631 et seq. ) is amended\u2014\n**(1)**\nin section 4 ( 15 U.S.C. 633 ), by adding at the end the following:\n(i) Disaster recovery assistance from resource partners (1) Authorization At the discretion of the Administrator, the Administrator may authorize a resource partner of the Administration to provide advice, information, and assistance to a small business concern located outside of the area of service in which that resource partner provides services, without regard to geographic proximity to that resource partner, if\u2014 (A) the small business concern is located in an area with respect to which loans under section 7(b)(2) may be made; and (B) in providing that advice, information, and assistance, the resource partner coordinates with another resource partner that serves the area in which the small business concern is located. (2) Period of assistance (A) In general A resource partner of the Administration may provide advice, information, and assistance to a small business concern under paragraph (1) for a period of not more than 2 years after the date on which the applicable disaster has been determined to exist. (B) Extension The Administrator may, at the discretion of the Administrator, extend the period described in subparagraph (A). (3) Continuity of services A resource partner of the Administration that provides counselors to an area pursuant to an authorization under paragraph (1) shall, to the maximum extent practicable, ensure continuity of services in any area of service in which that resource partner otherwise provides services. (4) Sites and facilities For purposes of this subsection, the Administrator shall, to the maximum extent practicable, permit the personnel of a resource partner of the Administration to use any site or facility designated by the Administrator for use to provide disaster recovery assistance. ;\n**(2)**\nin section 7(b)(5) ( 15 U.S.C. 636(b)(5) )\u2014\n**(A)**\nby redesignating subparagraphs (A) through (G) as clauses (i) through (vii), respectively, and adjusting the margins accordingly;\n**(B)**\nby striking If a disaster and inserting the following:\n(A) In general If a disaster ;\n**(C)**\nin subparagraph (A), as so redesignated\u2014\n**(i)**\nin clause (vi), as so redesignated, by striking and at the end;\n**(ii)**\nin clause (vii), as so redesignated, by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(viii) links to websites of resource partners of the Administration. ; and\n**(D)**\nby adding at the end the following:\n(B) Provision of information to resource partners In carrying out subparagraph (A), the Administrator shall make all information communicated under that subparagraph available to resource partners of the Administration so that those resource partners can assist in amplifying public awareness regarding relevant information needed by disaster loan applicants. ; and\n**(3)**\nby amending section 40(a)(2)(D) ( 15 U.S.C. 657l(a)(2)(D) ) to read as follows:\n(D) guidelines pursuant to which the Administration will coordinate with other Federal agencies, State, local, and regional authorities, and resource partners of the Administration to best respond to the demand described in subparagraph (B) and to best use the resources described in that subparagraph. .\n##### (b) Disaster planning coordination\nSection 12073(c) of the Small Business Disaster Response and Loan Improvements Act of 2008 ( 15 U.S.C. 636h(c) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking and at the end;\n**(2)**\nby redesignating paragraph (3) as paragraph (4); and\n**(3)**\nby inserting after paragraph (2) the following:\n(3) resource partners of the Administration; and .",
      "versionDate": "2025-05-08",
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
        "name": "Commerce",
        "updateDate": "2025-05-29T15:28:22Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1698is.xml"
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
      "title": "Small Business Disaster Coordination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Small Business Disaster Coordination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Disaster Response and Loan Improvements Act of 2008 to require the Small Business Administration to coordinate with resource partners with respect to disaster planning activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:36Z"
    }
  ]
}
```
