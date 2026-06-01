# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6050?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6050
- Title: HEALTH Act
- Congress: 119
- Bill type: HR
- Bill number: 6050
- Origin chamber: House
- Introduced date: 2025-11-17
- Update date: 2026-01-22T17:41:04Z
- Update date including text: 2026-01-22T17:41:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-17: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-17: Introduced in House

## Actions

- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-17",
    "latestAction": {
      "actionDate": "2025-11-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6050",
    "number": "6050",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001066",
        "district": "4",
        "firstName": "Steven",
        "fullName": "Rep. Horsford, Steven [D-NV-4]",
        "lastName": "Horsford",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "HEALTH Act",
    "type": "HR",
    "updateDate": "2026-01-22T17:41:04Z",
    "updateDateIncludingText": "2026-01-22T17:41:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-17",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-17",
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
          "date": "2025-11-17T17:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-17T17:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "IL"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "VI"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "MI"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "AL"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "HI"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6050ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6050\nIN THE HOUSE OF REPRESENTATIVES\nNovember 17, 2025 Mr. Horsford (for himself, Ms. Barrag\u00e1n , Ms. Kelly of Illinois , Ms. Plaskett , Ms. Scholten , Ms. Sewell , and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Appropriations , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend certain provisions of the health insurance premium tax credit, to rescind unobligated balances for providing assistance to Argentina, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Every American Lower Their Healthcare Act or the HEALTH Act .\n#### 2. Extension of health insurance premium tax credit provisions\n##### (a) Extension of rule To allow credit to taxpayers whose household income exceeds 400 percent of poverty line\nSubparagraph (E) of section 36B(c)(1) of the Internal Revenue Code of 1986 is amended to read as follows:\n(E) Temporary rule (i) In general In the case of a taxable year beginning before the applicable date, subparagraph (A) shall be applied without regard to but does not exceed 400 percent . (ii) Applicable date For purposes of clause (i), the term applicable date means the latest date which the Secretary estimates will result in\u2014 (I) the sum of the increase in outlays, and the reduction in revenues, of the Federal Government by reason of this subparagraph and subsection (b)(3)(A)(iii), not exceeding (II) the decrease in outlays of the Federal Government by reason of section 3 of the Helping Every American Lower Their Healthcare Act . (iii) Method of estimation To the maximum extent practicable, the estimates of the Secretary under clause (ii) shall be made in the same manner as such estimates are made by the Congressional Budget Office and the Joint Committee on Taxation with respect to proposed legislation. .\n##### (b) Extension of rules To increase premium assistance amounts\nClause (iii) of section 36B(b)(3)(A) of such Code is amended\u2014\n**(1)**\nin the heading, by striking for 2021 through 2025 , and\n**(2)**\nin the matter preceding subclause (I), by striking January 1, 2026 and inserting the applicable date (as defined in subsection (c)(1)(E)) .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Rescission of unobligated balances for providing assistance to Argentina\nEffective on the date of the enactment of this Act, the unobligated balances of any amounts appropriated or otherwise made available for providing assistance to Argentina are rescinded.",
      "versionDate": "2025-11-17",
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
        "actionDate": "2025-11-21",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "6246",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Save American Healthcare Act",
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
        "name": "Taxation",
        "updateDate": "2026-01-21T16:01:59Z"
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
      "date": "2025-11-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6050ih.xml"
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
      "title": "HEALTH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEALTH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Every American Lower Their Healthcare Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to extend certain provisions of the health insurance premium tax credit, to rescind unobligated balances for providing assistance to Argentina, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:39Z"
    }
  ]
}
```
