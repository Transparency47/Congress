# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4000?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4000
- Title: Securing Infrastructure from Adversaries Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4000
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-03-24T19:46:04Z
- Update date including text: 2026-03-24T19:46:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4000",
    "number": "4000",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Securing Infrastructure from Adversaries Act of 2026",
    "type": "S",
    "updateDate": "2026-03-24T19:46:04Z",
    "updateDateIncludingText": "2026-03-24T19:46:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T17:00:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "WI"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "AR"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4000is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4000\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Budd (for himself, Ms. Baldwin , Mr. Cotton , and Ms. Blunt Rochester ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit the Secretary of Transportation from entering into, extending, or renewing a contract with, or awarding a grant to, an entity that uses or procures light detection and ranging technology from certain foreign entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Infrastructure from Adversaries Act of 2026 .\n#### 2. Prohibition on use of, procurement of, and contracting related to certain foreign-made LiDAR technology\n##### (a) Definitions\nIn this section:\n**(1) Covered foreign country; covered LiDAR company; covered LiDAR technology; LiDAR**\nThe terms covered foreign country , covered LiDAR company , covered LiDAR technology , and LiDAR have the meanings given those terms in section 164(e) of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 (10 U.S.C. note prec. 4651; Public Law 118\u2013159 ).\n**(2) Secretary**\nThe term Secretary means the Secretary of Transportation.\n##### (b) Prohibition on use or procurement of certain LiDAR\n**(1) In general**\nThe Secretary may not\u2014\n**(A)**\nprocure or obtain\u2014\n**(i)**\nany covered LiDAR technology;\n**(ii)**\nany LiDAR technology otherwise produced or provided by a covered LiDAR company; or\n**(iii)**\nany LiDAR technology produced in or provided by a covered foreign country; or\n**(B)**\nenter into, extend, or renew a contract with any entity unless the entity submits to the Secretary a certification that no covered LiDAR technology and no LiDAR technology described in clause (ii) or (iii) of subparagraph (A) will be used in the performance of the contract.\n**(2) Waiver**\nThe Secretary may waive the prohibition under paragraph (1) on a case-by-case basis by submitting to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives, not later than 15 days before the applicable activity is carried out, a written certification that the activity to which that prohibition applies and for which a waiver will be provided is in the national interest of the United States.\n##### (c) Prohibition on use of loan or grant funds for certain LiDAR\nIn entering into an agreement with an entity under which the Secretary provides loan or grant funds to that entity, the Secretary shall ensure that no such funds may be obligated or expended to procure, obtain, or use\u2014\n**(1)**\nany covered LiDAR technology;\n**(2)**\nany LiDAR technology otherwise produced or provided by a covered LiDAR company; or\n**(3)**\nany LiDAR technology produced in or provided by a covered foreign country.\n##### (d) Applicability\n**(1) In general**\nSubject to paragraph (2), this section shall apply to any obligation or expenditure of funds, and any contract entered into, on or after June 30, 2026.\n**(2) Limitation**\nThis section shall not apply to\u2014\n**(A)**\nany application for an exemption from a Federal motor vehicle safety standard prescribed under section 30111 of title 49, United States Code;\n**(B)**\nany application for a waiver of, or an exemption from, a Federal motor carrier safety regulation prescribed under section 31136 of title 49, United States Code; or\n**(C)**\nany grant, operation, procurement, or contracting action that is for the purposes of any testing, research, evaluation, analysis, or training relating to vehicle safety.",
      "versionDate": "2026-03-05",
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
        "actionDate": "2025-12-01",
        "text": "Referred to the Subcommittee on Highways and Transit."
      },
      "number": "4802",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Securing Infrastructure from Adversaries Act of 2025",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-03-24T19:46:03Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4000is.xml"
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
      "title": "Securing Infrastructure from Adversaries Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing Infrastructure from Adversaries Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Secretary of Transportation from entering into, extending, or renewing a contract with, or awarding a grant to, an entity that uses or procures light detection and ranging technology from certain foreign entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:03:26Z"
    }
  ]
}
```
