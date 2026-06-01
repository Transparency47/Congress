# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5091?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5091
- Title: To amend section 5545 of title 5, United States Code, to provide hazard pay for carrying out prescribed burns, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5091
- Origin chamber: House
- Introduced date: 2025-09-02
- Update date: 2026-02-24T09:05:42Z
- Update date including text: 2026-02-24T09:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-09-02: Introduced in House

## Actions

- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5091",
    "number": "5091",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001228",
        "district": "2",
        "firstName": "Celeste",
        "fullName": "Rep. Maloy, Celeste [R-UT-2]",
        "lastName": "Maloy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "To amend section 5545 of title 5, United States Code, to provide hazard pay for carrying out prescribed burns, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:42Z",
    "updateDateIncludingText": "2026-02-24T09:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
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
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-02",
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
          "date": "2025-09-02T16:01:15Z",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NV"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CO"
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
      "sponsorshipDate": "2025-11-04",
      "state": "VA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "AK"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "FL"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "MI"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5091ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5091\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 2, 2025 Ms. Maloy introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend section 5545 of title 5, United States Code, to provide hazard pay for carrying out prescribed burns, and for other purposes.\n#### 1. Sense of Congress\nIt is the sense of Congress that the control and suppression of prescribed fires is an important part of fire preparedness and land management. Firefighters who engage in such suppression of prescribed fires take on risks, smoke exposure, and arduous tasks comparable to those in wildfire suppression. They should receive hazard pay to fairly compensate their risk and efforts. Likewise, smokejumpers are aerial delivery firefighters whose role in firefighting necessitates jumping from airplanes, which is a hazardous duty that should receive hazard pay.\n#### 2. Hazard pay for performing prescribed burns\n##### (a) In general\nSection 5545 of title 5, United States Code, is amended by adding at the end the following new subsection:\n(e) (1) For the purposes of subsection (d), duties involving the ignition, control, or suppression of a prescribed burn and duties involving parachute jumps from flying aircraft by smokejumper firefighters for training, proficiency, or operational purposes are duties involving unusual physical hardship or hazard for which the applicable pay differential under such subsection shall be equal to the pay differential for fighting forest and range fires on the fireline. (2) In this subsection, the term prescribed burn means the intentional application of fire to live or dead vegetation or forestry, range, or other landscapes for the purposes of land or resource management. .\n##### (b) Regulations\nNot later than 90 days after the date of the enactment of this Act, the Director of the Office of Personnel Management shall issue such regulations as are necessary to implement the amendment made by subsection (a).\n##### (c) Applicability\nThe amendment made by subsection (a) shall apply with respect to pay periods beginning after the earlier of\u2014\n**(1)**\nthe date on which the Director of the Office of Personnel Management issues the regulations required by subsection (b); or\n**(2)**\nthe date that is 90 days after the date of the enactment of this Act.\n##### (d) Rule of construction\nThis section and the amendments made this section may not be construed as rescinding, replacing, or otherwise affecting any determination of the duties for which a pay differential is provided under subsection (d) of section 5545 of title 5, United States Code, as of the date of the enactment of this Act, except to the extent necessary for any such pay differential for a duty described in subsection (e)(1) of such section, as added by subsection (a), to comply with such subsection (e)(1).",
      "versionDate": "2025-09-02",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-17T20:06:14Z"
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
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5091ih.xml"
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
      "title": "To amend section 5545 of title 5, United States Code, to provide hazard pay for carrying out prescribed burns, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-04T07:33:21Z"
    },
    {
      "title": "To amend section 5545 of title 5, United States Code, to provide hazard pay for carrying out prescribed burns, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T08:05:52Z"
    }
  ]
}
```
