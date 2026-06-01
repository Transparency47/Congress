# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6445?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6445
- Title: Fast Track Healthcare Apprenticeships Act
- Congress: 119
- Bill type: HR
- Bill number: 6445
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-01-06T15:25:59Z
- Update date including text: 2026-01-06T15:25:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-12-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H5030-5031)
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-12-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H5030-5031)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6445",
    "number": "6445",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000310",
        "district": "32",
        "firstName": "Julie",
        "fullName": "Rep. Johnson, Julie [D-TX-32]",
        "lastName": "Johnson",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Fast Track Healthcare Apprenticeships Act",
    "type": "HR",
    "updateDate": "2026-01-06T15:25:59Z",
    "updateDateIncludingText": "2026-01-06T15:25:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H5030-5031)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6445ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6445\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Ms. Johnson of Texas (for herself and Mr. Kennedy of Utah ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo clarify the time period for registering health care apprenticeships under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ) and require the digitization of apprenticeship agreement forms under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fast Track Healthcare Apprenticeships Act .\n#### 2. Health care apprenticeship registration\nThe Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 4 as section 6; and\n**(2)**\nby inserting after section 3 the following:\n4. Health care apprenticeship registration (a) In general In administering this Act, the Secretary of Labor shall establish a national apprenticeship system that provides, with respect to any application submitted seeking to register a program in the health care field as an apprenticeship program under this Act, that\u2014 (1) a decision shall be provided to the applicant on the application not later than 45 days after receipt of the application; and (2) if a decision is not made within the 45 days after receipt, a written explanation for the delay and an estimated timeline for a determination (that is not more than 90 days after the date of such written explanation) shall be provided to the applicant. (b) Definitions In this section: (1) Health care field The term health care field means the following occupations: (A) Healthcare practitioners and technical occupations, as described in the Bureau of Labor Statistics Standard Occupational Classification System (or any corresponding occupation in any corresponding System). (B) Healthcare support occupations, as described in such System (or any corresponding occupation in any corresponding System). (2) National apprenticeship system The term national apprenticeship system means the system established by the Secretary of Labor to carry out the activities authorized and directed to be carried out under section 1. .\n#### 3. Digitization of apprenticeship agreement forms\nThe Act of August 16, 1937 (commonly known as the National Apprenticeship Act ; 50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ), as amended by section 2, is further amended by inserting after section 4 (as added by section 2) the following:\n5. Digitization of apprenticeship agreement forms In administering this Act, the Secretary of Labor shall establish a national apprenticeship system (as such term is defined in section 4) that provides that any apprenticeship agreement form for such system (including any employer agreement form or any disability disclosure form) shall be digitized. .",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-12-04",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3364",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Fast Track Healthcare Apprenticeships Act",
      "type": "S"
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
        "updateDate": "2026-01-06T15:25:33Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6445ih.xml"
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
      "title": "Fast Track Healthcare Apprenticeships Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-24T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fast Track Healthcare Apprenticeships Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-24T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To clarify the time period for registering health care apprenticeships under the Act of August 16, 1937 (commonly known as the \"National Apprenticeship Act\") and require the digitization of apprenticeship agreement forms under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-24T04:03:19Z"
    }
  ]
}
```
