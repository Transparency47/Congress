# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5225?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5225
- Title: Protect Innocent Victims of Taxation After Fire Extension Act
- Congress: 119
- Bill type: HR
- Bill number: 5225
- Origin chamber: House
- Introduced date: 2025-09-09
- Update date: 2026-04-14T19:59:32Z
- Update date including text: 2026-04-14T19:59:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-09: Introduced in House

## Actions

- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5225",
    "number": "5225",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000578",
        "district": "1",
        "firstName": "Doug",
        "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
        "lastName": "LaMalfa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Protect Innocent Victims of Taxation After Fire Extension Act",
    "type": "HR",
    "updateDate": "2026-04-14T19:59:32Z",
    "updateDateIncludingText": "2026-04-14T19:59:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-09",
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
      "actionDate": "2025-09-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T14:04:10Z",
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
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "OR"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "OR"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "UT"
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
      "sponsorshipDate": "2025-09-26",
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
      "sponsorshipDate": "2025-10-08",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5225ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5225\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 9, 2025 Mr. LaMalfa (for himself, Mr. Thompson of California , Mr. McClintock , Mr. Sherman , Mr. Bentz , Ms. Bynum , and Mr. Moore of Utah ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude qualified wildfire relief payments from gross income, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Innocent Victims of Taxation After Fire Extension Act .\n#### 2. Exclusion from gross income for compensation for losses or damages resulting from wildfires\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139L the following new section:\n139M. Compensation for losses or damages resulting from wildfires (a) In general Gross income shall not include any amount received by an individual as a qualified wildfire relief payment. (b) Qualified wildfire relief payment For purposes of this section\u2014 (1) In general The term qualified wildfire relief payment means any amount received by or on behalf of an individual as compensation for losses, expenses, or damages (including compensation for additional living expenses, lost wages (other than compensation for lost wages paid by the employer which would have otherwise paid such wages), personal injury, death, or emotional distress) incurred as a result of a qualified wildfire disaster, but only to the extent the losses, expenses, or damages compensated by such payment are not compensated for by insurance or otherwise. (2) Qualified wildfire disaster The term qualified wildfire disaster means any federally declared disaster (as defined in section 165(i)(5)(A)) declared, after December 31, 2014, as a result of any forest or range fire. (c) Denial of double benefit Notwithstanding any other provision of this subtitle\u2014 (1) no deduction or credit shall be allowed (to the individual for whose benefit a qualified wildfire relief payment is made) for, or by reason of, any expenditure to the extent of the amount excluded under this section with respect to such expenditure, and (2) no increase in the basis or adjusted basis of any property shall result from any amount excluded under this section with respect to such property. (d) Termination Subsection (a) shall not apply to amounts received after December 31, 2032. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139L the following new item:\nSec. 139M. Compensation for losses or damages resulting from wildfires. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts received after December 31, 2025.",
      "versionDate": "2025-09-09",
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
        "actionDate": "2026-03-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7825",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Doug LaMalfa Protect Innocent Victims of Taxation After Fire Extension Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-09",
        "text": "Placed on the Union Calendar, Calendar No. 525."
      },
      "number": "5366",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Doug LaMalfa Federal Disaster Tax Relief Certainty Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2744",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Federal Disaster Tax Relief Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-04",
        "text": "Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S8514)"
      },
      "number": "3372",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Innocent Victims of Taxation After Fire Extension Act",
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
        "name": "Taxation",
        "updateDate": "2025-09-16T21:58:09Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5225ih.xml"
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
      "title": "Protect Innocent Victims of Taxation After Fire Extension Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Innocent Victims of Taxation After Fire Extension Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-16T04:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude qualified wildfire relief payments from gross income, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-16T04:48:18Z"
    }
  ]
}
```
