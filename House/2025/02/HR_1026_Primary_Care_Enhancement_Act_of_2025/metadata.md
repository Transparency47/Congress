# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1026?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1026
- Title: Primary Care Enhancement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1026
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-05-05T15:03:49Z
- Update date including text: 2025-05-05T15:03:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1026",
    "number": "1026",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Primary Care Enhancement Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-05T15:03:49Z",
    "updateDateIncludingText": "2025-05-05T15:03:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:02:00Z",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NY"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "TX"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "WA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "PA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "IL"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1026ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1026\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Smucker (for himself, Ms. Tenney , Mr. Schneider , Mr. Panetta , Mr. Crenshaw , and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow individuals with direct primary care service arrangements to remain eligible individuals for purposes of health savings accounts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Primary Care Enhancement Act of 2025 .\n#### 2. Treatment of direct primary care service arrangements\n##### (a) In general\nSection 223(c)(1) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(E) Treatment of direct primary care service arrangements (i) In general A direct primary care service arrangement shall not be treated as a health plan for purposes of subparagraph (A)(ii). (ii) Direct primary care service arrangement For purposes of this paragraph\u2014 (I) In general The term direct primary care service arrangement means, with respect to any individual, an arrangement under which such individual is provided medical care (as defined in section 213(d)) consisting solely of primary care services provided by primary care practitioners (as defined in section 1833(x)(2)(A) of the Social Security Act, determined without regard to clause (ii) thereof), if the sole compensation for such care is a fixed periodic fee. (II) Limitation With respect to any individual for any month, such term shall not include any arrangement if the aggregate fees for all direct primary care service arrangements (determined without regard to this subclause) with respect to such individual for such month exceed $150 (twice such dollar amount in the case of an individual with any direct primary care service arrangement (as so determined) that covers more than one individual). (iii) Certain services specifically excluded from treatment as primary care services For purposes of this paragraph, the term primary care services shall not include\u2014 (I) procedures that require the use of general anesthesia, (II) prescription drugs (other than vaccines), and (III) laboratory services not typically administered in an ambulatory primary care setting. The Secretary, after consultation with the Secretary of Health and Human Services, shall issue regulations or other guidance regarding the application of this clause. .\n##### (b) Direct primary care service arrangement fees treated as medical expenses\nSection 223(d)(2)(C) of such Code is amended by striking or at the end of clause (iii), by striking the period at the end of clause (iv) and inserting , or , and by adding at the end the following new clause:\n(v) any direct primary care service arrangement. .\n##### (c) Inflation adjustment\nSection 223(g)(1) of such Code is amended\u2014\n**(1)**\nby inserting , (c)(1)(D)(ii)(II), after (b)(2) each place it appears, and\n**(2)**\nin subparagraph (B), by inserting and (iii) after clause (ii) in clause (i), by striking and at the end of clause (i), by striking the period at the end of clause (ii) and inserting , and , and by inserting after clause (ii) the following new clause:\n(iii) in the case of the dollar amount in subsection (c)(1)(D)(ii)(II) for taxable years beginning in calendar years after 2026, calendar year 2025 . .\n##### (d) Reporting of direct primary care service arrangement fees on W\u20132\nSection 6051(a) of such Code is amended by striking and at the end of paragraph (16), by striking the period at the end of paragraph (17) and inserting , and , and by inserting after paragraph (17) the following new paragraph:\n(18) in the case of a direct primary care service arrangement (as defined in section 223(c)(1)(D)(ii)) which is provided in connection with employment, the aggregate fees for such arrangement for such employee. .\n##### (e) Effective date\nThe amendments made by this section shall apply to months beginning after December 31, 2025, in taxable years ending after such date.",
      "versionDate": "2025-02-05",
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
        "name": "Taxation",
        "updateDate": "2025-05-05T15:03:49Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1026ih.xml"
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
      "title": "Primary Care Enhancement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Primary Care Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T13:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow individuals with direct primary care service arrangements to remain eligible individuals for purposes of health savings accounts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T13:18:27Z"
    }
  ]
}
```
