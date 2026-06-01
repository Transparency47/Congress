# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7520?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7520
- Title: Efficiency Adjustment Delay Act
- Congress: 119
- Bill type: HR
- Bill number: 7520
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-05-14T08:07:34Z
- Update date including text: 2026-05-14T08:07:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7520",
    "number": "7520",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "E000298",
        "district": "4",
        "firstName": "Ron",
        "fullName": "Rep. Estes, Ron [R-KS-4]",
        "lastName": "Estes",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Efficiency Adjustment Delay Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:34Z",
    "updateDateIncludingText": "2026-05-14T08:07:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:03:15Z",
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
          "date": "2026-02-12T14:03:10Z",
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
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "KS"
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
      "sponsorshipDate": "2026-05-12",
      "state": "DC"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "KS"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NC"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7520ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7520\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Estes (for himself and Mr. Suozzi ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to delay the implementation of an efficiency adjustment to work relative value units under the Medicare physician fee schedule.\n#### 1. Short title\nThis Act may be cited as the Efficiency Adjustment Delay Act .\n#### 2. Delaying the implementation of an efficiency adjustment to work relative value units under the Medicare physician fee schedule\n##### (a) In general\nSection 1848(c) of the Social Security Act ( 42 U.S.C. 1395w\u20134(c) ) is amended by adding at the end the following new paragraph:\n(9) Delayed implementation of work RVU efficiency adjustment (A) Delayed implementation The Secretary may not implement the policy established in the final rule published on November 5, 2025 (90 Fed. Reg. 49266 et seq.), that establishes an efficiency adjustment to work relative value units, and makes corresponding updates to the intraservice portion of physician time inputs for non-time-based services, before January 1, 2030. (B) Report to Congress Not later than 2 years after the date of the enactment of this paragraph, the Secretary shall submit to the Committee on Energy and Commerce and the Committee on Ways and Means of the House of Representatives, and to the Committee on Finance of the Senate, a report containing an assessment of whether it is necessary to apply a one-time, across-the-board adjustment to work relative value units, and to make corresponding updates to the intraservice portion of physician time inputs for non-time-based services, with respect to services that have not been revalued or reviewed within the 10-year period preceding the calendar year in which such one-time adjustment would be applied. Such report shall include supporting evidence for such assessment. (C) Limitations on future implementation (i) In general Subject to clause (ii) , in the case that the report under subparagraph (B) supports the implementation of the efficiency adjustment described in subparagraph (A) , the Secretary may implement such adjustment on or after January 1, 2030, if the following conditions are met: (I) Before implementing such adjustment, the Secretary consults with representatives of physician specialties affected by the potential implementation of such adjustment. (II) The Secretary does not implement such adjustment with respect to services that have been revalued or reviewed within the 10-year period preceding the calendar year in which such one-time adjustment would be applied. (III) The Secretary establishes a methodology for calculating such adjustment that does not rely on a factor that is used for determining productivity relative to inflation unless the update to the nonqualifying APM conversion factor under section 1848(d) for the year in which the one-time adjustment would be applied is greater than or equal to the percentage increase in the consumer price index for all urban consumers (all items; United States city average) over the previous year. (ii) Multiple adjustments prohibited The Secretary may not implement such an efficiency adjustment more than once. (D) Rule of construction Nothing in subparagraph (A) shall be construed to prevent the Secretary from revaluing misvalued codes for specific services or assigning values to new or revised codes for services. .\n##### (b) Adjustment to conversion factor\nSection 1848(d)(20) of the Social Security Act ( 42 U.S.C. 1395w\u20134(d)(20) ) is amended\u2014\n**(1)**\nby striking 0.75 percent and inserting 1.24 percent ;\n**(2)**\nby striking 0.25 percent and inserting 0.74 percent ;\n**(3)**\nby striking For 2026 and each subsequent year and inserting the following:\n(A) Update for 2026 For 2026 ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(B) Update for 2027 and subsequent years For 2027 and each subsequent year, the update to the qualifying APM conversion factor established under paragraph (1)(A) is 0.75 percent, and the update to the nonqualifying APM conversion factor established under such paragraph is 0.25 percent. .",
      "versionDate": "2026-02-12",
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
        "updateDate": "2026-02-20T17:43:36Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7520ih.xml"
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
      "title": "Efficiency Adjustment Delay Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T08:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Efficiency Adjustment Delay Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T08:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to delay the implementation of an efficiency adjustment to work relative value units under the Medicare physician fee schedule.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T08:33:59Z"
    }
  ]
}
```
