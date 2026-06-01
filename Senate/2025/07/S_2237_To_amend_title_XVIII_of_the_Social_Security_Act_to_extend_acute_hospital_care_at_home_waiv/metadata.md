# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2237?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2237
- Title: Hospital Inpatient Services Modernization Act
- Congress: 119
- Bill type: S
- Bill number: 2237
- Origin chamber: Senate
- Introduced date: 2025-07-10
- Update date: 2026-02-05T17:34:23Z
- Update date including text: 2026-02-05T17:34:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in Senate
- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-10: Introduced in Senate

## Actions

- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2237",
    "number": "2237",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Hospital Inpatient Services Modernization Act",
    "type": "S",
    "updateDate": "2026-02-05T17:34:23Z",
    "updateDateIncludingText": "2026-02-05T17:34:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T14:47:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sponsorshipDate": "2025-07-10",
      "state": "GA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TN"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "RI"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "ID"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2237is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2237\nIN THE SENATE OF THE UNITED STATES\nJuly 10, 2025 Mr. Scott of South Carolina (for himself, Mr. Warnock , Mr. Tillis , Ms. Smith , Mrs. Blackburn , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to extend acute hospital care at home waiver flexibilities, and to require an additional study and report on such flexibilities.\n#### 1. Short title\nThis Act may be cited as the Hospital Inpatient Services Modernization Act .\n#### 2. Extending acute hospital care at home waiver flexibilities\nSection 1866G(a)(1) of the Social Security Act ( 42 U.S.C. 1395cc\u20137(a)(1) ) is amended by striking 2025 and inserting 2030 .\n#### 3. Requiring additional study and report on acute hospital care at home waiver flexibilities\nSection 1866G of the Social Security Act ( 42 U.S.C. 1395cc\u20137 ), as amended by section 2, is further amended\u2014\n**(1)**\nin subsection (b), in the subsection heading, by striking Study and inserting Initial study ;\n**(2)**\nby redesignating subsections (c) and (d) as subsections (d) and (e), respectively; and\n**(3)**\nby inserting after subsection (b) the following new subsection:\n(c) Subsequent study and report (1) In general Not later than September 30, 2028, the Secretary shall conduct a study to\u2014 (A) analyze, to the extent practicable, the criteria established by hospitals under the Acute Hospital Care at Home initiative to determine which individuals may be furnished services under such initiative; and (B) analyze and compare (both within and between hospitals participating in the initiative, and relative to comparable hospitals that do not participate in the initiative, for relevant parameters such as diagnosis-related groups)\u2014 (i) quality of care furnished to individuals with similar conditions and characteristics in the inpatient setting and through the Acute Hospital Care at Home initiative, including health outcomes, hospital readmission rates (including readmissions both within and beyond 30 days post-discharge), hospital mortality rates, length of stay, infection rates, composition of care team (including the types of labor used, such as contracted labor), the ratio of nursing staff, transfers from the hospital to the home, transfers from the home to the hospital (including the timing, frequency, and causes of such transfers), transfers and discharges to post-acute care settings (including the timing, frequency, and causes of such transfers and discharges), and patient and caregiver experience of care; (ii) clinical conditions treated and diagnosis-related groups of discharges from inpatient settings relative to discharges from the Acute Hospital Care at Home initiative; (iii) costs incurred by the hospital for furnishing care in inpatient settings relative to costs incurred by the hospital for furnishing care through the Acute Hospital Care at Home initiative, including costs relating to staffing, equipment, food, prescriptions, and other services, as determined by the Secretary; (iv) the quantity, mix, and intensity of services (such as in-person visits and virtual contacts with patients and the intensity of such services) furnished in inpatient settings relative to the Acute Hospital Care at Home initiative, and, to the extent practicable, the nature and extent of family or caregiver involvement; (v) socioeconomic information on individuals treated in comparable inpatient settings relative to the initiative, including racial and ethnic data, income, housing, geographic proximity to the brick-and-mortar facility and whether such individuals are dually eligible for benefits under this title and title XIX; and (vi) the quality of care, outcomes, costs, quantity and intensity of services, and other relevant metrics between individuals who entered into the Acute Hospital Care at Home initiative directly from an emergency department compared with individuals who entered into the Acute Hospital Care at Home initiative directly from an existing inpatient stay in a hospital. (2) Selection bias In conducting the study under paragraph (1), the Secretary shall, to the extent practicable, analyze and compare individuals who participate and do not participate in the initiative controlling for selection bias or other factors that may impact the reliability of data. (3) Report Not later than September 30, 2028, the Secretary of Health and Human Services shall submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a report on the study conducted under paragraph (1). .",
      "versionDate": "2025-07-10",
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
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-02",
        "text": "Received in the Senate and Read twice and referred to the Committee on Finance."
      },
      "number": "4313",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Hospital Inpatient Services Modernization Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-26T14:19:54Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-09-26T14:19:54Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-09-26T14:19:54Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-09-26T14:19:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-07-28T12:52:19Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2237is.xml"
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
      "title": "Hospital Inpatient Services Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:48:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Hospital Inpatient Services Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-17T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to extend acute hospital care at home waiver flexibilities, and to require an additional study and report on such flexibilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T02:18:17Z"
    }
  ]
}
```
