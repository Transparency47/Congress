# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2621?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2621
- Title: A bill to amend the Public Health Service Act to reauthorize support for State-based maternal mortality review committees, to direct the Secretary of Health and Human Services to disseminate best practices on maternal mortality prevention to hospitals, State-based professional societies, and perinatal quality collaboratives, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 2621
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-01-29T11:56:24Z
- Update date including text: 2026-01-29T11:56:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2621",
    "number": "2621",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001047",
        "district": "",
        "firstName": "Shelley",
        "fullName": "Sen. Capito, Shelley Moore [R-WV]",
        "lastName": "Capito",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "A bill to amend the Public Health Service Act to reauthorize support for State-based maternal mortality review committees, to direct the Secretary of Health and Human Services to disseminate best practices on maternal mortality prevention to hospitals, State-based professional societies, and perinatal quality collaboratives, and for other purposes.",
    "type": "S",
    "updateDate": "2026-01-29T11:56:24Z",
    "updateDateIncludingText": "2026-01-29T11:56:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
            "date": "2025-07-31T20:09:59Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-31T20:09:59Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "GA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "KS"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NJ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "NC"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "FL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-10-16",
      "state": "ME"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "AR"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "VA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "DE"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "MD"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2621is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2621\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mrs. Capito (for herself, Mr. Warnock , Mr. Marshall , Mr. Booker , Ms. Smith , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to reauthorize support for State-based maternal mortality review committees, to direct the Secretary of Health and Human Services to disseminate best practices on maternal mortality prevention to hospitals, State-based professional societies, and perinatal quality collaboratives, and for other purposes.\n#### 1. Preventing maternal deaths\n##### (a) Maternal mortality review committee\nSection 317K(d) of the Public Health Service Act ( 42 U.S.C. 247b\u201312(d) ) is amended\u2014\n**(1)**\nin paragraph (1)(A), by inserting (including obstetricians and gynecologists) after clinical specialties ; and\n**(2)**\nin paragraph (3)(A)(i)\u2014\n**(A)**\nin subclause (I), by striking as applicable and inserting if available ; and\n**(B)**\nin subclause (III), by striking , as appropriate and inserting and coordinating with death certifiers to improve the collection of death record reports and the quality of death records, including by amending cause-of-death information on a death certificate, as appropriate .\n##### (b) Best practices relating to the prevention of maternal mortality\nSection 317K of the Public Health Service Act ( 42 U.S.C. 247b\u201312 ) is amended\u2014\n**(1)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively; and\n**(2)**\nby inserting after subsection (d) the following:\n(e) Best practices relating to the prevention of maternal mortality (1) In general The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall, in consultation with the Administrator of the Health Resources and Services Administration, disseminate to hospitals, State professional society groups, and perinatal quality collaboratives, best practices on how to prevent maternal mortality and morbidity that consider and reflect best practices identified through other relevant Federal maternal health programs. (2) Frequency The Secretary, acting through the Director of the Centers for Disease Control and Prevention, shall disseminate the best practices referred to in paragraph (1) not less frequently than once per fiscal year. .\n##### (c) Extension\nSubsection (g) of section 317K of the Public Health Service Act ( 42 U.S.C. 247b\u201312 ), as redesignated by subsection (b), is amended by striking $58,000,000 for each of fiscal years 2019 through 2023 and inserting $100,000,000 for each of fiscal years 2026 through 2030 .",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-03-06",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1909",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Preventing Maternal Deaths Reauthorization Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
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
        "updateDate": "2025-09-18T18:05:48Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2621is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to reauthorize support for State-based maternal mortality review committees, to direct the Secretary of Health and Human Services to disseminate best practices on maternal mortality prevention to hospitals, State-based professional societies, and perinatal quality collaboratives, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:52Z"
    },
    {
      "title": "A bill to amend the Public Health Service Act to reauthorize support for State-based maternal mortality review committees, to direct the Secretary of Health and Human Services to disseminate best practices on maternal mortality prevention to hospitals, State-based professional societies, and perinatal quality collaboratives, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T10:56:31Z"
    }
  ]
}
```
