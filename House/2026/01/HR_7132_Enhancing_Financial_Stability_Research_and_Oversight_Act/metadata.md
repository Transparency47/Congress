# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7132
- Title: Enhancing Financial Stability Research and Oversight Act
- Congress: 119
- Bill type: HR
- Bill number: 7132
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-02-12T14:15:45Z
- Update date including text: 2026-02-12T14:15:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7132",
    "number": "7132",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Enhancing Financial Stability Research and Oversight Act",
    "type": "HR",
    "updateDate": "2026-02-12T14:15:45Z",
    "updateDateIncludingText": "2026-02-12T14:15:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "OH"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "NY"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7132ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7132\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mr. Foster (for himself, Mr. Sherman , Mrs. Beatty , Mr. Casten , and Ms. Vel\u00e1zquez ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Financial Stability Act of 2010 to preserve the independent funding in the Office of Financial Research, to establish minimum staffing levels for the Financial Stability Oversight Council, to establish minimum funding levels for such staff, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing Financial Stability Research and Oversight Act .\n#### 2. Preserving independent funding\nThe Financial Stability Act of 2010 ( 12 U.S.C. 5311 et seq. ) is amended\u2014\n**(1)**\nin section 152\u2014\n**(A)**\nby amending subsection (c) to read as follows:\n(c) Budget (1) In general The Director shall have sole discretion to establish the annual budget of the Office. (2) Minimum funding level of the budget The annual budget of the Office in any given fiscal year shall not be less than $124,627,000. (3) Adjustment of minimum funding level The dollar amount referred to in paragraph (2) shall be adjusted annually by the Director, using the percent increase (if any) in the employment cost index for total compensation for State and local government workers published by the Federal Government, or the successor index thereto, for the 12-month period ending September 30 of the year preceding the annual budget. ;\n**(B)**\nin subsection (d)\u2014\n**(i)**\nby striking , in consultation with the Chairperson, each place such term appears; and\n**(ii)**\nin paragraph (1), by striking may fix the number of, and appoint and inserting shall ensure that the Office has not less than 231 full-time equivalent positions, and may appoint ;\n**(C)**\nin subsection (h), by striking , in consultation with the Chairperson, ; and\n**(D)**\nin subsection (i), by striking , in consultation with the Chairperson, ; and\n**(2)**\nin section 155\u2014\n**(A)**\nin subsection (d), by inserting before the period the following: , as determined in the sole discretion of the Director ; and\n**(B)**\nby adding at the end the following:\n(e) Reviewability Notwithstanding any other provision of this subtitle, the funding pursuant to subsection (d) shall not be subject to review by the Committees on Appropriations of the House of Representatives and the Senate. (f) Preservation of the Office of Financial Research\u2019s independence Nothing in this section shall authorize the Secretary to influence the budget or the number or compensation of employees of the Office. .\n#### 3. Minimum FSOC staffing levels\n##### (a) Minimum staffing level\nSection 111 of the Financial Stability Act of 2010 ( 12 U.S.C. 5321 ) is amended by adding at the end the following:\n(k) Minimum staffing level The Chairperson of the Council shall ensure that the Council has not less than 48 full-time equivalent positions, not including any employees detailed pursuant to subsection (j). .\n##### (b) Minimum budget levels\nSection 118 of the Financial Stability Act of 2010 ( 12 U.S.C. 5328 ) is amended to read as follows:\n118. Council funding (a) In general The Office of Financial Research shall transfer to the Council the amount of funds necessary to pay for the expenses of the Council, and the Council may immediately use such funds. (b) Minimum budget The Office of Financial Research shall transfer not less than $15,287,000 to the Council each year to pay for the staffing and other expenses of the Council, including for the office of the independent member of the Council described under section 111(b)(1)(J). Such dollar amount shall be adjusted annually by the Chairperson of the Council, using the percent increase (if any) in the employment cost index for total compensation for State and local government workers published by the Federal Government, or the successor index thereto, for the 12-month period ending September 30 of the previous year. .",
      "versionDate": "2026-01-16",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-02-12T14:15:45Z"
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
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7132ih.xml"
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
      "title": "Enhancing Financial Stability Research and Oversight Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T13:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Enhancing Financial Stability Research and Oversight Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T13:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Financial Stability Act of 2010 to preserve the independent funding in the Office of Financial Research, to establish minimum staffing levels for the Financial Stability Oversight Council, to establish minimum funding levels for such staff, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T13:03:37Z"
    }
  ]
}
```
