# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4981?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4981
- Title: Stamp Out Lyme Disease Act
- Congress: 119
- Bill type: HR
- Bill number: 4981
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2026-05-13T08:06:42Z
- Update date including text: 2026-05-13T08:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-15 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-15: Introduced in House

## Actions

- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-15 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4981",
    "number": "4981",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Stamp Out Lyme Disease Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:42Z",
    "updateDateIncludingText": "2026-05-13T08:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-15T16:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NE"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "DC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "IN"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "RI"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "VA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4981ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4981\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Mr. Gottheimer (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for the issuance of a Lyme Disease Research Semipostal Stamp.\n#### 1. Short title\nThis Act may be cited as the Stamp Out Lyme Disease Act .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe Centers for Disease Control and Prevention (CDC) estimate that 476,000 Lyme disease cases are diagnosed and treated in the United States annually.\n**(2)**\nThe CDC reports that Lyme disease is difficult to diagnose due to its diverse manifestations and a lack of reliable testing options.\n**(3)**\nThe National Institutes of Health (NIH) reports that a significant number of later-stage or post-treatment Lyme disease patients are not cured.\n**(4)**\nThe Tick-Borne Disease Working Group reports that 10 to 20 percent of Lyme disease patients will suffer from persistent symptoms which can be chronic and disabling.\n**(5)**\nAccording to the Johns Hopkins Bloomberg School of Public Health, Lyme disease costs the United States healthcare system up to $1,300,000,000 per year.\n##### (b) Purpose\nTo afford a convenient way for members of the public to contribute to funding for Lyme disease and related tick-borne illness research within the National Institute of Allergy and Infectious Diseases, the United States Postal Service shall issue a semipostal stamp (hereinafter in this Act referred to as the Lyme Disease Research Semipostal Stamp ) in accordance with this section.\n#### 3. Lyme disease research semipostal stamp\n##### (a) Terms and conditions\nThe issuance and sale of the Lyme Disease Research Semipostal Stamp shall be governed by the provisions of section 416 of title 39, United States Code, and regulations issued under such section.\n##### (b) Disposition of proceeds\n**(1) In general**\nAll amounts becoming available from the sale of the Lyme Disease Research Semipostal Stamp (as determined under section 416(d) of such title 39) shall be transferred to the National Institute of Allergy and Infectious Diseases, for the purpose described in subsection (a), through payments which shall be made at least twice a year.\n**(2) Proceeds not to be offset**\nIn accordance with section 416(d)(4) of such title 39, amounts becoming available from the sale of the Lyme Disease Research Semipostal Stamp (as so determined) shall not be taken into account in any decision relating to the level of appropriations or other Federal funding to be furnished in any year to the National Institute of Allergy and Infectious Diseases.\n##### (c) Duration\nThe Lyme Disease Research Semipostal Stamp shall be made available to the public for a period of at least 6 years, beginning no later than 12 months after the date of the enactment of this Act.\n##### (d) Definition\nFor purposes of this Act, the term semipostal stamp refers to a stamp described in section 416(a)(1) of title 39, United States Code.",
      "versionDate": "2025-08-15",
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
        "name": "Health",
        "updateDate": "2025-09-19T15:33:35Z"
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
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4981ih.xml"
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
      "title": "Stamp Out Lyme Disease Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-19T06:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stamp Out Lyme Disease Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-19T06:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the issuance of a Lyme Disease Research Semipostal Stamp.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-19T06:33:23Z"
    }
  ]
}
```
