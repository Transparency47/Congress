# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6649?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6649
- Title: Fit Vets Act
- Congress: 119
- Bill type: HR
- Bill number: 6649
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-01-31T09:05:38Z
- Update date including text: 2026-01-31T09:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-15 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-15 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6649",
    "number": "6649",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Fit Vets Act",
    "type": "HR",
    "updateDate": "2026-01-31T09:05:38Z",
    "updateDateIncludingText": "2026-01-31T09:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-15T18:12:55Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CO"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "NE"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "DE"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6649ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6649\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mrs. Kiggans of Virginia (for herself, Mr. Neguse , Mr. Panetta , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to conduct a pilot program on providing access to a senior exercise program for enrolled veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fit Vets Act .\n#### 2. Pilot program on access to senior exercise program for enrolled veterans\n##### (a) Establishment\nThe Secretary of Veterans Affairs shall carry out a pilot program to provide to eligible veterans described in subsection (b) access to the health and fitness program referred to as SilverSneakers , or another evidence-based senior exercise program the Secretary determines comparable to such program, as part of the health care furnished under the laws administered by the Secretary.\n##### (b) Eligible veterans\nAn eligible veteran described in this subsection is a veteran\u2014\n**(1)**\nenrolled in the patient enrollment system under section 1705 of title 38, United States Code; and\n**(2)**\nwho satisfies the criteria for participation in the pilot program under subsection (a), as established by the Secretary in regulations.\n##### (c) Scope\nThe Secretary may carry out the pilot program under subsection (a) on a national or regional basis, as the Secretary determines appropriate.\n##### (d) Termination\nThe authority to carry out the pilot program under subsection (a) shall terminate on the date that is three years after the date of the establishment of the pilot program.\n##### (e) Report\nNot later than 180 days after the date on which the pilot program terminates under subsection (c), the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report containing the following:\n**(1)**\nThe rates of participation in such pilot program by covered veterans.\n**(2)**\nThe costs of such pilot program.\n**(3)**\nAn analysis of the effect of such pilot program on the health outcomes of participants, including with respect to physical fitness and chronic disease management.\n**(4)**\nRecommendations by the Secretary on whether to make such pilot program permanent.",
      "versionDate": "2025-12-11",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T16:55:04Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6649ih.xml"
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
      "title": "Fit Vets Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T07:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fit Vets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T07:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Veterans Affairs to conduct a pilot program on providing access to a senior exercise program for enrolled veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T07:33:25Z"
    }
  ]
}
```
