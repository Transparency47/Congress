# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4262?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4262
- Title: To reauthorize programs related to health professions education, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 4262
- Origin chamber: House
- Introduced date: 2025-06-30
- Update date: 2025-09-16T14:13:50Z
- Update date including text: 2025-09-16T14:13:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-30: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-10 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-09-10 - Committee: Referred to the Subcommittee on Health.
- 2025-09-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-06-30: Introduced in House

## Actions

- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Introduced in House
- 2025-06-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-10 - Committee: Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.
- 2025-09-10 - Committee: Referred to the Subcommittee on Health.
- 2025-09-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-30",
    "latestAction": {
      "actionDate": "2025-06-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4262",
    "number": "4262",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "To reauthorize programs related to health professions education, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-09-16T14:13:50Z",
    "updateDateIncludingText": "2025-09-16T14:13:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-30",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-30",
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
          "date": "2025-06-30T18:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-09-10T17:49:44Z",
                "name": "Reported by"
              },
              {
                "date": "2025-09-10T17:42:41Z",
                "name": "Markup by"
              },
              {
                "date": "2025-09-10T17:42:07Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4262ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4262\nIN THE HOUSE OF REPRESENTATIVES\nJune 30, 2025 Ms. Schakowsky introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo reauthorize programs related to health professions education, and for other purposes.\n#### 1. Reauthorization of programs related to health professions education\n##### (a) Centers of excellence\nSection 736(i) of the Public Health Service Act ( 42 U.S.C. 293(i) ) is amended by striking appropriated and all that follows through the period at the end and inserting appropriated $28,422,000 for each of fiscal years 2026 through 2030. .\n##### (b) Scholarships for disadvantaged students\nSection 740(a) of the Public Health Service Act ( 42 U.S.C. 293d(a) ) is amended by striking section 737 and all that follows through 2025. and inserting section 737, $55,014,000 for each of fiscal years 2026 through 2030. .\n##### (c) Loan repayments and fellowships regarding faculty positions\nSection 740(b) of the Public Health Service Act ( 42 U.S.C. 293d(b) ) is amended by striking appropriated and all that follows through the period at the end and inserting appropriated, $2,310,000 for each of fiscal years 2026 through 2030. .\n##### (d) Educational assistance in health professions regarding individuals for disadvantaged backgrounds\nSection 740(c) of the Public Health Service Act ( 42 U.S.C. 293d(c) ) is amended by striking authorized to be appropriated and all that follows through 2025. and inserting authorized to be appropriated $16,000,000 for each of fiscal years 2026 through 2030. .\n##### (e) Primary care training and enhancement\nSection 747(c)(1) of the Public Health Service Act ( 42 U.S.C. 293k(c)(1) ) is amended by striking appropriated and all that follows through the period at the end and inserting appropriated $49,924,000 for each of fiscal years 2026 through 2030. .\n##### (f) Training in general, pediatric, and public health dentistry\nSection 748(f) of the Public Health Service Act ( 42 U.S.C. 293k\u20132(f) ) is amended by striking appropriated and all that follows through the period at the end and inserting appropriated $42,673,000 for each of fiscal years 2026 through 2030. .\n##### (g) Area health education centers\nSection 751(j)(1) of the Public Health Service Act ( 42 U.S.C. 294a(j)(1) ) is amended by striking section and all that follows through the period at the end and inserting section $47,000,000 for each of fiscal years 2026 through 2030. .\n##### (h) Education and training relating to geriatrics\nSection 753(d) of the Public Health Service Act ( 42 U.S.C. 294c(d) ) is amended by striking appropriated and all that follows through the period at the end and inserting appropriated $48,245,000 for each of fiscal years 2026 through 2030 for purposes of carrying out this section. .\n##### (i) National Center for Health Care Workforce Analysis\nSection 761(e)(1)(A) of the Public Health Service Act ( 42 U.S.C. 294n(e)(1)(A) ) is amended by striking 2021 through 2025 and inserting 2026 through 2030 .\n##### (j) Public health workforce development\nSection 770(a) of the Public Health Service Act ( 42 U.S.C. 295e(a) ) is amended by striking appropriated and all that follows through the period at the end and inserting appropriated $18,000,000 for each of fiscal years 2026 through 2030. .\n##### (k) Pediatric specialty loan repayment program\nSection 775(e) of the Public Health Service Act ( 42 U.S.C. 295f(e) ) is amended by striking appropriated and all that follows through the period at the end and inserting appropriated to carry out this section $10,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-06-30",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Aging",
            "updateDate": "2025-09-16T14:13:37Z"
          },
          {
            "name": "Child health",
            "updateDate": "2025-09-16T14:13:41Z"
          },
          {
            "name": "Dental care",
            "updateDate": "2025-09-16T14:13:45Z"
          },
          {
            "name": "Education of the disadvantaged",
            "updateDate": "2025-09-16T14:13:50Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-09-16T14:13:19Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-09-16T14:13:29Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-09-16T14:13:04Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-09-16T14:13:14Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-09-16T14:13:34Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-09-16T14:13:09Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-09-16T14:13:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-07-30T13:55:15Z"
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
      "date": "2025-06-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4262ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize programs related to health professions education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T04:31:28Z"
    },
    {
      "title": "To reauthorize programs related to health professions education, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:32Z"
    }
  ]
}
```
