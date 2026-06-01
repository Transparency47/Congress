# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7581?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7581
- Title: LOVE Act
- Congress: 119
- Bill type: HR
- Bill number: 7581
- Origin chamber: House
- Introduced date: 2026-02-13
- Update date: 2026-05-27T08:05:47Z
- Update date including text: 2026-05-27T08:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-13: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-13 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-13: Introduced in House

## Actions

- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Introduced in House
- 2026-02-13 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-13 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-13",
    "latestAction": {
      "actionDate": "2026-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7581",
    "number": "7581",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "LOVE Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:05:47Z",
    "updateDateIncludingText": "2026-05-27T08:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-13",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-13",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-13",
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
          "date": "2026-02-13T15:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-13T15:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "OR"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7581ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7581\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2026 Ms. Malliotakis (for herself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to establish a demonstration program to provide payment under the Medicare program for living kidney donor transplant facilitator training.\n#### 1. Short title\nThis Act may be cited as the Living Organ Volunteer Engagement Act or the LOVE Act .\n#### 2. Medicare demonstration program to provide payment for living kidney donor transplant facilitator training\nSection 1881 of the Social Security Act ( 42 U.S.C. 1395rr ) is amended by adding at the end the following new subsection:\n(i) Living kidney donor transplant facilitator training demonstration program (1) In general Not later than 180 days after the date of the enactment of this subsection, the Secretary shall establish an 8-year demonstration program under which, for each year of the program, the Secretary shall pay to each eligible hospital participating in the program for such year an amount equal to the reasonable costs of the hospital in operating a living kidney donor transplant facilitator training program described in paragraph (3) for such year, as determined by the Secretary. (2) Eligible hospital A hospital is eligible to participate in the demonstration program under this subsection if such hospital is a hospital in which kidney transplants are performed. (3) Living kidney donor transplant facilitator training program described A living kidney donor transplant facilitator training program described in this paragraph is a program operated by a hospital that trains individuals to\u2014 (A) assist individuals who are entitled to benefits under parts A and B of this title and have been determined to have end-stage renal disease in identifying prospective living kidney donors; and (B) assist individuals entitled to benefits under parts A and B of this title pursuant to subsection (d) in successfully navigating the kidney donation process. (4) Waiver The Secretary may waive such provisions of this title as may be necessary in order to implement the demonstration program. (5) Reports (A) Initial report Not later than 6 years after the date of the enactment of this subsection, the Secretary shall submit to the appropriate committees of Congress a report that includes, with respect to the 5-year period following such date of enactment, the following information: (i) Any increase in the number of living kidney donors, as compared to the 5-year period preceding such date of enactment. (ii) Any increase in the number of transplants conducted using kidneys donated by living donors, as compared to the 5-year period preceding such date of enactment. (iii) Outcome measures for individuals that received kidneys from living donors during such period. (iv) Any cost savings to the Medicare program attributable to the increase in transplant services and the decline in dialysis services, as compared to the 5-year period preceding such date of enactment. (v) Qualitative information with respect to transplants conducted using kidneys donated by living donors during such period, as determined based on interviews of facilitators, volunteers at eligible hospitals participating in the demonstration program established under paragraph (1) , living kidney donors, and kidney transplant recipients. (B) Subsequent reports Not later than 1 year after the initial report is submitted under subparagraph (A) , and annually thereafter for the next 2 years, the Secretary shall submit to the appropriate committees of Congress a report that includes updates to the information described in clauses (i) through (v) of such subparagraph. (C) Definitions In this paragraph: (i) Appropriate committees of Congress The term appropriate committees of Congress means\u2014 (I) the Committee on Ways and Means and the Committee on Energy and Commerce of the House of Representatives; and (II) the Committee on Finance of the Senate. (ii) Facilitator The term facilitator means an individual who has received training under a living kidney donor transplant facilitator training program described in paragraph (3). .",
      "versionDate": "2026-02-13",
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
        "updateDate": "2026-03-11T14:21:22Z"
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
      "date": "2026-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7581ih.xml"
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
      "title": "LOVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T06:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LOVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T06:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Living Organ Volunteer Engagement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T06:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to establish a demonstration program to provide payment under the Medicare program for living kidney donor transplant facilitator training.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T06:18:28Z"
    }
  ]
}
```
