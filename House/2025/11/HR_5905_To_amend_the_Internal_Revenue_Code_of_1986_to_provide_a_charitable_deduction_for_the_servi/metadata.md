# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5905?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5905
- Title: Helping Our Heroes Act
- Congress: 119
- Bill type: HR
- Bill number: 5905
- Origin chamber: House
- Introduced date: 2025-11-04
- Update date: 2025-12-31T09:05:17Z
- Update date including text: 2025-12-31T09:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-04: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-04: Introduced in House

## Actions

- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5905",
    "number": "5905",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001327",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
        "lastName": "Bresnahan",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Helping Our Heroes Act",
    "type": "HR",
    "updateDate": "2025-12-31T09:05:17Z",
    "updateDateIncludingText": "2025-12-31T09:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-04",
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
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-04",
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
          "date": "2025-11-04T19:02:00Z",
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
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-30",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5905ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5905\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Mr. Bresnahan (for himself and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a charitable deduction for the service of volunteer firefighters and emergency medical and rescue personnel.\n#### 1. Short title\nThis Act may be cited as the Helping Our Heroes Act .\n#### 2. Allowance of charitable deduction for the service of volunteer firefighters and emergency medical and rescue personnel\n##### (a) In general\nSection 170 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby redesignating subsection (q) as subsection (r), and\n**(2)**\nby inserting after subsection (p) the following new subsection:\n(q) Service of volunteer firefighters and emergency medical personnel treated as charitable contribution (1) In general Each hour of qualified services rendered by an individual as a bona fide volunteer shall be treated for purposes of this section as a contribution of $20 to the organization to which such services are rendered. (2) Limitation Not more than 300 hours of qualified services shall be taken into account under paragraph (1) with respect to any individual for any taxable year. (3) Definitions For purposes of this subsection\u2014 (A) Bona fide volunteer An individual shall be treated as a bona fide volunteer if the only compensation received by such individual for performing qualified services is in the form of\u2014 (i) reimbursement for (or a reasonable allowance for) reasonable expenses incurred in the performance of such services, or (ii) reasonable benefits (including length of service awards), and fees for such services, customarily paid by eligible employers in connection with the performance of such services by volunteers. (B) Qualified services The term qualified services means fire fighting and prevention services, emergency medical and rescue services, ambulance services, civil air patrol, and search and rescue services. Such term shall include all training and training-related activities related to the services described in the preceding sentence which are required or authorized by the organization referred to in paragraph (1). (4) Verification A contribution to which this subsection applies shall be verified in such manner as the Secretary may provide. (5) Inflation adjustment In the case of any taxable year beginning in a calendar year after 2026, the $20 amount contained in paragraph (1) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. Any increase determined under the preceding sentence which is not a multiple of $1 shall be rounded to the nearest multiple of $1. (6) Exclusion for Members of Congress Services rendered during any period with respect to which such individual is a Member of Congress (as defined in section 2106 of title 5, United States Code) shall not be treated as qualified services for purposes of this subsection. .\n##### (b) Allowance of deduction to individuals who do not elect To itemize deductions\nSection 63(b) of such Code is amended by striking paragraph (4) and inserting the following new paragraph:\n(4) so much of the deduction allowed under section 170 for the taxable year as does not exceed the amount of such deduction which would be determined if only contributions treated as made under section 170(q) by reason of services rendered during such taxable year were taken into account. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-11-04",
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
        "updateDate": "2025-11-20T17:53:01Z"
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
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5905ih.xml"
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
      "title": "Helping Our Heroes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Helping Our Heroes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a charitable deduction for the service of volunteer firefighters and emergency medical and rescue personnel.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T04:48:17Z"
    }
  ]
}
```
